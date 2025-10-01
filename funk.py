def print_main_menu():
    print("------------ Välkommen till programmet ------------\n")
    print ("[1] Starta övervakning\n")
    print ("[2] Lista aktiv övervakning\n")
    print ("[3] Skapa larm\n")
    print ("[4] Visa larm\n")
    print ("[5] Starta övervakningsläge\n")
    print ("[6] Ta bort alarm\n")
    print ("[7] Avsluta programmet")
    print("---------------------------------------------------")

def menu_choice():
    while True:
        menu_input = input("\nGör ett menyval 1-7: ")
        try:
            menu_number = int(menu_input)
            if 1 <= menu_number <= 7:
                return menu_choice
            else:
                print("Du måste välja en siffra mellan 1-7.")
        except ValueError:
            print("Ogiltigt val! Det måste vara en siffra.")