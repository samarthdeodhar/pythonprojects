import datetime
import time
from os import system, name


def clear():
    # for windows
    #print("name of the OS", name)
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


clear()
#start of the program

# while True:
#     x = datetime.datetime.now()
#     hour = x.hour
#     min = x.minute
#     seconds = x.second
#     print (hour,":",min,":",seconds)
#     time.sleep(1)
#     clear()
#     if seconds == 0:
#         exit()

x = datetime.datetime.now()
min_start = x.minute

while True:
    x = datetime.datetime.now()
    hour = x.hour
    min = x.minute
    seconds = x.second
    print (hour,":",min,":",seconds)
    time.sleep(1)
    clear()
    start_time = min
    if min != min_start:
        exit()