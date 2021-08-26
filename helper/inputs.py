from datetime import datetime, timedelta

from helper import outputs, sys_interactions, constants

### Capture user input for integers.
def int_input(description):
    outputs.header(str.format("-{0}-",description))
    input_value = None
    while input_value == None:
        input_value = get_input()
        if input_value == "":
            return 0
        
        try:
            input_value = int(input_value)
        except ValueError:
            outputs.error(constants.Inputs.needs_integer)
            input_value = None

    return input_value

### Generic method to get input.
def get_input():
    input_value = input()
    return input_value if input_value != constants.Console.quit else sys_interactions.out()

### Capture user input for time in H:M format. 
def time_input(date):
    input_time = None
    while input_time == None:
        input_time = get_input()
        if input_time in constants.Inputs.skip_activity:
            input_time = None
            break
        try:
            input_time = datetime.strptime(input_time, "%H:%M").replace(year=date.year,month=date.month,day=date.day)
        except ValueError:
            outputs.error(constants.Inputs.date_parse_error)
            input_time = None

    return input_time

### Capture user input of a date in dd.mm.yyyy format.
def date_input():
    outputs.header(constants.Inputs.date_entry_hint)
    input_date = None
    while input_date == None:
        input_date = get_input()
        try:
            if input_date == "y" or input_date == "yesterday":
                input_date = (datetime.now() - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
                print(input_date)
            else:
                input_date = datetime.strptime(input_date, "%d.%m.%Y")
        except ValueError:
            outputs.error(constants.Inputs.date_parse_error)
            input_date = None

    return input_date


### Capture user input for lists of start and stop times of a given activity in JSON serializable format.
def start_stop_times_input(activity, date):
    start_input = []
    stop_input = []
    add_event = True
    while(add_event):
        outputs.header(str.format("-{0}-",activity))
        outputs.header("started:")
        next_start_time = time_input(date)

        if next_start_time is not None:
            outputs.header("stopped:")
            next_stop_time = time_input(date)

            # every start time must have a corresponding stop time.
            if next_stop_time is not None:
                if next_start_time < next_stop_time:
                    start_input.append(next_start_time.isoformat())
                    stop_input.append(next_stop_time.isoformat())
                else:
                    outputs.error(constants.Inputs.stop_too_early)
            else:
                break
        else:
            break

    ## package data in JSON-serializable dicts.
    return {"start_time": start_input, "stop_time": stop_input } if start_input is not [] else None