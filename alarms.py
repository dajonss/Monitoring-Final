class Alarm:
    def __init__(self, name):  # Constructor
        self.name = name
        self.thresholds = []  # Create empty list to store set alarms

    def set_alarm(self, threshold):  # Add new alarm to the thresholds list
        self.thresholds.append(threshold)
        print(f"{self.name} alarm set at {threshold}%.")

    def check_alarm(self, usage):  # Check alarms against set alarms
        for threshold in self.thresholds:  # Loop over set alarms agains threshold set by the user
            if usage > threshold:
                print(f"*** {self.name} ALARM: Usage is above {threshold}% ***")
                return True
        return False

    def show_alarms(self):  # Show alarms in order
        if not self.thresholds:  # If no alarms are set, notify the user.
            print(f"No alarms set for {self.name}.")
        else:
            # Sort the thresholds list using a lambda function
            sorted_thresholds = sorted(
                self.thresholds, key=lambda threshold: threshold)
            # Display the sorted alarms.
            print(f"{self.name} Alarms: {
                  '%, '.join(map(str, sorted_thresholds))}%")


def cpu_alarm(cpu_alarm_obj):  # Get cpu_alarm_obj from main.py
    # Set alarm level for CPU alarm.
    threshold = input("Enter alarm level for CPU (1-100%): ")
    if threshold.isdigit() and 1 <= int(threshold) <= 100:  # Input sanitaztion
        # Appends alarm entered by the user with .set_alarm method in Class Alarm
        cpu_alarm_obj.set_alarm(int(threshold))
    else:
        print("ERROR: Please enter a valid integer between 1-100.")


def ram_alarm(ram_alarm_obj):  # Get cpu_alarm_obj from main.py
    # Set alarm level for RAM alarm.
    threshold = input("Enter alarm level for RAM (1-100%): ")
    if threshold.isdigit() and 1 <= int(threshold) <= 100:  # Input sanitaztion
        # Appends alarm entered by the user with .set_alarm method in Class Alarm
        ram_alarm_obj.set_alarm(int(threshold))
    else:
        print("ERROR: Please enter a valid integer between 1-100.")


def hdd_alarm(hdd_alarm_obj):  # Get cpu_alarm_obj from main.py
    # Set alarm level for HDD alarm.
    threshold = input("Enter alarm level for HDD (1-100%): ")
    if threshold.isdigit() and 1 <= int(threshold) <= 100:  # Input sanitaztion
        # Appends alarm entered by the user with .set_alarm method in Class Alarm
        hdd_alarm_obj.set_alarm(int(threshold))
    else:
        print("ERROR: Please enter a valid integer between 1-100.")


def show_alarms(alarms):  # Menu 4 - Show alarms
    # Calls Alarms Dictionary from main
    
    # Call the show_alarms method of the CPU alarm object
    alarms["CPU"].show_alarms()
    # Call the show_alarms method of the RAM alarm object
    alarms["RAM"].show_alarms()
    # Call the show_alarms method of the HDD alarm object
    alarms["HDD"].show_alarms()
