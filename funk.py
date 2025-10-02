import psutil
import time

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
                print("Du måste välja en siffra mellan 1-6.")
        except ValueError:
            print("Ogiltigt val! Det måste vara en siffra.")

def alarm_choice():
    while True:
        alarm_input = input("\nGör ett menyval 1-4: ")
        try:
            alarm_number = int(alarm_input)
            if 1 <= alarm_number <= 6:
                return alarm_number
            else:
                    print("Du måste välja en siffra mellan 1-4.")
        except ValueError:
                print("Ogiltigt val! Det måste vara en siffra.")
    
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
     alarms_dict[alarm_type] = percentage
     print((f"✓ Larm för {alarm_type} satt till {percentage}%"))

def check_alarms(cpu, memory, disk):
    if alarms_dict["cpu"] is not None and cpu >= alarms_dict["cpu"]:
          alarms_dict.append(f"⚠️ CPU-LARM: {cpu}% (gräns: {alarms_dict["cpu"]}%)")

    if alarms_dict["memory"] is not None and memory >= alarms_dict["memory"]:
          alarms_dict.append(f"⚠️ MINNE-LARM: {memory}% (gräns: {alarms_dict["memory"]}%)")

    if alarms_dict["disk"] is not None and disk >= alarms_dict["disk"]:
          alarms_dict.append(f"⚠️ DISK-LARM: {disk}% (gräns: {alarms_dict["disk"]}%)")

    return alarms_dict