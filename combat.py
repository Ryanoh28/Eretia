from utilities import clear_console
from items import get_loot_drop, EyeOfInsight
from skills.magic import spell_menu
import random
from colorama import Fore, Style

def display_health(player):
    if player.health > 75:
        health_color = Fore.GREEN
    elif 40 < player.health <= 75:
        health_color = Fore.YELLOW
    else:
        health_color = Fore.RED
    
    print(f"Health: {health_color}{player.health}{Style.RESET_ALL}")
def combat(player, monster):
    
    while player.alive and monster.alive:
        print("\n=================")
        display_health(player)
        print("=================")
        print("\nChoose your action:\n")
        print("1. Attack")
        print("2. Use Spell")
        print("3. Inventory")
        print("4. Run")
        
        eye_of_insight = next((item for item in player.inventory.items if isinstance(item, EyeOfInsight)), None)
        if eye_of_insight:
            print("5. Use Eye of Insight")

        choice = input("\nEnter your choice: ").strip()
        clear_console()
        player_action_taken = False

        if choice == "1":
            player.normal_attack(monster)
            player_action_taken = True
        elif choice == "2":
            selected_spell = spell_menu(player, monster)
            if selected_spell:
                selected_spell.cast(player, monster)
                player_action_taken = True
        elif choice == "3":
            item_used = player.inventory.use_item_interface(player)
            player_action_taken = item_used
        elif choice == "4":
            print("You managed to escape from the Monster safely.\n")
            input("Press enter to continue...")
            return 'escaped'
        elif choice == "5" and eye_of_insight:
            eye_of_insight.use(monster)
            player_action_taken = True

        # Monster's turn to attack
        if monster.alive and player_action_taken:
            monster.monster_attack(player)
            if player.stone_skin_turns_remaining > 0:
                player.stone_skin_turns_remaining -= 1
                if player.stone_skin_turns_remaining == 0:
                    player.reduce_defence_post_effect()

        # Check if monster is defeated
        if not monster.check_if_alive():
            print(f"\nThe {monster.name} has been defeated!")
            player.gain_experience(monster.level) 
            handle_loot_and_examine(player)  
            input("\nPress Enter to continue...")
            return 'monster_defeated'

        # Check if player is defeated
        if not player.alive:
            return 'player_defeated'

    return 'end_of_combat'



def handle_loot_and_examine(player):
    loot = get_loot_drop()
    for item in loot:
        print(f"You found a {item.name}!")
        player.inventory.add_item(item)

        examine_choice = input("\nDo you want to examine it? (Y/N):\n ").lower().strip()
        if examine_choice == 'y':
            clear_console()
            print(f"\n{item.name}: {item.description}\n")




def fight_monster(player, location):
    clear_console()
    player.in_combat = True

    while player.in_combat:
        monster = create_monster(location)
        if monster.level < player.level:
            level_color = Fore.GREEN
        elif monster.level == player.level:
            level_color = Fore.YELLOW
        else:
            level_color = Fore.RED
        print(f"You encounter a {level_color}Level {monster.level}{Style.RESET_ALL} {monster.name}...")
        combat_result = combat(player, monster)

        if combat_result == 'monster_defeated':
            #player.gain_experience(monster.level)
            #print(f"\nThe {monster.name} has been defeated!\n")  # Show defeat message
            #handle_loot_and_examine(player)  # Handle loot after showing XP gain
            player.update_monster_kill_log_and_missions(monster.name)
        elif combat_result == 'escaped':
            #print("You successfully escaped from the monster.")
            pass
        elif combat_result == 'player_defeated':
            input("\nYou've been defeated!\n")
            player.handle_player_defeat()
            break

        break

    from locations.locationfunctions import return_to_location
    return_to_location(player)
    player.in_combat = False






def create_monster(location):
    from classes import Monster
    base_health = 80
    
    location_level_ranges = {
        "Dark Forest": (1, 3),  
        "Damp Cave": (4, 7),    
        "The Border": (11, 25),
        "Echoing Cavern": (10,10), # Special mission monster
        "Human Bandit": (10,25),
        "Northern Hills Unique": (3,3),
        "Northern Hills": (5,10)
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
    ],
    "Echoing Cavern": [
        "Illusionary Monster" ],
     
     "Human Bandit": [
         "Human Bandit"
     ],

     "Northern Hills Unique": [
         "Hill Hound"
         ],
    
     "Northern Hills": [
        "Frost-Feathered Eagle", 
        "Stonehide Boar", 
        "Gale Howler Wolf", 
        "Hill Serpent", 
        "Mist Wraith",
        "Hill Hound"
    ]
}



    name = random.choice(monster_names.get(location, ["Generic Monster Location not set properly"]))
    
    return Monster(name, base_health, level, level, level, level)



