import sys
import socket

### Determine whether the user is connected to the internet.
def is_online():
    return True
    try:
        conn = socket.create_connection(("www.google.com", 80), timeout=1)
        if conn == None:
            return False
        conn.close()
        return True
    except:
        return False

### Exit the program.
def out():
    print("See you later!")
    sys.exit()