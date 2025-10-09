import psutil
import os

class SystemMonitor: #Klass för att övervaka systemresurser, hanterar systemdata & larm

        def __init__(self):
            self.alarms = {
                "cpu" : [],
                "memory" : [],
                "disk" : []
            }

        def get_cpu(self): # Hämtar cpu-användning
            return psutil.cpu_percent(interval=1)

        def get_memory(self): # Hämtar minnesanvändning
            return psutil.virtual_memory()
        
        def get_disk(self): # Hämtar diskanvändning
            return psutil.disk_usage('/')
        
        def get_all_stats(self): # Hämtar all systemdata på en gång
            return self.get_cpu(), self.get_memory(), self.get_disk()
        
        def add_alarm(self, alarm_type, percantage): # Lägger till ett larm
            if alarm_type in self.alarms: # Kollar om nyckeln finns i dictionaryn
                self.alarms[alarm_type].append(percantage) # Lägger till den nya procentsatssen i slutet på listan
                print(f"✓ Alarm for {alarm_type} set to {percantage}%")
                return True # Gör egentligen ingenting, då jag inte använder mig av något vilkor om detta är sant eller falskt. Men bra att ha för att veta att något lyckades och la till något.
        
        def show_alarms(self): # Visar alla aktiva larm
            if not any (self.alarms.values()): # Om ingen lista har något innehåll (dvs larm)
                print("No alarms set yet.")
            else:
                print("\nCURRENT ALARMS: ")
                for alarm_type in sorted(self.alarms.keys()): # Går igenom alla nycklar i self.alarm (cpu, memory, disk)
                    percentages = self.alarms[alarm_type] # Hämtar listan med procentsatser
                    if percentages: # Kollar om listan inte är tom
                        for p in percentages: # Loopar igenom varje procentsats i listan
                            print(f"- {alarm_type.upper()}: {p}%")

        def check_alarms(self, cpu, memory, disk): # Kontrollerar om några larm ska triggas
            
            for level in self.alarms["cpu"]: # Går igenom alla cpu larmgränser
                if cpu >= level: # Kollar om nuvarande cpu användning är = eller över larmgränsen
                    print(f"CPU-ALARM!    Current usage: {cpu}%, (Limit: {level})") 

            for level in self.alarms["memory"]:
                if memory >= level:
                    print(f"MEMORY-ALARM! Current usage: {memory}%, (Limit: {level})")

            for level in self.alarms["disk"]:
                if disk >= level:
                    print(f"DISK-ALARM!   Current usage: {disk}%, (Limit: {level})")
        
        def clear_screen(self): # Rensar terminalen
            os.system('cls' if os.name == 'nt' else 'clear')

# Vanliga funktioner - hanterar användargränssnitt
def print_main_menu():
    print("------------ System monitoring ------------\n")
    print ("[1] Start monitoring")
    print ("[2] List active monitoring")
    print ("[3] Create alarm")
    print ("[4] Show alarms")
    print ("[5] Start monitoring mode")
    print ("[6] Quit program\n")
    print("---------------------------------------------------")

def print_alarm_meny():
    print("\n----Configure alarm----\n")
    print("[1] CPU-usage")
    print("[2] Memory usage")
    print("[3] Disk usage")
    print("[4] Back to main menu")

def menu_choice():
    while True:
        menu_input = input("\nMake a menu choice 1-6: ")
        try:
            menu_number = int(menu_input)
            if 1 <= menu_number <= 6:
                return menu_number
        except ValueError:
            pass 
        print("\nInvalid choice. Must be a number between 1-6. Try again.")

def alarm_choice():
    while True:
        alarm_input = input("\nMake a menu choice 1-4: ")
        try:
            alarm_number = int(alarm_input)
            if 1 <= alarm_number <= 4:
                return alarm_number
        except ValueError:
                pass
        print("\nInvalid choice. Must be a number between 1-4. Try again.")
    
def get_valid_percentage(prompt): #lägger till prompt för att kunna skriva ut ett meddelande till användaren innan input.
     while True:
          percentage = input(prompt)
          if percentage.isdigit() and int(percentage) >= 0 and int(percentage) <=100:
               return int(percentage) 
          else:
               print("\nInvalid choice. Must be a percentage between 0-100%. Try again.\n")
