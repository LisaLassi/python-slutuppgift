import psutil
import time
import os

alarms_dict ={
        "cpu" : [],
        "memory" : [],
        "disk" : []
    }

def print_main_menu():
    print("------------ Välkommen till programmet ------------\n")
    print ("[1] Starta övervakning\n")
    print ("[2] Lista aktiv övervakning\n")
    print ("[3] Skapa larm\n")
    print ("[4] Visa larm\n")
    print ("[5] Starta övervakningsläge\n")
    print ("[6] Avsluta programmet")
    print("---------------------------------------------------")

def print_alarm_meny():
    print("\n----Konfiguera larm----\n")
    print("[1] CPU-användning")
    print("[2] Minnesanvändning")
    print("[3] Diskanvändning")
    print("[4] Tillbaka till huvudmeny")

def menu_choice():
    while True:
        menu_input = input("\nGör ett menyval 1-6: ")
        try:
            menu_number = int(menu_input)
            if 1 <= menu_number <= 6:
                return menu_number
            else:
                print("\nDu måste välja en siffra mellan 1-6.")
        except ValueError:
            print("\nOgiltigt val! Det måste vara en siffra.")

def alarm_choice():
    while True:
        alarm_input = input("\nGör ett menyval 1-4: ")
        try:
            alarm_number = int(alarm_input)
            if 1 <= alarm_number <= 4:
                return alarm_number
            else:
                    print("\nDu måste välja en siffra mellan 1-4.")
        except ValueError:
                print("\nOgiltigt val! Det måste vara en siffra.")
    
def monitoring():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    return cpu, memory, disk

def get_valid_percentage(prompt): #lägger till prompt för att kunna skriva ut ett meddelande till användaren och få input.
     while True:
          percentage = input(prompt)
          if percentage.isdigit() and int(percentage) >= 0 and int(percentage) <=100:
               return int(percentage) 
          else:
               print("\nOgiltigt val! Det måste vara en procentsats mellan 0-100\n")

def set_alarm(alarm_type, percentage):
     alarms_dict[alarm_type].append(percentage)
     print((f"✓ Larm för {alarm_type} satt till {percentage}%"))

def show_alarms():
    if not any(alarms_dict.values()):  # om alla listor är tomma
        print("Inga larm är satta ännu.")
    else:
        print("\n📋 Aktuella larm:")
        for alarm_type in sorted(alarms_dict.keys()):  # sortera efter typ
            percentages = alarms_dict[alarm_type]
            if percentages:  # om listan inte är tom
                for p in percentages:
                    print(f"- {alarm_type.upper()}: {p}%")

def check_alarms(cpu, memory, disk):
    """
    Kollar aktuella värden mot larmnivåer i alarms_dict.
    Skriver ut varningsmeddelande för varje larm som överskrids.
    """
    if "cpu" in alarms_dict:
        for level in alarms_dict["cpu"]:
            if cpu >= level:
                print(f"⚠️  CPU-LARM! Aktuell användning: {cpu}% (gräns: {level}%)")

    if "memory" in alarms_dict:
        for level in alarms_dict["memory"]:
            if memory >= level:
                print(f"⚠️  MINNE-LARM! Aktuell användning: {memory}% (gräns: {level}%)")

    if "disk" in alarms_dict:
        for level in alarms_dict["disk"]:
            if disk >= level:
                print(f"⚠️  DISK-LARM! Aktuell användning: {disk}% (gräns: {level}%)")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') 
    #os.name == nt --> betyder windows --> kör cls
    #annars --> kör clear