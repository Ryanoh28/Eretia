from utilities import clear_console
from items import get_loot_drop
from skills.magic import spell_menu
import random

def combat(player, monster):
    
    while player.alive and monster.alive:
        print("\nChoose your action:\n")
        print("1. Attack")
        print("2. Use Spell")
        print("3. Inventory")
        print("4. Run")
        choice = input("\nEnter your choice (1-4): ").strip()
        clear_console()

        if choice == "1":
            player.normal_attack(monster)
        elif choice == "2":
            selected_spell = spell_menu(player, monster)
            if selected_spell:
                selected_spell.cast(player, monster)
        elif choice == "3":
            player.inventory.use_item_interface(player)
        elif choice == "4":
            clear_console()
            print("You managed to escape from the Monster safely.\n")
            input("Press enter to continue...")
            return 'escaped'

        if monster.alive:
            monster.monster_attack(player)

        if not monster.check_if_alive():
            print(f"\nThe {monster.name} has been defeated!\n")
            player.gain_experience(10)
            handle_loot_and_examine(player)
            return 'monster_defeated'

    if not player.alive:
        return 'player_defeated'

    return 'end_of_combat'


def handle_loot_and_examine(player):
    loot = get_loot_drop()
    for item in loot:
        print(f"You found a {item.name}!")
        player.inventory.add_item(item)

        examine_choice = input("Do you want to examine it? (Y/N):\n ").lower().strip()
        if examine_choice == 'y':
            clear_console()
            print(f"\n{item.name}: {item.description}\n")

    input("Press Enter to continue...")





def fight_monster(player, location):
    clear_console()
    
    player.in_combat = True

    while player.in_combat:
        monster = create_monster(location)
        print(f"You encounter a Level {monster.level} {monster.name}...")
        combat_result = combat(player, monster)

        if combat_result == 'monster_defeated':
            print(f"\nThe {monster.name} has been defeated!")
            player.gain_experience(10)
            player.update_monster_kill_log(monster.name)
            
            
        elif combat_result == 'escaped':
            print("You successfully escaped from the monster.")

        elif combat_result == 'player_defeated':
            player.handle_player_defeat()
            break

        break

    from locations.locationfunctions import return_to_location
    return_to_location(player)
    player.in_combat = False






def create_monster(location):
    from classes import Monster
    base_health = 60
    
    location_level_ranges = {
        "Dark Forest": (1, 3),  
        "Damp Cave": (4, 7),    
        "The Border": (8, 15)
        # Add other locations and level ranges as needed
    }
    
    min_level, max_level = location_level_ranges.get(location, (1, 1))  
    level = random.randint(min_level, max_level)

    monster_names = {
    "Dark Forest": [
        "Dark Forest Wolf", 
        "Forest Ape", 
        "Shadow Stalker", 
        "Mystic Owlbeast",   
        "Thorned Lurker",    
        "Whispering Wraith"  
    ],
    "Damp Cave": [
        "Cave Bat", 
        "Grey Slime", 
        "Rock Troll", 
        "Luminous Fungoid",  
        "Echo Serpent",      
        "Crystaline Beetle"  
    ],
    "The Border": [
        "Blighted Sentinel", 
        "Feral Shadehound", 
        "Ravaged Harpy", 
        "Corrupted Ent", 
        "Nightmare Wisp", 
        "Barren Drake"
    ]
}



    name = random.choice(monster_names.get(location, ["Generic Monster Location not set properly"]))
    
    return Monster(name, base_health, level, level, level, level)



