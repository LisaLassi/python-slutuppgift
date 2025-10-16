import psutil
import os
import json
from functions import write_log

"""Class for monitoring system resources, managing system data & alarms."""
class SystemMonitor:
        
        def __init__(self):
            self.alarms_file = os.path.join("system_logs", "alarms.json")
            self.alarms = {
                "cpu" : [],
                "memory" : [],
                "disk" : []
            }
            self.load_alarms()

        def load_alarms(self):
            """ bla bla Laddar larm från JSON-fil om den finns"""

            if os.path.exists(self.alarms_file):
                try:
                    with open(self.alarms_file, 'r', encoding='utf-8') as f:
                        self.alarms = json.load(f)
                    write_log(f"Loaded {sum(len(v) for v in self.alarms.values())} alarms from file")
                
                except:
                    write_log("Error loading alarms, using empty alarm list")

        def save_alarms(self):
            """bla bla Sparar larm till json-fil"""

            os.makedirs(os.path.dirname(self.alarms_file), exist_ok=True)
            with open(self.alarms_file, 'w', encoding='utf-8') as f:
                json.dump(self.alarms, f, indent=4)
        write_log("Alarms saved to file")

        def get_cpu(self):
            """Get current CPU usage percentage."""
            return psutil.cpu_percent(interval=1)

        def get_memory(self):
            """Get current memory statistics."""
            return psutil.virtual_memory()
        
        def get_disk(self):
            """Get current disk usage for the system drive."""
            if os.name == 'nt': #Windows
                return psutil.disk_usage('C:\\')
            else: #Linux/ Mac
                return psutil.disk_usage('/') # Ger "felmeddelande" pga att min dator kör windows.
        
        def get_all_stats(self):
            """Get all system statistics at once."""
            return self.get_cpu(), self.get_memory(), self.get_disk()
        
        def add_alarm(self, alarm_type, percentage):
            """Add a new alarm threshold"""

            self.alarms[alarm_type].append(percentage)
            print(f"\n--- ✓ Alarm for {alarm_type} set to {percentage}% ---")
            write_log(f"Alarm created: [{alarm_type}] set to ({percentage}%)")
            self.save_alarms()
            return True # Gör egentligen ingenting, då jag inte använder mig av något vilkor om detta är sant eller falskt. Men bra att ha för att veta att något lyckades och la till något.
        
        def show_alarms(self):
            """Display all currently configured alarms."""

            write_log("Listed alarms")
            if not any (self.alarms.values()):
                print("No alarms set yet.")
            else:
                print("\n• CURRENT ALARMS •\n")
                # Iterate through all alarm types in sorted order
                for alarm_type in sorted(self.alarms.keys()):
                    percentages = self.alarms[alarm_type] # Hämtar listan med procentsatser

                    # Only display if there are alarms for this type
                    if percentages:
                        # Display each threshold for this alarm type
                        for p in percentages:
                            print(f"- {alarm_type.upper()}: {p}%")

        def check_alarms(self, cpu, memory, disk):
            """Check if any alarm thresholds have been exceeded."""

            print("\n • Monitoring active • \n")
            for level in self.alarms["cpu"]: # Går igenom alla cpu larmgränser
                if cpu >= level: # Kollar om nuvarande cpu användning är = eller över larmgränsen
                    print(f"*** WARNING! CPU-ALARM ACTIVATED! cpu usage exceeds {level}%, current at {cpu:.1f}%) ***")
                    write_log(f"CPU alarm triggered: current at {cpu}%, level set at {level}%") 

            for level in self.alarms["memory"]:
                if memory >= level:
                    print(f"*** WARNING! MEMORY-ALARM ACTIVATED! memory usage exceeds {level}%, current at {memory}% ***")
                    write_log(f"MEMORY alarm triggered: current at {memory}%, level set at {level}%")

            for level in self.alarms["disk"]:
                if disk >= level:
                    print(f"*** WARNING! DISK-ALARM ACTIVATED! disk usage exceeds {level}%, current at {disk}% ***")
                    write_log(f"DISK alarm triggered: current at {disk}%, level set at {level}%")
        
        def clear_screen(self):
            """Clear the terminal screen (cross-platform)."""
            os.system('cls' if os.name == 'nt' else 'clear')