import time
from monitoring_class import SystemMonitor
from functions import print_main_menu, main_menu_choice, print_alarm_menu, write_log
from functions import alarm_menu_choice, get_valid_percentage, display_stats

"""Main program loop for system monitoring application."""
def main():
     # Initialize the system monitor
    monitor = SystemMonitor()

    menu_is_running = True
    monitoring_started = False

    write_log("Program started") 

    while menu_is_running:
        print_main_menu()
        menu_input = main_menu_choice()
        monitor.clear_screen()

         # Option 1: Start monitoring / "Activates" the system
        if menu_input == 1:
            write_log("Monitoring started")
            print("\n• Monitoring has started •\n")
            monitoring_started = True
            input("Press Enter to continue")

        # Option 2: List current stats
        elif menu_input == 2:
            cpu, memory, disk = monitor.get_all_stats()

             # Check if monitoring has been started
            if monitoring_started == False:
                print("\n• No monitoring started •\n")
                input("Press Enter to continue")
                continue

            write_log("Listed active monitoring")
            display_stats(cpu, memory, disk)
            input("\nPress Enter to continue")

         # Option 3: Configure alarms
        elif menu_input == 3:
            alarm_menu_is_running = True
            while alarm_menu_is_running:
                print_alarm_menu()
                alarm_input = alarm_menu_choice()
                monitor.clear_screen()

                # Create CPU alarm
                if alarm_input == 1: 
                    print("\n• Create an alarm for CPU-usage •\n")
                    cpu_percentage = get_valid_percentage("Enter alarm level (1-100): ")
                    monitor.add_alarm("cpu", cpu_percentage)

                # Create Memory alarm
                elif alarm_input == 2:
                    print("\n• Create an alarm for Memory usage •\n")
                    memory_percentage = get_valid_percentage("Enter alarm level (1-100): ")
                    monitor.add_alarm("memory", memory_percentage)

                # Create Disk alarm
                elif alarm_input == 3:
                    print("\n• Create an alarm for Disk usage •\n")
                    disk_percentage = get_valid_percentage("Enter alarm level (1-100): ")
                    monitor.add_alarm("disk", disk_percentage)

                 # Return to main menu
                elif alarm_input == 4:
                    alarm_menu_is_running = False

        # Option 4: Show all configured alarms
        elif menu_input == 4:
            monitor.show_alarms()
            input("\nPress Enter to continue")

        # Option 5: Start active monitoring mode
        elif menu_input == 5:
             # Check if monitoring has been started
            if not monitoring_started:
                print("\n• No monitoring started •\n")
                input("Press Enter to continue")
                continue

            write_log("Started active monitoring")
            try: 
                # Continuous monitoring loop
                while True:
                        cpu, memory, disk = monitor.get_all_stats()
                        monitor.clear_screen()
                    
                         # Display current stats and check alarms
                        display_stats(cpu, memory, disk)
                        monitor.check_alarms(cpu, memory.percent, disk.percent)
                        
                        print("\nPress Ctrl + C to exit")
                        # Update every 2 seconds
                        time.sleep(2)
            
            except KeyboardInterrupt:
                    # Handle Ctrl+C gracefully without crashing
                    write_log("Active monitoring ended")
                    print("\n\n• Monitoring ended •")
                    input('Press Enter to continue')
            
        # Option 6: Exit program
        elif menu_input == 6:
            write_log("Program ended")
            print("\nExiting program..")
            menu_is_running = False

if __name__ == "__main__":
    main()