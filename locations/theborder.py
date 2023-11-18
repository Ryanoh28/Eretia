from combat import fight_monster
from utilities import clear_console
from items import get_location_loot, HealthPotion, ManaPotion, Rune
from locations.locationfunctions import rest_in_location, return_to_location
from colorama import Style, Fore
from missions.missiongenerator import generate_mission, accept_mission, complete_mission
from classes import Shop
from items import Item, Weapon
from game1 import main_menu, save_game, load_game, show_instructions
import random

def enter_the_border(player):
    player.current_location = 'the_border'
    clear_console()

    # Check if the player is visiting The Border for the first time
    if 'first_visit_the_border' not in player.flags:
        print(Fore.YELLOW + "As you approach The Border, you sense an ominous aura. "
              "This is the threshold between Eretia and lands controlled by monsters. "
              "Beyond this point, danger and mystery await.")
        input("\nPress Enter to continue...")
        player.flags.add('first_visit_the_border')

    while True:
        clear_console()
        print("You are at The Border. What would you like to do?\n")
        print("1. Sentinel Garrison")
        print("2. Adventurers' Guild")
        print("3. Border Shop")
        print("4. Border Crossing")
        print("5. Inventory")
        print("6. Quests")
        print("7. Border Town Outskirts")
        print("8. Main Menu") 
        
        choice = input("\nEnter your choice (1-8): ").strip()

        if choice == "1":
            sentinel_garrison(player)
        elif choice == "2":
            adventurer_headquarters(player)
        elif choice == "3":
            border_shop(player)  
        elif choice == "4":
            cross_menu(player)
            
        elif choice == "5":
            player.inventory.inventory_menu(player)
        elif choice == "6":
            from bordertown import view_quest_log
            view_quest_log(player)
            pass
        elif choice == "8":
            player.current_location = 'the_border'
            main_menu(player)  
        elif choice == "7":
            print("\nReturning to Border Town.")
            from bordertown import leave_town
            leave_town(player)
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 8.")

        input("\nPress Enter to continue...")


def sentinel_garrison(player):
    clear_console()
    print("You see many Sentinels on the training grounds practicing their swordplay, "
          "but what catches your eye is the noticeboard and the imposing figure of the Garrison Commander.")
    input("\nPress Enter to continue...")
    
    while True:
        clear_console()
        print("What would you like to do?\n")
        print("1. Read the Noticeboard")
        print("2. Speak with Garrison Commander")
        print("3. Train with the Sentinels")
        print("4. Leave")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            read_noticeboard()
        elif choice == "2":
            if 'met_commander' in player.flags:
                clear_console()
                print("The commander looks too busy at the moment.")
                input("\nPress enter to continue...")
            else:
                converse_with_commander(player)
        elif choice == "3":
            player.training()  
        elif choice == "4":
            print("\nYou decide to leave the Sentinel Garrison.")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")
        #input("\nPress Enter to continue...")

def converse_with_commander(player):
    clear_console()
    if 'met_commander' not in player.flags:
        print(Fore.GREEN + "Garrison Commander: " + Style.RESET_ALL + "'I don't believe we've met. You seem like a new face around these parts. What brings you to the edge of Eretia?'")
        
        print("\nHow do you respond?\n")
        print("1. I seek adventure beyond The Border.")
        print("2. My goal is to battle monsters and become stronger.")
        print("3. I'm not quite sure yet.")
        print("4. To uncover the secrets of The Border.")

        choice = input("\nYour response (1-4): ")

        clear_console()  

        if choice == '1':
            print(Fore.GREEN + "Garrison Commander: " + Style.RESET_ALL + "'Ah, a brave soul! I admire your courage and determination, " + player.name + ". You'll find plenty of challenges and opportunities to prove your mettle. Stay vigilant and may your blade strike true.'")
        elif choice == '2':
            print(Fore.GREEN + "Garrison Commander: " + Style.RESET_ALL + "'A warrior after my own heart! The path of strength is a noble pursuit, " + player.name + ". May your enemies falter before your might.'")
        elif choice == '3':
            print(Fore.GREEN + "Garrison Commander: " + Style.RESET_ALL + "'Uncertainty is a common trait in these lands, " + player.name + ". Take your time to find your calling.'")
        elif choice == '4':
            print(Fore.GREEN + "Garrison Commander: " + Style.RESET_ALL + "'The Border holds many secrets, " + player.name + ". Tread carefully, for not all are meant to be uncovered.'")
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

        player.flags.add('met_commander')
        
    
    else:
        print(Fore.GREEN + "Garrison Commander: " + Style.RESET_ALL + "'The commander looks too busy at the moment.'")
        
    input("\nPress Enter to continue...") 
    
