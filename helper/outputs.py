from termcolor import colored

# Styling to print title.
def title(title):
    print(colored(str.format("[{0}]",title), "magenta"))

# Styling to print header.
def header(header):
    print(colored(header,"green"))

# Styling to print error.
def error(error):
    print(colored(error,"red"))

# Styling to print welcome.
def welcome(welcome):
    print(colored(welcome,"cyan"))

# Styling to print subtitle.
def subtitle(subtitle):
    print(colored(subtitle, "yellow"))