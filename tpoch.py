import os
import time
from datetime import datetime
from zoneinfo import ZoneInfo
from terminal_tui import TerminalTUI
from regions import regions


def tod():
    time_of_day = datetime.now().hour
    if 6 <= time_of_day <= 17:
        return "Day"

    elif 18 <= time_of_day <= 20:
        return "Evening"

    elif 5 >= time_of_day or time_of_day >= 21:
        return "Night"


def show_local():
    local_time = datetime.now()
    return "Local: " + local_time.strftime("%I:%M %p")


cities = regions()


try:
    while True:
        os.system("clear")
        tui = TerminalTUI()
        tui.display_header()
        tui.display_time(city["name"], city["timezone"])
        print("Time of Day: ", tod())
        print(show_local())
        print("Last Updated: ", datetime.now().strftime("%I:%M %p"))
        interval = 60 - datetime.now().second
        time.sleep(interval)


except KeyboardInterrupt:
    pass
