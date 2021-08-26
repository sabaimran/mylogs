class Console():
    welcome = "**************************\n***Welcome to datainput***\n**************************"
    help_desc = "'weight': weight data, datetime recorded as now\n'routine': routine data, entered with start and stop times\n'menses': menstrual flow data.\n'help': Select this option for more help"
    help = ["help","h"]
    entry_prompt = "Which data would you like to enter? Type 'help' to see options or 'quit' at any time to exit."
    save_options = ["s", "save"]
    quit = "quit"
    invalid_client = "Client name was not valid."

class Common():
    date = "date"

class Inputs():
    needs_integer = "enter an integer value"
    date_entry_hint = "date as dd.mm.yyyy:"
    date_parse_error = "invalid time. type 'none' or 'n' or press enter if you did not complete this."
    stop_too_early = "The stop time is earlier than the start time. Try again!"
    skip_activity = ["none", "n", ""]

class Routine():
    name = "routine"
    file_name = "routine.json"
    activities = [ "workout", "meditate", "code", "read" ]
    header_instructions = "Type 'none' or 'n' or press enter if the entry was not completed today."
    overwrite_warning = "This entry already exists. You will overwrite its data. Do you wish to continue?"

class Menses():
    name = "menses"
    file_name = "menses.csv"
    attributes = ["flow", "cramps", "mood", "nipple"]

class Weight():
    name = "weight"
    file_name = "weights.csv"