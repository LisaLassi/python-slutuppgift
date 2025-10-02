import psutil
import time

def print_main_menu():
    print("------------ Välkommen till programmet ------------\n")
    print ("[1] Starta övervakning\n")
    print ("[2] Lista aktiv övervakning\n")
    print ("[3] Skapa larm\n")
    print ("[4] Visa larm\n")
    print ("[5] Starta övervakningsläge\n")
    print ("[6] Avsluta programmet")
    print("---------------------------------------------------")

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
    

def monitoring():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    return cpu, memory, disk
