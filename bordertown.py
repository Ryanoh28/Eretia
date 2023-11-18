from items import HealthPotion
from classes import Shop
from utilities import clear_console
from locations.darkforest import enter_dark_forest
from missions.eldrin import speak_with_eldrin
from colorama import Fore, Style

def rest(player):
    clear_console()
    player.regain_health(100)  
    player.regenerate_energy() 
    print("Your energy and health have recovered after resting. \n\nPress Enter to continue...")

    input()  


def view_quest_log(player):
    clear_console()
    if not player.quests or all(not quest["accepted"] for quest in player.quests.values()):
        print("You currently have no active quests.")
    else:
        print("Your Quests:")
        for quest_name, quest_info in player.quests.items():
            if quest_info["accepted"] and not quest_info["completed"]:
                print(f"- {quest_name.title()}: In Progress")
            elif quest_info["completed"]:
                print(f"- {quest_name.title()}: Completed")

    input("\nPress Enter to continue...")  

    

def return_to_border_town(player):
    shop = Shop()
    while True:
        clear_console()
        print("You are in Border Town. What would you like to do?\n")
        print("1. Train")
        print("2. Leave Border Town")
        print("3. Visit Tavern")
        print("4. Rest")
        print("5. Inventory")
        print("6. Shop")
        print("7. Quests")
        print("8. Exit to Main Menu")

        choice = input("\nEnter your choice (1-8): ").strip()

        if choice == "1":
            player.training()
        elif choice == "2":
            leave_town(player)
        elif choice == "3":
            visit_tavern(player)
        elif choice == "4":
            rest(player)
        elif choice == "5":
            player.inventory.inventory_menu(player)  
        elif choice == "6":
            shop.shop_menu(player)
        elif choice == "7":
            view_quest_log(player)
        elif choice == "8":
            from game1 import main_menu
            main_menu(player)
        else:
            print("\nInvalid choice. Please enter a number between 1 and 8.\n")



def visit_tavern(player):
    while True:
        clear_console()
        print("You enter the bustling tavern filled with adventurers and townsfolk.\n")
        print("1. Talk to the Guard Captain")
        print("2. Listen to rumors")
        print("3. Speak with Eldrin the Greenwarden")
        print("4. Leave the tavern")
        tavern_choice = input("\nWhat would you like to do? ").lower().strip()

        if tavern_choice == '1':
            clear_console()
            converse_with_guard_captain(player)
        elif tavern_choice == '2':
            clear_console()
            listen_to_rumors(player)
        elif tavern_choice == '3':
            clear_console()
            speak_with_eldrin(player)
        elif tavern_choice == '4':
            clear_console()
            print("You leave the tavern and head back to the town center.")
            break  # Breaks out of the loop to return to the town menu
        else:
            print("\nInvalid choice. Please enter a valid option.")
        input("\nPress Enter to continue...")


def listen_to_rumors(player):
    clear_console()
    # Placeholder for future rumor listening functionality
    print("#Not implemented yet, low priority#")
    print("You overhear various adventurers sharing stories and rumors about the lands beyond the town. Apparently one named 'Crook' has been seen walking around with an extra sword in his pants...")
    

def leave_town(player):
    while True:
        clear_console()
        print("Where would you like to go?\n")
        print("1. Dark Forest")
        print("2. Damp Cave")
        print("3. The Border")
        print("4. Back to Border Town")
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            enter_dark_forest(player)
            player.current_location = 'dark_forest'
            break
        elif choice == "2":
            # Assuming enter_damp_cave function exists in dampcave.py
            from locations.dampcave import enter_damp_cave
            player.current_location = 'damp_cave'
            enter_damp_cave(player)
            break
        elif choice == "3":
            
            from locations.theborder import enter_the_border
            player.current_location = 'the_border'
            enter_the_border(player)
            break
        elif choice == "4":
            print("\nYou return to Border Town.")
            return_to_border_town(player)
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")



