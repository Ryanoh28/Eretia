from utilities import clear_console
from items import get_loot_drop
import random


# def create_monster_wolf():
#     return Monster("Monster Wolf", 60)

def combat(player, monster, shop):
    
    while player.alive and monster.alive:
        print("\nChoose your action:")
        print("\n1. Attack")
        print("2. Run")
        choice = input("\nEnter your choice (1-2): ").strip()
        clear_console()

        if choice == "1":
            player.normal_attack(monster)
            if not monster.check_if_alive():
                print(f"\nThe {monster.name} has been defeated!\n")
                player.gain_experience(10)

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

        elif choice == "2":
            clear_console()
            print("You managed to escape from the Monster safely.\n")
            #input("Press Enter to continue...")
            return 'escaped'

        if monster.alive:
            monster.monster_attack(player)

    if not player.alive:
        return 'player_defeated'

    return 'end_of_combat'



def fight_monster(player, shop, location):
    clear_console()
    player.in_combat = True

    while player.in_combat:
        monster = create_monster(location)
        print(f"You encounter a Level {monster.level} {monster.name}...")
        combat_result = combat(player, monster, shop)

        if combat_result == 'monster_defeated':
            print(f"\nThe {monster.name} has been defeated!")
            player.gain_experience(10)
            
            from locations.locationfunctions import return_to_location
            return_to_location(player, shop)
            break

        elif combat_result == 'escaped':
            from locations.locationfunctions import return_to_location
            return_to_location(player, shop)
            break

        elif combat_result == 'player_defeated':
            player.handle_player_defeat(shop)
            from locations.locationfunctions import return_to_location
            return_to_location(player, shop)
            break

    player.in_combat = False



def create_monster(location):
    from classes import Monster
    base_health = 60
    
    location_level_ranges = {
        "Dark Forest": (1, 3),  
        "Damp Cave": (4, 8),    
        # Add other locations and level ranges as needed
    }
    
    min_level, max_level = location_level_ranges.get(location, (1, 1))  
    level = random.randint(min_level, max_level)

    monster_names = {
        "Dark Forest": ["Dark Forest Wolf", "Forest Ape", "Shadow Stalker"],
        "Damp Cave": ["Cave Bat", "Grey Slime", "Rock Troll"],
        # Add more names for other locations
    }

    name = random.choice(monster_names.get(location, ["Generic Monster"]))
    
    return Monster(name, base_health, level, level, level, level)



