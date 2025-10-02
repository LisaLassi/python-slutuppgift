import psutil
import time

def main():
    menu_is_running = True

    from funk import print_main_menu
    from funk import menu_choice
    from funk import monitoring

    monitoring_started = False
        
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
            print("\n-----------------ÖVERVAKNING----------------")
            print(f"| CPU-användning: {cpu}%                     |"
                f" \n| Minnesanvändning: {memory.percent}% | {memory.used // (1024**6)} GB av {memory.total // (1024**3)} GB   |"
                f" \n| Diskanvändning: {disk.percent}%    | {disk.used // (1024**3)} GB av {disk.total //(1024**3)} GB |")
            print("--------------------------------------------")
            input("\n Tryck Enter för att bekräfta ")
            

        elif menu_input == 3: #Skapa larm
            pass

        elif menu_input == 4: #Visa larm
            pass

        elif menu_input == 5: #Skapa övervakningsläge
            pass
            
        elif menu_input == 6:
            print("Avslutar programmet...")
            menu_is_running = False

if __name__ == "__main__":
    main()