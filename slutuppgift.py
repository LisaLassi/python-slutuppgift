import psutil
import time

def main():
    from funk import print_main_menu
    from funk import menu_choice
    
    while True:
        print_main_menu()

        menu_choice()

        '''
        try:
            menu_choice = int(input("Gör ett menyval 1-7: "))
            if menu_choice < 1 or menu_choice > 7:
                print("\nOgiltigt val! Du måste skriva en siffra mellan 1-7. Försök igen!\n")
                continue
        except:
            print("\nOgiltigt val! Du måste ange en siffra mellan 1-7. Försök igen!\n")
            continue
        '''

        if menu_choice == 1:
            print()

        elif menu_choice == 2:
            print()

        elif menu_choice == 3:
            print()

        elif menu_choice == 4:
            print()

        elif menu_choice == 5:
            print()

        elif menu_choice == 6:
            print()
        
        elif menu_choice == 7:
            print("Avslutar programmet...")
            break

if __name__ == "__main__":
    main()