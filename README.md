# Data Entry
The motivation behind this project is to formalize notekeeping of day-to-day activities that I want to encourage participation in, or generally want to track. The activities can be amended over time, as the map of how I would prefer to spend my time changes, but I do imagine there may be certain mainstays.

## Adding data

For running the script, I advise using a virtual environment before installing the Python packages for better modularity. Steps 1 and 3 are only required at first run:
1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip3 install -r requirements.txt`
4. `python3 datainputs.py a | w | u`
    - Within the script, you can specify which 'type' of data you're entering: menses, routine, or weight.
    - When doing entering data, you can type `s` to push your changes to the remote, if you're connected to the internet.
5. `deactivate`

## Visualizing

With the logs populated, run `node server.js` and navigate to `localhost:5000` in order to visualize the various data streams.

## Usage

The primary interaction mode that I have with the data entry interface is via my phone, using [Termux](https://termux.com/) for the actual data entry, and [Tasker](https://tasker.joaoapps.com/) for phone interactions with launching the tool. I find it to be light and easy enough to use on the small screen.
