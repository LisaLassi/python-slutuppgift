import psutil
import time

def main():
    from funk import print_main_menu
    menu_is_running = True

    while menu_is_running:
        print_main_menu()

        try:
            menu_choice = int(input("Gör ett menyval 1-5: "))
            if menu_choice < 1 or menu_choice > 5:
                print("\nOgiltigt val! Du måste skriva en siffra mellan 1-5. Försök igen")
                continue
        except:
            print("\nOgiltigt val! Du måste ange en siffra mellan 1-5. Försök igen")
            continue

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

if __name__ == "__main__":
    main()