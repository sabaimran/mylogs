class Console():
    welcome = "**************************\n***Welcome to datainput***\n**************************"
    help_desc = "'weight': weight data, datetime recorded as now\n'routine': routine data, entered with start and stop times\n'menses': menstrual flow data.\n'help': Select this option for more help"
    help = ["help","h"]
    entry_prompt = "Which data would you like to enter? Type 'help' to see options or 'quit' at any time to exit."
    save_options = ["s", "save"]
    quit_options = ["q", "quit"]
    quit = "quit"
    invalid_client = "Client name was not valid."
    invalid_datastream = "Not a supported data stream. Type 'quit' to exit, or try one of these: {0}."
    header_instructions = "Type 'none' or 'n' or press enter if the entry was not completed today."

class Common():
    date = "date"

class FileTypes():
    csv = ".csv"
    json = ".json"
    json_entry = "index"
    overwrite_warning = "This entry already exists. You will overwrite its data. Do you wish to continue?"

class Config():
    file_name = "config.yaml"
    active = "active"
    filename = "filename"
    data_folder = "data"
    title = "title"

class Inputs():
    needs_integer = "enter an integer value"
    date_entry_hint = "date as dd.mm.yyyy:"
    date_parse_error = "invalid time. type 'none' or 'n' or press enter if you did not complete this."
    stop_too_early = "The stop time is earlier than the start time. Try again!"
    skip_activity = ["none", "n", ""]