def read_noticeboard():
    clear_console()
    print("The noticeboard is filled with various posters and warnings. Several notices catch your eye:\n")
    
    # Warning about the Blighted Sentinels
    print("1. A weathered poster with bold letters reads:")
    print(Fore.RED + "'Beware! Blighted Sentinels roam The Border. Once our brave defenders, "
          "now twisted by a sinister force. Avoid at all costs! They are strong, merciless, "
          "and unrecognisable from their former selves.'" + Style.RESET_ALL)
    
    # General warnings
    print("\n2. Another notice, with a grim illustration, warns:")
    print(Fore.YELLOW + "'Travelers and adventurers, be on high alert. The Border is fraught with dangers "
          "beyond the Blighted Sentinels. Feral Shadehounds, Ravaged Harpies, and more lurk in the shadows. "
          "Stay vigilant!'" + Style.RESET_ALL)
    
    # Notice about safety measures
    print("\n3. A more recent note advises:")
    print(Fore.GREEN + "'For those crossing into the monster territories: travel in groups, "
          "keep your weapons ready, and always have an escape plan. Report any sightings of "
          "Blighted Sentinels to the Garrison immediately.'" + Style.RESET_ALL)

    input("\nPress Enter to return to the Sentinel Garrison menu...")

def adventurer_headquarters(player):
    while True:
        clear_console()
        print("You are in the Adventurers' Guild. What would you like to do?\n")
        print("1. Front Desk")
        print("2. Bulletin Board")
        print("3. Adventurer Lodging")
        print("4. Leave")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            front_desk(player)
        elif choice == "2":
            bulletin_board(player)
        elif choice == "3":
            adventurer_lodging(player)
        elif choice == "4":
            print("\nLeaving the Adventurer Headquarters.")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")
            input("\nPress Enter to continue...")

def front_desk(player):
    while True:
        clear_console()
        print(Fore.MAGENTA + "Front Desk Attendant: " + Style.RESET_ALL + "'Welcome to the Adventurer Headquarters! How can I assist you today?'\n")
        print("1. Ask about the Headquarters")
        print("2. Join the Adventurer's Guild (100 Gold)")
        print("3. Complete Mission")
        print("4. Leave")

        choice = input("\nYour choice (1-4): ")

        if choice == "1":
            clear_console()
            print(Fore.MAGENTA + "Front Desk Attendant: " + Style.RESET_ALL + "'This place serves as a hub for adventurers like yourself. Whether you're seeking information, rest, or a new quest, you'll find it here.'")
            input("\nPress Enter to continue...")
        elif choice == "2":
            clear_console()
            join_guild(player)
            input("\nPress Enter to continue...")
        elif choice == "3":
            clear_console()
            complete_missions_at_desk(player)
            input("\nPress Enter to continue...")
        elif choice == "4":
            break
        else:
            clear_console()
            print("\nInvalid choice. Please enter a number between 1 and 4.")

def join_guild(player):
    if 'guild_member' not in player.flags:
        if player.gold >= 100:
            player.gold -= 100
            player.flags.add('guild_member')
            player.logbook['missions'] = []  
            player.logbook['monster_kills'] = {} 
            print(Fore.MAGENTA + "Front Desk Attendant: " + Style.RESET_ALL + "'Congratulations! You're now a member of the Adventurer's Guild. Here is your logbook.'")
        else:
            print(Fore.MAGENTA + "Front Desk Attendant: " + Style.RESET_ALL + "'You need 100 gold to join the Adventurer's Guild.'")
    else:
        print(Fore.MAGENTA + "Front Desk Attendant: " + Style.RESET_ALL + "'You're already a member of the Adventurer's Guild.'")