def converse_with_guard_captain(player):
    clear_console()
    print(Fore.YELLOW + "Guard Captain: " + Style.RESET_ALL + "'Greetings, warrior. What brings you to me today?'\n")
    print("1. Ask for advice")
    print("2. Talk with the Captain")
    print("3. Leave the conversation")

    choice = input("\nWhat would you like to do? ").lower().strip()

    if choice == '1':
        clear_console()
        print(Fore.YELLOW + "Guard Captain: " + Style.RESET_ALL +  f"\"Remember, use your strengths wisely and learn from each battle. Every challenge is an opportunity to grow stronger.\"")
    elif choice == '2':
        clear_console()
        # dialogue based on Eldrin's quest status
        if "monster_loot_quest" in player.quests:
            if player.quests["monster_loot_quest"]["completed"]:
                print(Fore.YELLOW + "Guard Captain: " + Style.RESET_ALL +  f"'I've heard you've been quite successful in the Dark Forest, {player.name}. It's no small feat to take on those creatures.'")
            elif player.quests["monster_loot_quest"]["accepted"]:
                print(Fore.YELLOW + "Guard Captain: " + Style.RESET_ALL +  f"'So, Eldrin has you hunting for treasures in the forest? Keep your guard up, {player.name}, and remember, our shop has potions if you need them.'")
            else:
                check_mystic_herb_quest_status(player)
        else:
            check_mystic_herb_quest_status(player)
    elif choice == '3':
        clear_console()
        print(Fore.YELLOW + "Guard Captain: " + Style.RESET_ALL +  f"\"Very well, {player.name}. Stay safe out there.\"")
    else:
        clear_console()
        print(Fore.YELLOW + "Guard Captain: " + Style.RESET_ALL +  f"I'm not sure what you mean. Could you please clarify?\"")

def check_mystic_herb_quest_status(player):
    if "mystic_herb_quest" in player.quests:
        if player.quests["mystic_herb_quest"]["completed"]:
            print(Fore.YELLOW + "Guard Captain: " + Style.RESET_ALL +  f"'Impressive work with Eldrin's herbs, {player.name}. The Blade of Verdant Greens is a fine reward for your efforts.'")
        elif player.quests["mystic_herb_quest"]["accepted"]:
            print(Fore.YELLOW + "Guard Captain: " + Style.RESET_ALL +  f"'Heard you're running around for Eldrin. Be careful in the Dark Forest, {player.name}. It's a dangerous place.'")
        else:
            print(Fore.YELLOW + "Guard Captain: " + Style.RESET_ALL + f"'Eldrin the Greenwarden often has tasks for willing adventurers. Have you spoken with him in the tavern, {player.name}?'")
    else:
        print(Style.DIM + Fore.YELLOW + f"Guard Captain: \"There are always challenges to be found around here, {player.name}. Keep your wits about you.\"")

def meet_guard_captain(player):
    from items import Weapon, HealthPotion, EnchantedFruit
    from locations.dampcave import Rune, MageStaff
    clear_console()
    print("As you enter the town, the Guard Captain approaches you with a stern look.")
    input("\nPress Enter to continue...")
    clear_console()

    print(Fore.YELLOW + "Guard Captain: " + Style.RESET_ALL + f"'Ah, {player.name}, the one who seeks glory in battle! Before you head into the fray, take this Health Potion. You'll need it if you're to survive the dangers that lie ahead.'\n")
    health_potion = HealthPotion()
    player.inventory.add_item(health_potion)
        

#add debug items here to be given
    input("\nPress Enter to continue...")
    clear_console()

    print(Fore.YELLOW + "Guard Captain: " + Style.RESET_ALL +  f"'And take this Rusted Sword as well. It's not much, but it's better than nothing.'" + Style.RESET_ALL)
    rusted_sword = Weapon("Rusted Sword", 0.5, 0.5)
    player.available_weapons.append(rusted_sword)
    print(f"\n{player.name} received a Rusted Sword.")
    input("\nEnter your inventory to equip weapons and armour. Press Enter to continue...")

    clear_console()




    






