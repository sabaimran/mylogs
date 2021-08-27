# Private, Personalized Logging via Python CLI 🌳️

The motivation behind this project is to formalize notekeeping of day-to-day activities and personal logs that I want to encourage participation in, or generally want to track. Free tools that offer this sort of capability are generally selling our data to data brokers, and I don't exactly want 3rd parties with access to the minute details of my life 😅️.

Naturally, the activities can be amended over time, as the map of one's life and habits change, but I do imagine there will be certain mainstays. In that vein, the tracked attributes should be trivial to amend. 

# Demo

## Command line interface

![A video demo of the data inputs Python CLI](./media/demo_datainputs.gif)

## Data Visualization Web UI

![A video demo of the web UI for data visualization](./media/demo_webui.gif)

# Setup

You should have your folder set up as a git repository before starting. Though it's not necessary, this will help you keep a version-controlled log of your activites over time.

`git clone git@github.com:sabaimran/mylogs.git`

## Configure config.yaml
Each command you want to support should get its own top-level entry. The structure should look like this:
```
command:
    filename: [the filename where it's stored under ./data/]
    title: [the title for the command line]
    active: 
        - metric2
        - metric3
        ...
    inactive:
        - metric0
        - metric1
```

`command`: the command that will kick off a particular data entry.

`title`: what will be printed when you start entering the data in the CLI.

`filename`: the filename. The CLI assumes the file is located under the `data` folder.  

`active`: the list is the attributes for this command that you are still tracking. 

`inactive`: the list of metrics, as the name implies, which are deprecated. Ergo will not show up in the command line for data entry, but are there for your reference and visualization purposes. 


## Adding data

For running the script, I advise using a virtual environment before installing the Python packages for better modularity. Steps 1 and 3 are only required at first run:
1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip3 install -r requirements.txt`
4. `python3 datainputs.py`
    - Within the script, you can specify which 'type' of data you're entering: menses, routine, or weight.
    - When entering data, you can type `s` to push your changes to the remote, if you're connected to the internet.
5. `deactivate`

## Visualizing

I have created a very rudimentary web UI for visualizing the data. With some logs populated, run `node server.js` from root and navigate to `localhost:5000` in order to visualize the various data streams.

Note that I have currently only built support for menses, routine, and weight data.

## Usage

You should be able to use this from any terminal where you can access `node` and `python`. I've used the script on Windows, Ubuntu, and Android clients. 

The primary interaction mode that I have with the data entry interface is via my phone, using [Termux](https://termux.com/) for the actual data entry, and [Tasker](https://tasker.joaoapps.com/) for phone interactions with launching the tool. I find it to be light and easy enough to use on the small screen.

# Feedback

Send me feedback, comments, suggestions! I'm open to any and all commentary on how to make this system better and more streamlined. Over time, I want to extract intelligent inferences from this data to make my life a little smarter 🤨️.