def complete_missions_at_desk(player):
    clear_console()
    if 'guild_member' in player.flags and player.logbook['missions']:
        for mission in player.logbook['missions'][:]:
            if mission['current_kills'] >= mission['required_kills']:
                player.gold += mission['gold_reward']
                print(Fore.MAGENTA + "Front Desk Attendant: " + Style.RESET_ALL + f"'Mission completed! Earned {mission['gold_reward']} gold for defeating {mission['required_kills']} {mission['monster']}.'")
                player.logbook['missions'].remove(mission)
            else:
                print(Fore.MAGENTA + "Front Desk Attendant: " + Style.RESET_ALL + f"'Mission to defeat {mission['required_kills']} {mission['monster']} not yet completed.'")
    else:
        print(Fore.MAGENTA + "Front Desk Attendant: " + Style.RESET_ALL + "'You don't have any missions to complete at the moment.'")

def bulletin_board(player):
    while True:
        clear_console()
        print("Bulletin Board: Available Missions\n")

        if 'guild_member' not in player.flags:
            print("You need to be a member of the Adventurer's Guild to accept missions.")
            input("\nPress Enter to return...")
            break

        missions = [generate_mission() for _ in range(5)]  # Generate 5 missions
        for i, mission in enumerate(missions, 1):
            print(f"{i}. {mission['monster']} in {mission['area']} - {mission['required_kills']} kills for {mission['gold_reward']} gold")

        print("\n6. Return")  # Option to return

        choice = input("\nYour choice (1-6): ")

        if choice in ['1', '2', '3', '4', '5']:  # Choices for missions
            mission_index = int(choice) - 1
            accept_mission(player, missions[mission_index])
        elif choice == '6':
            break  # Return to the previous menu
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
        
        input("\nPress Enter to continue...")

def adventurer_lodging(player):
    clear_console()
    print("You enter the lodging area, a place for adventurers to rest and recover.\n")

    if player.can_rest():
        player.regenerate_energy(100)  
        player.health = player.max_health 
        print("You feel refreshed after some rest.")
    else:
        print("You don't feel the need to rest right now.")

    input("\nPress Enter to continue...")


border_shop_specific_items = {
    'Earth Rune': {'price': 25, 'object': Rune("Earth Rune", "A rune imbued with the power of earth.")},
    'Fire Rune': {'price': 25, 'object': Rune("Fire Rune", "A rune imbued with the power of fire.")},
    'Water Rune': {'price': 25, 'object': Rune("Water Rune", "A rune imbued with the power of water.")}
}


border_shop_instance = Shop(additional_items=border_shop_specific_items)

