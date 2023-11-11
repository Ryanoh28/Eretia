from classes import Monster
from utilities import clear_console
from items import get_loot_drop


def create_monster_wolf():
    return Monster("Monster Wolf", 60)

def combat(player, monster, shop):
    while player.alive and monster.alive:
        choice = input("\nDo you want to (A)ttack or (R)un? ").lower()
        clear_console()

        if choice == "a":
            player.normal_attack(monster)
            if not monster.check_if_alive():
                print(f"\nThe {monster.name} has been defeated!\n")
                loot = get_loot_drop()
                for item in loot:
                    print(f"\nYou found a {item.name}!")
                    player.inventory.add_item(item)
                player.gain_experience(10)
                input("Press Enter to continue...")
                return 'monster_defeated'

            elif monster.alive:
                damage_dealt = monster.monster_attack(player)
                player.lose_health(damage_dealt, monster.strength)

        elif choice == "r":
            clear_console()
            print("You managed to escape from the Monster safely.\n")
            input("Press Enter to continue...")
            player.choice = 'return_to_camp'
            return 'escaped'

    if player.alive and not monster.alive:
        return 'monster_defeated'
    elif not player.alive:
        return 'player_defeated'


def fight_monster(player, shop):
    clear_console()
    player.in_combat = True

    while player.in_combat:
        monster_wolf = create_monster_wolf()
        print("\nYou encounter a Monster Wolf...\n")
        combat_result = combat(player, monster_wolf, shop)

        if combat_result == 'monster_defeated':
            print(f"\nThe {monster_wolf.name} has been defeated!")
            player.gain_experience(10)
            post_combat_options(player, shop)
            if player.choice == 'return_to_camp':
                break
        elif combat_result == 'escaped':
            player.choice = 'return_to_camp'
            break

        elif combat_result == 'player_defeated':
            player.handle_player_defeat(shop)
            break

    player.in_combat = False






def post_combat_options(player, shop):
    while True:
        clear_console()
        leave_choice = input("Would you like to (C)ontinue fighting, (R)eturn to camp, or check (I)nventory? ").lower()

        if leave_choice == "r":
            player.choice = 'return_to_camp'
            break
        elif leave_choice == "i":
            player.inventory.inventory_menu(player)
            clear_console()
        elif leave_choice == "c":
            break
        else:
            print("\nInvalid choice. Please enter 'C' to continue fighting, 'R' to return to camp, or 'I' to check inventory.\n")

# def combat_phase(player, shop):
#     while player.alive:
#         print("\nWhat would you like to do at the camp?\n")
        
#         choice = input("(T)rain, (F)ight, (C)onverse with the captain, (R)est, check (I)nventory, or visit the (S)hop: ").lower()
#         clear_console()

#         if choice == "f":
#             player.in_combat = True
#             fight_monster(player, shop)
#         elif choice == "t":
#             player.training_strength()
#         elif choice == "c":
#             from camp import converse_with_camp_captain
#             converse_with_camp_captain(player)
#         elif choice == "r":
#             player.regain_health(20)
#             print(f"\nYou have rested and regained health. Current health: {player.health}.\n")
#         elif choice == "i":
#             from camp import manage_inventory
#             manage_inventory(player)
#         elif choice == "s": 
#             shop.display_items(player)
#         elif choice == 'm':
#             from game1 import main_menu
#             main_menu(player, shop)
#         else:
#             print("\nInvalid choice. Please enter 'T' to train, 'F' to fight, 'C' to converse, 'R' to rest, 'I' to check inventory, or 'S' to visit the shop.\n")            