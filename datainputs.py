import csv
import json
import sys

from datetime import datetime

from helper import constants, operatingsystem, outputs, sys_interactions, inputs, git

# The file path to access the files we want to write to
filepath = ""

# The git repo path we want to use for updating
repopath = ""

### constants for filepaths
weight_filepath = ""
routine_filepath = ""
menses_filepath = ""

### Setup the file path depending on the client which is using the file
def set_filepaths(client):
    global filepath
    global repopath

    if client == "a":
        operating_system = operatingsystem.Android
    elif client == "w":
        operating_system = operatingsystem.Windows
    elif client == "u":
        operating_system = operatingsystem.Ubuntu

    try:
        filepath = operating_system.data_filepath()
        repopath = operating_system.repopath()
    except NameError:
        outputs.error(constants.Console.invalid_client)
        sys_interactions.out()

### Initialize the constants for the filepaths
def initialize_datafiles():
    global weight_filepath
    global routine_filepath
    global menses_filepath

    weight_filepath = str.format(filepath, constants.Weight.file_name)
    routine_filepath = str.format(filepath, constants.Routine.file_name)
    menses_filepath = str.format(filepath, constants.Menses.file_name)

# Get the routine data.
def get_routine_data():
    outputs.title("ROUTINE DATA")
    outputs.header(constants.Routine.header_instructions)
    
    date = inputs.date_input()

    with open(routine_filepath, "r+") as routine_data:
        data = json.load(routine_data)
        routine_data.close()

    overwrite_index = -1

    for index,entry in enumerate(data[constants.Routine.name]):
        if entry[constants.Common.date] == date.isoformat():
            print(constants.Routine.overwrite_warning)
            overwrite_index = index if inputs.get_input() == "yes" else sys_interactions.out()
            break

    # Get inputs for all the relevant activities I'm tracking.
    activities = constants.Routine.activities

    routine_input = { activity: inputs.start_stop_times_input(activity, date) for activity in activities }
    routine_input[constants.Common.date] = date.isoformat()

    ## Write data to file.
    if (overwrite_index > -1):
        data[constants.Routine.name][overwrite_index] = routine_input
    else:
        data[constants.Routine.name].append(routine_input)

    with open(routine_filepath, "w") as routine_data:
        json.dump(data, routine_data, indent=2)
        routine_data.close()

def get_weight_data():
    outputs.title("WEIGHT DATA")

    ## date,weight
    with open(weight_filepath,'a',newline='') as weight_file:
        writer = csv.writer(weight_file)
        writer.writerow([datetime.now().isoformat(),inputs.int_input(constants.Weight.name)])

def get_menses_data():
    outputs.title("MENSES DATA")
    date = inputs.date_input()

    menses_input = [inputs.int_input(attribute) for attribute in constants.Menses.attributes]
    menses_input.insert(0, date)

    ## date,flow,cramps,mood
    with open(menses_filepath,'a',newline='') as menses_file:
        writer = csv.writer(menses_file)
        writer.writerow(menses_input)

if __name__ == '__main__':
    outputs.welcome(constants.Console.welcome)
    set_filepaths(sys.argv[1])
    initialize_datafiles()

    connected = sys_interactions.is_online()
    git = git.GitProxy(repopath)

    # Pull remote changes if user is connected to the internet.
    if connected:
        git.pull()

    while True:
        input_text = ''
        while(input_text == '' or input_text in constants.Console.help):
            if (input_text in constants.Console.help):
                outputs.header(constants.Console.help_desc)
            print(constants.Console.entry_prompt)
            input_text = str(input())

        ### Weight data.
        if (input_text == constants.Weight.name):
            get_weight_data()

        ### Routine data.
        elif (input_text == constants.Routine.name):
            get_routine_data()

        ### Menstrual data.
        elif (input_text == constants.Menses.name):
            get_menses_data()
                
        elif (input_text in constants.Console.save_options):
            # Push local changes if the user is connected to the internet.
            if connected:
                outputs.title("pushing...")
                git.commit_and_push()
                outputs.title("pushed")
            sys_interactions.out()

        else:
            sys_interactions.out()
