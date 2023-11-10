from classes import Warrior, Shop
from camp import meet_camp_captain, return_to_camp
from utilities import clear_console

def welcome():
    clear_console()
    print("\nWelcome to the land of Eretia.")
    print("You are a warrior and you must defeat the monsters!\n")
    name = input("What is your name?\n")
    return name

def game_over():
    print("Game over.\n")
    exit()

def start_game(shop):
    player_name = welcome()
    player = Warrior(player_name)
    player.gold = 50
    meet_camp_captain(player)
    return_to_camp(player, shop)
    return player

def show_instructions():
    print("\n=== Game Instructions ===")
    print("Here you will fight monsters and gain gold.")
    print("Use the commands provided to interact with the game.")
    print("Menu can only be accessed from the camp")
    input("\nPress Enter to return to the main menu...")
    clear_console()

def main_menu():
    clear_console()
    shop = Shop()  # Create the shop instance here
    player = None

    while True:
        print("\n=== Main Menu ===")
        print("1. New Game")
        print("2. Return to Camp")
        print("3. Save Game")
        print("4. Load Game")
        print("5. Instructions")
        print("6. Exit to Desktop")
        choice = input("Enter your choice (1-6): ").lower().strip()

        if choice == '1':
            if not player:
                player = start_game(shop)
            else:
                print("Game already started. Returning to camp.")
                return_to_camp(player, shop)
        elif choice == '2' and player:
            return_to_camp(player, shop)
        elif choice == '3':
            # Implement save game functionality here
            pass
        elif choice == '4':
            # Implement load game functionality here
            pass
        elif choice == '5':
            show_instructions()
        elif choice == '6':
            print("Exiting game. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()

