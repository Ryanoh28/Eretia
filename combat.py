from classes import Monster, create_monster
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
                player.gain_experience(100)  # 100 for testing

                loot = get_loot_drop()
                for item in loot:
                    print(f"You found a {item.name}!")
                    player.inventory.add_item(item)
                    
                    examine_choice = input("Do you want to examine it? (Y/N): ").lower().strip()
                    if examine_choice == 'y':
                        clear_console()
                        print(f"\n{item.name}: {item.description}\n")

                input("Press Enter to continue...")
                return 'monster_defeated'

        elif choice == "r":
            clear_console()
            print("You managed to escape from the Monster safely.\n")
            input("Press Enter to continue...")
            player.choice = 'return_to_camp'
            return 'escaped'

        if monster.alive:
            monster.monster_attack(player)  # Monster attacks the player

    if not player.alive:
        return 'player_defeated'
    return 'end_of_combat'



def fight_monster(player, shop, location):
    clear_console()
    player.in_combat = True

    while player.in_combat:
        # Create a monster appropriate for the current location
        monster = create_monster(location)
        print(f"You encounter a {monster.name}...\n")
        combat_result = combat(player, monster, shop)

        if combat_result == 'monster_defeated':
            print(f"\nThe {monster.name} has been defeated!")
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
            print("\nInvalid choice. Please enter 'C' to continue fighting, 'R' to return, or 'I' to check inventory.\n")         