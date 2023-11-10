from classes import Monster
from utilities import clear_console
from items import GildedFeather, EnchantedStone
import random

def create_monster_wolf():
    return Monster("Monster Wolf", 60)

def combat(player, monster):
    while player.alive and monster.alive:
        choice = input("Do you want to (A)ttack or (R)un? ").lower()
        clear_console()

        if choice == "a":
            damage_dealt = player.normal_attack(monster)
            if not monster.check_if_alive():
                # Monster defeated logic
                print(f"The {monster.name} has been defeated!")
                
                # Determine loot drop
                drop_chance = random.randint(1, 100)
                if drop_chance <= 15:  
                    player.inventory.add_item(GildedFeather())
                    print("You found a Gilded Feather!")
                elif drop_chance <= 5:  
                    player.inventory.add_item(EnchantedStone())
                    print("You found an Enchanted Stone!")

                player.gain_experience(10)
                input("You gained experience! Press Enter to continue...")
                return 'monster_defeated'

            if monster.alive:
                monster.monster_attack(player)
                if not player.check_if_alive():
                    return 'player_defeated'

        elif choice == "r":
            clear_console()
            print("You managed to escape from the Monster Wolf.\n")
            player.choice = 'return_to_camp'  
            return 'escaped'

    if player.alive and not monster.alive:
        return 'monster_defeated'
    elif not player.alive:
        return 'player_defeated'





def combat_phase(player, shop):
    while player.alive:
        print("\nWhat would you like to do at the camp?\n")
        
        choice = input("(T)rain, (F)ight, (C)onverse with the captain, (R)est, check (I)nventory, or visit the (S)hop: ").lower()
        clear_console()

        if choice == "f":
            player.in_combat = True
            fight_monster(player)
        elif choice == "t":
            player.training_strength()
        elif choice == "c":
            from camp import converse_with_camp_captain
            converse_with_camp_captain(player)
        elif choice == "r":
            player.regain_health(20)
            print(f"\nYou have rested and regained health. Current health: {player.health}.\n")
        elif choice == "i":
            from camp import manage_inventory
            manage_inventory(player)
        elif choice == "s":  # Shop option
            shop.display_items()
            item_choice = input("Enter the name of the item you would like to buy: ").lower().strip()
            shop.buy_item(player, item_choice)
        elif choice == 'm':
            from game1 import main_menu
            main_menu()  # Access the main menu
            clear_console()
        else:
            print("\nInvalid choice. Please enter 'T' to train, 'F' to fight, 'C' to converse, 'R' to rest, 'I' to check inventory, or 'S' to visit the shop.\n")

def fight_monster(player, shop):
    clear_console()
    player.in_combat = True

    while player.in_combat:
        monster_wolf = create_monster_wolf()
        clear_console()
        print("\nYou encounter a Monster Wolf...\n")
        combat_result = combat(player, monster_wolf)

        if combat_result in ['monster_defeated', 'escaped']:
            if combat_result == 'monster_defeated':
                print(f"The {monster_wolf.name} has been defeated!")
                player.gain_experience(10)
                input("Press Enter to continue...\n")
                post_combat_options(player, shop)
                if player.choice == 'return_to_camp':
                    return  
            elif combat_result == 'escaped':
                print("You managed to escape from the Monster Wolf.\n")
                player.choice = 'return_to_camp'  
                return  
        elif combat_result == 'player_defeated':
            player.handle_player_defeat(shop)
            break

    player.in_combat = False



def post_combat_options(player, shop):
    leave_choice = input("Would you like to (C)ontinue fighting, (R)eturn to camp, or check (I)nventory? ").lower()
    
    if leave_choice == "r":
        player.choice = 'return_to_camp'
    elif leave_choice == "i":
        clear_console()
        player.inventory.inventory_menu(player)
  
