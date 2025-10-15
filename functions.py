import psutil
import os
from datetime import datetime

log_file = os.path.join("system_logs", "logs")

def write_log(message):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} | {message}\n")

def print_main_menu():
    print("------------ System monitoring ------------\n")
    print ("[1] Start monitoring")
    print ("[2] List active monitoring")
    print ("[3] Create alarm for cpu/ memory/ disk")
    print ("[4] Show alarms")
    print ("[5] Start monitoring mode")
    print ("[6] Quit program\n")
    print("---------------------------------------------------")

def print_alarm_meny():
    print("\n• Configure alarm •\n")
    print("[1] CPU-usage")
    print("[2] Memory usage")
    print("[3] Disk usage")
    print("[4] Back to main menu")

def main_menu_choice():
    while True:
        menu_input = input("\nMake a menu choice 1-6: ")
        try:
            menu_number = int(menu_input)
            if 1 <= menu_number <= 6:
                return menu_number
        except ValueError:
            pass 
        print("\nInvalid choice. Must be a number between 1-6. Try again.")

def display_stats(cpu, memory, disk):

    used_memory_gb = bytes_to_gb(memory.used)
    total_memory_gb = bytes_to_gb(memory.total)
    used_disk_gb = bytes_to_gb(disk.used)
    total_disk_gb = bytes_to_gb(disk.total)

    print("\n" + "-" * 23 + "MONITORING" + "-" * 23)
    print(f"| {'CPU-usage:':<20} {cpu:>5.1f}%{' ' * 26}|"
    f" \n| {'Memory usage:':<20} {memory.percent:>5.1f}% | {used_memory_gb:>6.2f} GB of {total_memory_gb:>6.2f} GB |"
    f" \n| {'Disk usage:':<20} {disk.percent:>5.1f}% | {used_disk_gb:>6.2f} GB of {total_disk_gb:>6.2f} GB |")
    print("-" * 56)

def bytes_to_gb(bytes_value):
    return bytes_value / (1024**3)

def alarm_menu_choice():
    while True:
        alarm_input = input("\nMake a menu choice 1-4: ")
        try:
            alarm_number = int(alarm_input)
            if 1 <= alarm_number <= 4:
                return alarm_number
        except ValueError:
            pass
        print("\nInvalid choice. Must be a number between 1-4. Try again.")
    
def get_valid_percentage(prompt):
     while True:
          percentage = input(prompt)
          if percentage.isdigit() and int(percentage) >= 0 and int(percentage) <=100:
               return int(percentage) 
          else:
               print("\nInvalid choice. Must be a number between 0-100. Try again.\n")