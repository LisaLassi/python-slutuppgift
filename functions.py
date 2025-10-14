import psutil
import os

# Vanliga funktioner - hanterar användargränssnitt
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
    print("\n----------------MONITORING---------------")
    print(f"| CPU-usage: {cpu}%                       |"
    f" \n| Memory usage: {memory.percent}% | {memory.used // (1024**3)} GB av {memory.total // (1024**3)} GB   |"
    f" \n| Disk usage: {disk.percent}%    | {disk.used // (1024**3)} GB av {disk.total //(1024**3)} GB |")
    print("-----------------------------------------")

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