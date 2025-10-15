import psutil
import os
from functions import write_log

#Klass för att övervaka systemresurser, hanterar systemdata & larm
class SystemMonitor:
        
        def __init__(self):
            self.alarms = {
                "cpu" : [],
                "memory" : [],
                "disk" : []
            }

        def get_cpu(self):
            return psutil.cpu_percent(interval=1)

        def get_memory(self):
            return psutil.virtual_memory()
        
        def get_disk(self):
            if os.name == 'nt': #Windows
                return psutil.disk_usage('C:\\')
            else: #Linux/ Mac
                return psutil.disk_usage('/') # Ger "felmeddelande" pga att min dator kör windows.
        
        def get_all_stats(self):
            return self.get_cpu(), self.get_memory(), self.get_disk()
        
        def add_alarm(self, alarm_type, percantage):
                self.alarms[alarm_type].append(percantage)
                print(f"\n--- ✓ Alarm for {alarm_type} set to {percantage}% ---")
                write_log(f"Alarm created: [{alarm_type}] set to ({percantage}%)")
                return True # Gör egentligen ingenting, då jag inte använder mig av något vilkor om detta är sant eller falskt. Men bra att ha för att veta att något lyckades och la till något.
        
        def show_alarms(self):
            write_log("Listed alarms")
            if not any (self.alarms.values()):
                print("No alarms set yet.")
            else:
                print("\n• CURRENT ALARMS •\n")
                for alarm_type in sorted(self.alarms.keys()): # Går igenom alla nycklar i self.alarm + sorterar efter typ(cpu, memory, disk)
                    percentages = self.alarms[alarm_type] # Hämtar listan med procentsatser
                    if percentages: # Kollar om listan inte är tom
                        for p in percentages: # Loopar igenom varje procentsats i listan
                            print(f"- {alarm_type.upper()}: {p}%")

        def check_alarms(self, cpu, memory, disk): # Kontrollerar om några larm ska triggas
            print("\n • Monitoring active • \n")
            for level in self.alarms["cpu"]: # Går igenom alla cpu larmgränser
                if cpu >= level: # Kollar om nuvarande cpu användning är = eller över larmgränsen
                    print(f"*** WARNING! CPU-ALARM ACTIVATED! cpu usage exceeds {level}%, current at {cpu}%) ***")
                    write_log(f"CPU alarm triggered: current at {cpu}%, level set at {level}%") 

            for level in self.alarms["memory"]:
                if memory >= level:
                    print(f"*** WARNING! MEMORY-ALARM ACTIVATED! memory usage exceeds {level}%, current at {memory}% ***")
                    write_log(f"CPU alarm triggered: current at {memory}%, level set at {level}%")

            for level in self.alarms["disk"]:
                if disk >= level:
                    print(f"*** WARNING! DISK-ALARM ACTIVATED! disk usage exceeds {level}%, current at {disk}% ***")
                    write_log(f"CPU alarm triggered: current at {disk}%, level set at {level}%")
        
        def clear_screen(self):
            os.system('cls' if os.name == 'nt' else 'clear')