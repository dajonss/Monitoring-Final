# main.py

from monitoring import get_cpu_usage, get_disk_usage, get_ram_usage
from surveillance import surveillance_mode
from alarms import cpu_alarm, ram_alarm, hdd_alarm, show_alarms, Alarm
import os

# Initialize Alarm objects for CPU, RAM, and HDD.
cpu_alarm_obj = Alarm("CPU")
ram_alarm_obj = Alarm("RAM")
hdd_alarm_obj = Alarm("HDD")


# Dictionary for Alarms
alarms = {
    "CPU": cpu_alarm_obj,
    "RAM": ram_alarm_obj,
    "HDD": hdd_alarm_obj
}

# Check if user has started the monitoring before running it
begin_monitoring = False


def main_menu():  # Options showed for user as the main menu
    print("1. Start monitoring")
    print("2. Show current monitoring")
    print("3. Create Alarm")
    print("4. Show Alarms")
    print("5. Start surveillance-mode")
    print("6. Exit")

def start_monitoring():  # Menu 1 - Start monitoring
    global begin_monitoring
    if begin_monitoring == False:
        begin_monitoring = True
        print("Monitoring has started..")
    else:
        print("Monitoring already active..")


def current_monitoring():  # Menu 2 - Current monitoring of CPU, RAM and HDD
    if begin_monitoring is True:
        # Get current snapshot usages from monitoring.py
        get_cpu_usage()
        get_ram_usage()
        get_disk_usage()
        input("Press any key to return to main menu...")
        main_menu_loop()
    else:
        input("Start the monitoring to see current usages, press any key to continue..")
        main_menu_loop()

def create_alarms():  # Menu 3 - Create alarms for CPU, RAM and HDD
    print("1. CPU Usage")
    print("2. RAM Usage")
    print("3. HDD Usage")
    print("4. Return to Main Menu..")
    while True:
        create_alarm = input("Choose an option: ")
        if create_alarm == "1":
            cpu_alarm(cpu_alarm_obj) # Prompt the user to set a CPU usage threshold and store it in the cpu_alarm_obj
            break
        elif create_alarm == "2":
            ram_alarm(ram_alarm_obj) # Prompt the user to set a HDD usage threshold and store it in the ram_alarm_obj
            break
        elif create_alarm == "3":
            hdd_alarm(hdd_alarm_obj) # Prompt the user to set a HDD usage threshold and store it in the hdd_alarm_obj
            break
        elif create_alarm == "4":
            main_menu_loop() # Return to main menu
        else:
            print("ERROR: Choose a valid option in the menu..")


def main_menu_loop():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') # Clears console
        main_menu()
        option = input("Choose an option: ")
        if option == "1":
            start_monitoring()
            input("Press any key to return to main menu...")
        elif option == "2":
            current_monitoring()
            input("Press any key to return to main menu...")
        elif option == "3":
            create_alarms()
            input("Press any key to return to main menu...")
        elif option == "4":
            show_alarms(alarms)
            input("Press any key to return to main menu...")
        elif option == "5":
            surveillance_mode(ram_alarm_obj.thresholds,
                              cpu_alarm_obj.thresholds, hdd_alarm_obj.thresholds)
        elif option == "6":
            exit()
        else:
            print("Error: Choose a valid option")


print("Welcome to the monitoring program")
main_menu_loop()
