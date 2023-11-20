import pickle
import os
import sys
from classes import Warrior
from bordertown import meet_guard_captain, return_to_border_town
from utilities import clear_console
from colorama import init, Fore, Style
from locations.locationfunctions import return_to_location
init(autoreset=True)  

def list_save_files():
    save_path = "saves"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    return [f for f in os.listdir(save_path) if os.path.isfile(os.path.join(save_path, f))]

def save_game(player):
    save_path = "saves"
    save_files = list_save_files()

    print("Select a slot to save your game:\n")
    for i, file in enumerate(save_files, 1):
        print(f"{i}. {file.replace('.pkl', '')}")
    print(f"{len(save_files) + 1}. Create new save")

    choice = int(input("\nEnter your choice: "))

    if choice <= len(save_files):
        filename = save_files[choice - 1]
    else:
        print("Enter a name for your new save file:")
        filename = input().strip() + ".pkl"

    filepath = os.path.join(save_path, filename)

    with open(filepath, 'wb') as file:
        pickle.dump(player, file)

    print(f"Game saved successfully in slot {choice}.")

def load_game():
    save_path = "saves"
    save_files = list_save_files()

    if not save_files:
        print("No saved games found.")
        return None

    print("\nAvailable saves:\n")
    for i, file in enumerate(save_files, 1):
        print(f"{i}. {file.replace('.pkl', '')}")

    choice = int(input("\nEnter the number of the save file to load: "))
    filepath = os.path.join(save_path, save_files[choice - 1])

    with open(filepath, 'rb') as file:
        player = pickle.load(file)

    print(f"Game loaded from slot {choice}.")
    return_to_location(player)
    return player


def welcome():
    clear_console()
    print("Welcome to the land of " + Style.DIM + Fore.YELLOW + "Eretia" + Style.RESET_ALL + ".\n")
    print("Drawn by tales of untold challenges and uncharted frontiers, you have journeyed to Eretia's perilous edges. Here, where civilisation meets the wild, legends are born, and warriors are tested against the hordes of monsters that roam these ancient lands.\n")
    name = input(Style.DIM + Fore.YELLOW + "Brave adventurer, what is your name?\n" + Style.RESET_ALL)
    return name

def game_over():
    print("Game over.\n")
    exit()

def start_game():
    player_name = welcome()
    player = Warrior(player_name)
    player.gold = 50 # Testing
    meet_guard_captain(player)
    return_to_border_town(player)
    return player

def show_instructions():
    print("\n=== Game Instructions ===")
    print("Here you will fight monsters and gain gold.")
    print("Use the commands provided to interact with the game.")
    print("Menu can only be accessed from Border Town")
    input("\nPress Enter to return to the main menu...")
    clear_console()

def main_menu(player=None):
    clear_console()

    while True:
        print("=== Main Menu ===")
        print("1. New Game")
        print("2. Continue Game")
        print("3. Save Game")
        print("4. Load Game")
        print("5. Instructions")
        print("6. Exit to Desktop")
        print("=================")
        choice = input("Enter your choice (1-6): ").lower().strip()

        if choice == '1':
            if player is None:
                player = start_game()
                return_to_location(player)  
            else:
                print("Game already started.")
                return_to_location(player)  

        elif choice == '2':
            if player:
                return_to_location(player)  
            else:
                print("No ongoing game to continue. Please start a new game.")

        elif choice == '3':
            if player:
                save_game(player)
            else:
                print("No game to save. Please start a new game.")

        elif choice == '4':
            try:
                player = load_game()
                if player:
                    print("Game loaded successfully.")
                    return_to_location(player)  
            except FileNotFoundError:
                print("No saved game found. Please start a new game.")

        elif choice == '5':
            show_instructions()

        elif choice == '6':
            print("Exiting game. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            input("Press Enter to continue...")

        clear_console()

if __name__ == "__main__":
    main_menu(player=None)



