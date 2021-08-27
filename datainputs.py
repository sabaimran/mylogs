# This script parses input data and adds encodes it in files which house all my collected info.
# The program will loop if user enters information that is in incorrect format.
# As of 23.07.2021, it supports menses, routine, and weight data. 

import csv
import json
import os
import yaml

from helper import constants, outputs, sys_interactions, inputs, git

# The directory path for where this file is running. This is especially helpful for the case where the caller executing thes script is outside of the directory.
dirname = os.path.dirname(__file__)

# The file path to access the files we want to write to
filepath = os.path.join(dirname, constants.Config.data_folder) + "/{0}"

# The git repo path we want to use for updating
repopath = ""

config = None

def check_date_overwrite(date, data):
    for index,entry in enumerate(data[constants.FileTypes.json_entry]):
        if entry[constants.Common.date] == date.isoformat():
            outputs.error(constants.FileTypes.overwrite_warning)
            return index if inputs.get_input() == "yes" else sys_interactions.out()

def get_filepath(filename):
    return str.format(filepath, filename)

def csv_data(local_config):
    date = inputs.date_input()

    data_source = get_filepath(local_config[constants.Config.filename])

    data_input = [inputs.int_input(attribute) for attribute in local_config[constants.Config.active]]
    data_input.insert(0, date)

    with open(data_source,'a',newline='') as raw_data:
        writer = csv.writer(raw_data)
        writer.writerow(data_input)

def json_data(local_config):
    date = inputs.date_input()
    
    data_source = get_filepath(local_config[constants.Config.filename])
    with open(data_source, "r+") as raw_data:
        data = json.load(raw_data)
        raw_data.close()

    overwrite_index = check_date_overwrite(date, data)
    outputs.header(constants.Console.header_instructions)
    data_input = { activity: inputs.start_stop_times_input(activity, date) for activity in local_config[constants.Config.active]}
    data_input[constants.Common.date] = date.isoformat()

    ## Write data to file.
    if (overwrite_index):
        data[constants.FileTypes.json_entry][overwrite_index] = data_input
    else:
        data[constants.FileTypes.json_entry].append(data_input)

    with open(data_source, "w") as raw_data:
        json.dump(data, raw_data, indent=2)
        raw_data.close()

def user_input(local_config):
    outputs.title(local_config[constants.Config.title])
    file = local_config[constants.Config.filename]
    print(file)
    if file[-5:] == constants.FileTypes.json:
        json_data(local_config)
    elif file[-4:] == constants.FileTypes.csv:
        csv_data(local_config)

def load_config():
    global config

    stream = open(os.path.join(dirname, constants.Config.file_name), "r")
    config = yaml.load(stream, Loader=yaml.FullLoader)

if __name__ == '__main__':
    outputs.welcome(constants.Console.welcome)
    load_config()

    connected = sys_interactions.is_online()
    git = git.GitProxy(dirname)

    # Pull remote changes if user is connected to the internet.
    if connected:
        git.pull()

    while True:
        outputs.header(constants.Console.entry_prompt)
        input_text = ''
        while(input_text == '' or input_text in constants.Console.help):
            if (input_text in constants.Console.help):
                outputs.header(constants.Console.help_desc)
            input_text = str(input())

        if input_text in constants.Console.save_options:
            # Push local changes if the user is connected to the internet, and exit.
            if connected:
                outputs.title("pushing...")
                git.commit_and_push()
                outputs.title("pushed")
            sys_interactions.out()

        elif input_text in constants.Console.quit_options:
            # The quit command
            sys_interactions.out()

        elif input_text in config:
            # A command was hit
            user_input(config[input_text])
            outputs.subtitle("done!")

        else:
            outputs.error(constants.Console.invalid_datastream.format(list(config.keys())))
