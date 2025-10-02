import psutil
import time

def main():
    menu_is_running = True
    monitoring_started = False
    alarm_menu_is_running = True

    from funk import print_main_menu
    from funk import menu_choice
    from funk import monitoring
    from funk import print_alarm_meny
    from funk import alarm_choice
    from funk import get_valid_percentage
    from funk import set_alarm
    from funk import check_alarms
    from funk import alarms_dict
        
    while menu_is_running:
        print_main_menu()
        menu_input = menu_choice()

        if menu_input == 1: #Starta övervakning
            print("\n• Övervakningen har startat •\n")
            monitoring_started = True

        elif menu_input == 2: #Lista övervakning
            cpu, memory, disk = monitoring()
            if monitoring_started == False:
                print("\n• Ingen övervakning startad •\n")
                continue
            print("\n-----------------ÖVERVAKNING-----------------")
            print(f"| CPU-användning: {cpu}%                     |"
                f" \n| Minnesanvändning: {memory.percent}% | {memory.used // (1024**6)} GB av {memory.total // (1024**3)} GB   |"
                f" \n| Diskanvändning: {disk.percent}%    | {disk.used // (1024**3)} GB av {disk.total //(1024**3)} GB |")
            print("---------------------------------------------")
            input("\n Tryck Enter för att bekräfta ")
            

        elif menu_input == 3: #Skapa larm
            while alarm_menu_is_running:
                print_alarm_meny()
                alarm_input = alarm_choice()

                if alarm_input == 1:
                    print("\n---Du valde att skapa ett larm för CPU-användning---\n")
                    cpu_percentage = get_valid_percentage("Ange vilken procentsats du vill bli larmad om: ")
                    set_alarm("cpu", cpu_percentage)

                elif alarm_input == 2:
                    print("\n---Du valde att skapa ett larm för Minnesanvändning---\n")
                    memory_percentage = get_valid_percentage("Ange vilken procentsats du vill bli larmad om: ")
                    set_alarm("memory", memory_percentage)

                elif alarm_input == 3:
                    print("\n---Du valde att skapa ett larm för Diskanvändning---\n")
                    disk_percentage = get_valid_percentage("Ange vilken procentsats du vill bli larmad om: ")
                    set_alarm("disk", disk_percentage)

                elif alarm_input == 4:
                    alarm_menu_is_running = False

        elif menu_input == 4: #Visa larm
            print("\n=====AKTIVA LARM=====\n")
            
            
            input("\nTryck Enter för att bekräfta\n")

        elif menu_input == 5: #Skapa övervakningsläge
            pass
            
        elif menu_input == 6:
            print("Programmet avslutas")
            menu_is_running = False

if __name__ == "__main__":
    main()