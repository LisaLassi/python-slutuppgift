import psutil
import os
import time
import msvcrt #för att kunna kolla om användaren tryckt enter

def main():
    menu_is_running = True
    monitoring_started = False
    alarm_menu_is_running = True

    from funk import print_main_menu, menu_choice, monitoring, print_alarm_meny, alarm_choice
    from funk import get_valid_percentage, set_alarm, show_alarms, check_alarms, clear_screen
    #from funk import alarms_dict 
    #Behöver tydligen inte importera dictionaryn för att den redan används internt i funk
        
    while menu_is_running:
        print_main_menu()
        menu_input = menu_choice()

        if menu_input == 1: #Starta övervakning
            print("\n• Övervakningen har startat •\n")
            monitoring_started = True
            input("Tryck Enter för att bekräfta")

        elif menu_input == 2: #Lista övervakning
            cpu, memory, disk = monitoring()
            if monitoring_started == False:
                print("\n• Ingen övervakning startad •\n")
                input("Tryck Enter för att bekräfta")
                continue
            print("\n-----------------ÖVERVAKNING-----------------")
            print(f"| CPU-användning: {cpu}%                      |"
                f" \n| Minnesanvändning: {memory.percent}% | {memory.used // (1024**3)} GB av {memory.total // (1024**3)} GB   |"
                f" \n| Diskanvändning: {disk.percent}%    | {disk.used // (1024**3)} GB av {disk.total //(1024**3)} GB |")
            print("---------------------------------------------")
            input("\n Tryck Enter för att bekräfta ")
            

        elif menu_input == 3: #Skapa larm
            alarm_menu_is_running = True
            while alarm_menu_is_running:
                print_alarm_meny()
                alarm_input = alarm_choice()

                if alarm_input == 1:
                    print("\n---Skapa ett larm för CPU-användning---\n")
                    cpu_percentage = get_valid_percentage("Ange vilken procentsats du vill bli larmad om: ")
                    set_alarm("cpu", cpu_percentage)

                elif alarm_input == 2:
                    print("\n---Skapa ett larm för Minnesanvändning---\n")
                    memory_percentage = get_valid_percentage("Ange vilken procentsats du vill bli larmad om: ")
                    set_alarm("memory", memory_percentage)

                elif alarm_input == 3:
                    print("\n---Skapa ett larm för Diskanvändning---\n")
                    disk_percentage = get_valid_percentage("Ange vilken procentsats du vill bli larmad om: ")
                    set_alarm("disk", disk_percentage)

                elif alarm_input == 4:
                    alarm_menu_is_running = False

        elif menu_input == 4: #Visa larm
            show_alarms()
            input("\nTryck Enter för att bekräfta")

        elif menu_input == 5: #Skapa övervakningsläge
            if not monitoring_started:
                print("\n• Ingen övervakning startad •\n")
                input("Tryck Enter för att bekräfta")
                continue

            while True:
                    cpu, memory, disk = monitoring()
                    clear_screen() #Rensar skärmen innan ny uppdatering
            
                    print("\n-----------------ÖVERVAKNING-----------------")
                    print(f"| CPU-användning: {cpu}%                     |"
                    f" \n| Minnesanvändning: {memory.percent}% | {memory.used // (1024**3)} GB av {memory.total // (1024**3)} GB   |"
                    f" \n| Diskanvändning: {disk.percent}%    | {disk.used // (1024**3)} GB av {disk.total //(1024**3)} GB |")
                    print("---------------------------------------------")

                    # Här kollar vi larm och skriver ut varningar direkt
                    check_alarms(cpu, memory.percent, disk.percent)
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