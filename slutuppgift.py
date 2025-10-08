import time
import msvcrt

from funk import SystemMonitor
from funk import print_main_menu, menu_choice, print_alarm_meny, alarm_choice, get_valid_percentage

def main():

    monitor = SystemMonitor()

    menu_is_running = True
    monitoring_started = False
    alarm_menu_is_running = True

    while menu_is_running:
        print_main_menu()
        menu_input = menu_choice()

        if menu_input == 1:
            print("\n• Övervakningen har startat •\n")
            monitoring_started = True
            input("Tryck Enter för att fortsätta")

        elif menu_input == 2:
            cpu, memory, disk = monitor.get_all_stats()
            if monitoring_started == False:
                print("\n• Ingen övervakning startad •\n")
                input("Tryck Enter för att fortsätta")
                continue

            print("\n-----------------ÖVERVAKNING-----------------")
            print(f"| CPU-användning: {cpu}%                      |"
                f" \n| Minnesanvändning: {memory.percent}% | {memory.used // (1024**3)} GB av {memory.total // (1024**3)} GB   |"
                f" \n| Diskanvändning: {disk.percent}%    | {disk.used // (1024**3)} GB av {disk.total //(1024**3)} GB |")
            print("---------------------------------------------")
            input("\n Tryck Enter för att fortsätta ")
            

        elif menu_input == 3:
            alarm_menu_is_running = True
            while alarm_menu_is_running:
                print_alarm_meny()
                alarm_input = alarm_choice()

                if alarm_input == 1:
                    print("\n---Skapa ett larm för CPU-användning---\n")
                    cpu_percentage = get_valid_percentage("Ange vilken procentsats du vill bli larmad om: ")
                    monitor.add_alarm("cpu", cpu_percentage)

                elif alarm_input == 2:
                    print("\n---Skapa ett larm för Minnesanvändning---\n")
                    memory_percentage = get_valid_percentage("Ange vilken procentsats du vill bli larmad om: ")
                    monitor.add_alarm("memory", memory_percentage)

                elif alarm_input == 3:
                    print("\n---Skapa ett larm för Diskanvändning---\n")
                    disk_percentage = get_valid_percentage("Ange vilken procentsats du vill bli larmad om: ")
                    monitor.add_alarm("disk", disk_percentage)

                elif alarm_input == 4:
                    alarm_menu_is_running = False

        elif menu_input == 4:
            monitor.show_alarms()
            input("\nTryck Enter för att fortsätta")

        elif menu_input == 5:
            if not monitoring_started:
                print("\n• Ingen övervakning startad •\n")
                input("Tryck Enter för att bekräfta")
                continue

            while True:
                    cpu, memory, disk = monitor.get_all_stats()
                    monitor.clear_screen()
            
                    print("\n-----------------ÖVERVAKNING-----------------")
                    print(f"| CPU-användning: {cpu}%                     |"
                    f" \n| Minnesanvändning: {memory.percent}% | {memory.used // (1024**3)} GB av {memory.total // (1024**3)} GB   |"
                    f" \n| Diskanvändning: {disk.percent}%    | {disk.used // (1024**3)} GB av {disk.total //(1024**3)} GB |")
                    print("---------------------------------------------")

                    monitor.check_alarms(cpu, memory.percent, disk.percent)

                    print("\nTryck Enter för att avsluta övervakning")
                    time.sleep(2)
                    
                    if msvcrt.kbhit():
                        key = msvcrt.getch()
                        if key == b'\r':
                            print("\nÖvervakning avslutad")
                            break
            
        elif menu_input == 6:
            print("\nProgrammet avslutas")
            menu_is_running = False

if __name__ == "__main__":
    main()