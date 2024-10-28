import psutil
from alarms import *
# from alarms import cpu_alarm, ram_alarm, hdd_alarm, show_alarms


def get_cpu_usage():  # Get CPU usage at the moment
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_percent}%")  # Show CPU used in %


def get_ram_usage():  # Get RAM usage at the moment
    ram = psutil.virtual_memory()
    ram_available = ram.available / (1024**3)  # Show ram available in GB
    ram_total = ram.total / (1024**3)  # Show total ram available in GB
    print(f"RAM Usage: {ram.percent}% | {
        round(ram_available, 2)} GB out of {round(ram_total, 2)} GB used.")


def get_disk_usage(): # Get HDD usage at the moment
    hdd = psutil.disk_usage("C:/")  # Path for HDD
    hdd_percent = psutil.disk_usage("C:/").percent  # Convert to Percent
    hdd_free = hdd.free / (1024**3)  # Convert free disk space to GB
    hdd_used = hdd.used / (1024**3)  # Convert used disk space to GB
    print(f"HDD Usage: {hdd_percent}% | {
          round(hdd_used)} GB out of {round(hdd_free)} GB used.")
