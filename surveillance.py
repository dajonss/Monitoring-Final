import time
import datetime
import os
import psutil


# Function to show surveillance to the user in real time
def surveillance_mode(ram_thresholds, cpu_thresholds, hdd_thresholds): # Menu 5 - surveillance mode.

    run = True
    while run:

        # Fetch values takes 1 second
        active_ram = psutil.virtual_memory().percent
        active_hdd = psutil.disk_usage("C:/").percent
        active_cpu = psutil.cpu_percent()

        # clear console
        os.system('cls' if os.name == 'nt' else 'clear')

        # show real-time surveillance, KeyBoardIntterupt-info for user
        print(datetime.datetime.now().replace(microsecond=0))
        print("Surveillance mode started.\n======= Press CTRL+C to return to main menu =======\n")
        print(f"RAM % Used: {active_ram}")
        print(f"CPU % Used: {active_cpu}")
        print(f"HDD % Used: {active_hdd}")

        try:
            # Checks current processors against set levels in thresholds attribute of
            for ram_alarm in ram_thresholds:
                if int(active_ram) > ram_alarm:
                    print(
                        f"\n*** RAM-ALARM ACTIVE *** RAM USAGE ABOVE ALARM LEVEL: {ram_alarm}% ***")

            for cpu_alarm in cpu_thresholds:
                if int(active_cpu) > cpu_alarm:
                    print(
                        f"\n*** CPU-ALARM ACTIVE *** CPU USAGE ABOVE ALARM LEVEL: {cpu_alarm}% ***")

            for hdd_alarm in hdd_thresholds:
                if int(active_hdd) > hdd_alarm:
                    print(
                        f"\n*** HDD-ALARM ACTIVE *** HDD USAGE ABOVE ALARM LEVEL: {hdd_alarm}% ***")
            time.sleep(1)

        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nInterrupted! \nReturning to main menu.\n...")
            time.sleep(1.2)
            os.system('cls' if os.name == 'nt' else 'clear')
            run = False
            # break