def border_shop(player):
    while True:
        clear_console()
        print("Welcome to the border!\n")
        print("Choose an option:\n")
        print("1. View items to buy")
        print("2. Sell items")
        print("3. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            view_items_to_buy(player, border_shop_instance)
        elif choice == '2':
            sell_items(player, border_shop_instance)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
            input("\nPress Enter to continue...")

def view_items_to_buy(player, shop):
    shop.display_items_for_sale(player)

def sell_items(player, shop):
    shop.sell_items_interface(player)

def cross_menu(player):
    clear_console()
    if 'first_visit_border_crossing' not in player.flags:
        print(Fore.RED + "Warning: Beyond this point, humans have no influence and monsters roam unabashedly." + Style.RESET_ALL)
        print(Fore.GREEN + "\nTwo Sentinel Guards salute you, praising your bravery and wishing you good luck." + Style.RESET_ALL)
        player.flags.add('first_visit_border_crossing')
        input("\nPress Enter to continue...")

    while True:
        clear_console()
        print("You are at the Border Crossing. What would you like to do?\n")
        print("1. Lower Bonefields")
        print("2. Upper Bonefields")
        print("3. Inventory")
        print("4. Quests")
        print("5. Return")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            lower_bonefields(player)
        elif choice == "2":
            
            pass
        elif choice == "3":
            player.inventory.inventory_menu(player)
        elif choice == "4":
            from bordertown import view_quest_log
            view_quest_log(player)
        elif choice == "5":
            from locations.locationfunctions import return_to_location
            return_to_location(player)  
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")
            input("\nPress Enter to continue...")

def lower_bonefields(player):
    while True:
        clear_console()
        print("The Lower Bonefields stretch out before you, a land of desolation and danger.\n")
        print("1. Adventure into the wilds")
        print("2. Follow the ancient road")
        print("3. Rest")
        print("4. Inventory")
        print("5. Return")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            adventure_into_wilds(player)
        elif choice == "2":
            follow_ancient_road(player)
        elif choice == "3":
            rest_in_location(player) 
        elif choice == "4":
            player.inventory.inventory_menu(player)  
        elif choice == "5":
            print("\nYou decide to head back.")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")
            input("\nPress Enter to continue...")

def adventure_into_wilds(player, first_time=True):
    clear_console()

    energy_cost_per_exploration = 10

    if player.energy < energy_cost_per_exploration:
        print("You don't have enough energy to continue exploring. Rest to regain energy.")
        input("\nPress Enter to continue...")
        return

    if first_time:
        print("You adventure out into the wildlands of the Lower Bonefields...\n")
    else:
        print("You delve deeper into the wildlands...\n")

    player.consume_energy(energy_cost_per_exploration)

    found_item = get_lower_bonefields_loot(LOWER_BONEFIELDS_LOOT)

    if found_item:
        if isinstance(found_item, Item):
            print(f"You found a {found_item.name}!")
            player.inventory.add_item(found_item)
            examine_choice = input("\nDo you want to examine it? (Y/N): ").lower().strip()
            if examine_choice == 'y':
                clear_console()
                print(f"{found_item.name}: {found_item.description}\n")
        elif isinstance(found_item, Weapon):
            print(Fore.CYAN + f"You found a {found_item.name} (Damage: {found_item.extra_damage}, Crit: {found_item.crit_chance_bonus})!" + Style.RESET_ALL)
            player.available_weapons.append(found_item)
        
        input("Press enter to continue...")

    if random.randint(1, 2) == 2:
        clear_console()
        print(Fore.LIGHTRED_EX + "\nAs you explore, a monster emerges from the wildlands!" + Style.RESET_ALL)
        input("\nPress enter to continue...")
        fight_monster(player, "The Border")

    clear_console()
    print("What would you like to do next?\n")
    print("1. Continue adventuring in the wildlands")
    print("2. Return to the crossing")
    next_action = input("\nEnter your choice (1-2): ").strip()

    if next_action == "1":
        adventure_into_wilds(player, first_time=False)
    elif next_action == "2":
        cross_menu(player)
    else:
        clear_console()
        print("Invalid choice. Please enter a valid number.")
        input("\nPress Enter to continue...")


def follow_ancient_road(player):
    # Implement a story tree or narrative-driven adventure
    # This could involve quests, discoveries, and character development
    pass

sentinel_sword = Weapon("Sentinel Sword", "Forged for the valiant Sentinels guarding the fringes of civilisation, this sword bears the marks of numerous battles.", 3, 2.5)
LOWER_BONEFIELDS_LOOT = {
    'Phantom Feather': {'chance': 20, 'object': Item("Phantom Feather", "A feather shimmering with ghostly light.")},
    'Ancient Manuscript': {'chance': 15, 'object': Item("Ancient Manuscript", "A script containing forgotten knowledge.")},
    'Spectral Dust': {'chance': 25, 'object': Item("Spectral Dust", "Dust that glows with a strange, otherworldly light.")},
    'Fossilised Scale': {'chance': 10, 'object': Item("Fossilised Scale", "A scale from a long-extinct creature.")},
    'Cursed Coin': {'chance': 5, 'object': Item("Cursed Coin", "A coin that seems to absorb light.")},
    'Bone Amulet': {'chance': 10, 'object': Item("Bone Amulet", "An amulet made from the bones of an unknown creature.")},
    'Sentinel Sword': {'chance': 1, 'object': sentinel_sword}  
}

def get_lower_bonefields_loot(loot_table):
    total_chance = sum(item['chance'] for item in loot_table.values())
    roll = random.randint(1, total_chance)
    current = 0

    for name, info in loot_table.items():
        current += info['chance']
        if roll <= current:
            return info['object']

    return None