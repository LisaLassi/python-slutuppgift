import time
import msvcrt

from monitoring_class import SystemMonitor
from functions import print_main_menu, main_menu_choice, print_alarm_meny
from functions import alarm_menu_choice, get_valid_percentage

def main():
    monitor = SystemMonitor()

    menu_is_running = True
    monitoring_started = False
    alarm_menu_is_running = True

    while menu_is_running:
        print_main_menu()
        menu_input = main_menu_choice()
        monitor.clear_screen()

        if menu_input == 1:
            print("\n• Monitoring has started •\n")
            monitoring_started = True
            input("Press Enter to continue")

        elif menu_input == 2:
            cpu, memory, disk = monitor.get_all_stats()
            if monitoring_started == False:
                print("\n• No monitoring started •\n")
                input("Press Enter to continue")
                continue

            print("\n----------------MONITORING---------------")
            print(f"| CPU-usage: {cpu}%                       |"
                f" \n| Memory usage: {memory.percent}% | {memory.used // (1024**3)} GB av {memory.total // (1024**3)} GB   |"
                f" \n| Disk usage: {disk.percent}%    | {disk.used // (1024**3)} GB av {disk.total //(1024**3)} GB |")
            print("-----------------------------------------")
            input("\n Press Enter to continue")
            
        elif menu_input == 3:
            alarm_menu_is_running = True
            while alarm_menu_is_running:
                print_alarm_meny()
                alarm_input = alarm_menu_choice()
                monitor.clear_screen()

                if alarm_input == 1:
                    print("\n• Create an alarm for CPU-usage •\n")
                    cpu_percentage = get_valid_percentage("Enter the percentage you want to be alerted about: ")
                    monitor.add_alarm("cpu", cpu_percentage)

                elif alarm_input == 2:
                    print("\n• Create an alarm for Memory usage •\n")
                    memory_percentage = get_valid_percentage("Enter the percentage you want to be alerted about: ")
                    monitor.add_alarm("memory", memory_percentage)

                elif alarm_input == 3:
                    print("\n• Create an alarm for Disk usage •\n")
                    disk_percentage = get_valid_percentage("Enter the percentage you want to be alerted about: ")
                    monitor.add_alarm("disk", disk_percentage)

                elif alarm_input == 4:
                    alarm_menu_is_running = False

        elif menu_input == 4:
            monitor.show_alarms()
            input("\nPress Enter to continue")

        elif menu_input == 5:
            if not monitoring_started:
                print("\n• No monitoring started •\n")
                input("Press Enter to continue")
                continue

            while True:
                    stop_display = False
                    cpu, memory, disk = monitor.get_all_stats()
                    monitor.clear_screen()
                    
                    print("\n---------------MONITORING----------------")
                    print(f"| CPU-usage: {cpu}%                       |"
                    f" \n| Memory usage: {memory.percent}% | {memory.used // (1024**3)} GB of {memory.total // (1024**3)} GB   |"
                    f" \n| Disk usage: {disk.percent}%    | {disk.used // (1024**3)} GB of {disk.total //(1024**3)} GB |")
                    print("-----------------------------------------")

                    monitor.check_alarms(cpu, memory.percent, disk.percent)

                    print("\nPress Enter to exit")
                    time.sleep(2)

                    if msvcrt.kbhit():
                        key = msvcrt.getch()
                        if key == b'\r':
                            print("\n• Monitoring ended •")
                            break
            
        elif menu_input == 6:
            print("\nExiting program..")
            menu_is_running = False

if __name__ == "__main__":
    main()