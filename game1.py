from classes import Warrior, Monster, Shop  
from items import Potion, Inventory  
from camp import return_to_camp, post_combat_options, manage_inventory, converse_with_camp_captain, meet_camp_captain
from utilities import clear_console


def welcome():
    print("\nWelcome to the land of Eretia.")
    print("You are a warrior and you must defeat the monsters!\n")
    name = input("What is your name?\n")
    return name

def create_monster_wolf():
    return Monster("Monster Wolf", 60)

def game_over():
    print("Game over.\n")
    exit()    

def combat(player, monster):
    while player.alive and monster.alive:
        choice = input("Do you want to (A)ttack or (R)un? ").lower()
        clear_console()

        if choice == "a":
            damage_dealt = player.normal_attack(monster)
            if not monster.check_if_alive():  
                print(f"The {monster.name} has been defeated!")  
                player.gain_experience(10) 
                break  
            if monster.alive:
                monster.monster_attack(player)
                if not player.check_if_alive():
                    print(f"{player.name} has been defeated by the {monster.name}.")
                    return 'player_defeated'
        elif choice == "r":
            print("You managed to escape from the Monster Wolf.")
            return 'escaped'  

    # After combat, decide the outcome
    if player.alive and not monster.alive:
        return 'monster_defeated'  
    elif not player.alive:
        return 'player_defeated'  

def combat_phase(player, shop):
    while player.alive:
        print("\nWhat would you like to do at the camp?")
        
        choice = input("(T)rain, (F)ight, (C)onverse with the captain, (R)est, check (I)nventory, or visit the (S)hop: ").lower()
        clear_console()

        if choice == "f":
            player.in_combat = True
            fight_monster(player)
        elif choice == "t":
            player.training_strength()
        elif choice == "c":
            converse_with_camp_captain(player)
        elif choice == "r":
            player.regain_health(20)
            print(f"\nYou have rested and regained health. Current health: {player.health}.\n")
        elif choice == "i":
            manage_inventory(player)
        elif choice == "s":  # Shop option
            shop.display_items()
            item_choice = input("Enter the name of the item you would like to buy: ").lower().strip()
            shop.buy_item(player, item_choice)
        else:
            print("\nInvalid choice. Please enter 'T' to train, 'F' to fight, 'C' to converse, 'R' to rest, 'I' to check inventory, or 'S' to visit the shop.\n")



def fight_monster(player):
    while player.in_combat:
        print("You venture out and encounter a Monster Wolf...\n")
        monster_wolf = create_monster_wolf()
        combat_result = combat(player, monster_wolf)
        if combat_result == 'monster_defeated':
            print("The Monster Wolf has been defeated!\n")
            player.gain_experience(10)
            post_combat_options(player)
        elif combat_result == 'escaped':
            player.in_combat = False
            return_to_camp(player)
        elif combat_result == 'player_defeated':
            game_over()
            break



def main_menu():
    while True:
        clear_console()
        print("\n=== Main Menu ===")
        print("1. Start Game")
        print("2. Instructions")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").lower().strip()

        if choice == '1':
            start_game()  
        elif choice == '2':
            show_instructions() 
        elif choice == '3':
            print("Exiting game. Goodbye!")
            exit() 
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def start_game():
    player_name = welcome()  
    player = Warrior(player_name)  
    player.gold = 50  
    shop = Shop()  
    # ... other setup ...
    combat_phase(player, shop)  


def show_instructions():
    clear_console()
    print("\n=== Instructions ===")
    print("Here are the instructions for the game...")
    # ... other instructions ...


if __name__ == "__main__":
    main_menu()  




