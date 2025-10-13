import psutil
import os

#Klass för att övervaka systemresurser, hanterar systemdata & larm
class SystemMonitor:
        
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
            print("\n • Monitoring active • \n")
            for level in self.alarms["cpu"]: # Går igenom alla cpu larmgränser
                if cpu >= level: # Kollar om nuvarande cpu användning är = eller över larmgränsen
                    print(f"*** WARNING! CPU-ALARM ACTIVATED! cpu usage exceeds {level}%, current at {cpu}%) ***") 

            for level in self.alarms["memory"]:
                if memory >= level:
                    print(f"*** WARNING! MEMORY-ALARM ACTIVATED! memory usage exceeds {level}%, current at {memory}% ***")

            for level in self.alarms["disk"]:
                if disk >= level:
                    print(f"*** WARNING! DISK-ALARM ACTIVATED! disk usage exceeds {level}%, current at {disk}% ***")
        
        def clear_screen(self): # Rensar terminalen
            os.system('cls' if os.name == 'nt' else 'clear')