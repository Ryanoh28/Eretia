from items import HealthPotion, Weapon
from classes import Shop
from utilities import clear_console
from locations.darkforest import enter_dark_forest
from locations.northernhills import enter_northern_hills
from missions.eldrin import speak_with_eldrin
from colorama import Fore, Style
import random

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
    player.current_location = 'border_town'
    shop = Shop()
    while True:
        
        clear_console()
        print("You are in Border Town. What would you like to do?\n")
        print("1. Train")
        print("2. East Gate")
        print("3. West Gate")
        print("4. Visit Tavern")
        print("5. Rest")
        print("6. Inventory")
        print("7. Shop")
        print("8. Quests")
        print("9. Exit to Main Menu")

        choice = input("\nEnter your choice (1-9): ").strip()

        if choice == "1":
            player.training()
        elif choice == "2":
            leave_town(player)
        elif choice == "3":
            leave_town_west(player)
            #pass
        elif choice == "4":
            visit_tavern(player)
        elif choice == "5":
            rest(player)
        elif choice == "6":
            player.inventory.inventory_menu(player)  
        elif choice == "7":
            shop.shop_menu(player)
        elif choice == "8":
            view_quest_log(player)
        elif choice == "9":
            from game1 import main_menu
            main_menu(player)
        else:
            print("\nInvalid choice. Please enter a number between 1 and 9.\n")

def leave_town_west(player):
    while True:
        clear_console()
        print("Not implemented yet\n")
        print("The western path leads inland to more peaceful locations.\n")
        print("1. Meadowlands")
        print("2. Crystal Lake")
        print("3. Ancient Library")
        print("4. Inventory")
        print("5. Return to Border Town")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            pass
            #enter_meadowlands(player)
        elif choice == "2":
            pass
            #enter_crystal_lake(player)
        elif choice == "3":
            pass
            #visit_ancient_library(player)
        elif choice == "4":
            player.inventory.inventory_menu(player)
        elif choice == "5":
            print("\nYou decide to return to the safety of Border Town.")
            return_to_border_town(player)
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

    


def visit_tavern(player):
    while True:
        clear_console()
        print("You enter the bustling tavern filled with adventurers and townsfolk.\n")
        print("1. Talk to the Guard Captain")
        print("2. Listen to the crowd")
        print("3. Speak with Eldrin the Greenwarden")
        print("4. Leave the tavern")
        tavern_choice = input("\nWhat would you like to do? ").lower().strip()

        if tavern_choice == '1':
            clear_console()
            converse_with_guard_captain(player)
        elif tavern_choice == '2':
            clear_console()
            listen_to_crowd(player)
        elif tavern_choice == '3':
            clear_console()
            speak_with_eldrin(player)
        elif tavern_choice == '4' or 'q':
            clear_console()
            print("You leave the tavern and head back to the town center.")
            break  # Breaks out of the loop to return to the town menu
        else:
            print("\nInvalid choice. Please enter a valid option.")
        input("\nPress Enter to continue...")


import random

def listen_to_crowd(player):
    clear_console()

    # Your updated list of random dialogues/tips
    tavern_chatter = [
        '"I heard they found a vast deposit of ore in the Damp Caves... shame about the monsters though."',
        '"The Adventurers Guild are hiring... if you got 100 gold spare and don\'t mind life on the border."',
        '"Heard bandits are roaming the outer edges of the border crossing."',
        '"A traveling merchant told me about a rare herb that grows only on the cliffs of Eretia. It\'s said to have miraculous healing properties."',
        '"There\'s an alchemist in town looking for rare ingredients. I hear they pay handsomely for the right stuff."',
        '"I\'ve heard whispers of a secret society that meets under the cover of darkness. They\'re said to possess ancient knowledge and forbidden magic."',
        '"Some adventurers spoke of a cavern filled with crystals that emit a haunting melody. It\'s supposedly hidden somewhere in the Damp Caves."',
        '"A group of miners went missing in the northern hills. People say they stumbled upon something... unnatural."',
        '"There\'s a rogue, \'Crook\' they called him I think, hunts the beasts in the Dark Forest for sport..."'
        
    ]

    print("You listen in to the chatter around the tavern...\n")
    random.shuffle(tavern_chatter)  

    for dialogue in tavern_chatter:
        print(f"Overheard: {dialogue}\n")
        choice = input("Do you want to continue listening? (Y/N): ").lower().strip()
        if choice != "y":
            break  
        clear_console()  

    print("You decide to stop eavesdropping and focus on your next move.\n")


    
    

def leave_town(player):
    while True:
        clear_console()
        print("Where would you like to go?\n")
        print("1. Dark Forest")
        print("2. Damp Cave")
        print("3. Northern Hills")
        print("4. The Border")
        print("5. Border Town")
        print("6. View Sign Post")
        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            enter_dark_forest(player)
            break
        elif choice == "2":
            from locations.dampcave import enter_damp_cave
            enter_damp_cave(player)
            break
        elif choice == "3":
            enter_northern_hills(player)
            break
        elif choice == "4":
            from locations.theborder import enter_the_border
            enter_the_border(player)
            break
        elif choice == "5" or choice == 'q':
            print("\nYou return to Border Town.")
            return_to_border_town(player)
            player.current_location = 'border_town'
        elif choice == "6":
            clear_console()
            print("The old, weather-beaten sign post creaks as you approach. The faded lettering reads:\n")
            print("   'Traveler, beware! Beyond lies the Dark Forest, home to creatures most foul.")
            print("    The Border is near, where the unknown meets the known.")
            print("    Heed this warning: only the brave or foolish tread these paths. Prepare well!'\n")
            input("Press enter to continue...")

        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")







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
    clear_console()
    print("As you enter the town, the Guard Captain approaches you with a stern look.")
    input("\nPress Enter to continue...")
    clear_console()

    print(Fore.YELLOW + "Guard Captain: " + Style.RESET_ALL + f"'Ah, {player.name}, the one who seeks glory in battle! Before you head into the fray, take this Health Potion. You'll need it if you're to survive the dangers that lie ahead.'\n")
    health_potion = HealthPotion()
    player.inventory.add_item(health_potion)
    # from items import Armour
    # iron_armour = Armour("Iron Armour", "+7 Defence Buff", 7)
    # player.inventory.add_equipment(iron_armour)
    input("\nPress Enter to continue...")
    clear_console()
    
    print(Fore.YELLOW + "Guard Captain: " + Style.RESET_ALL +  f"'And take this Rusted Sword as well. It's not much, but it's better than nothing.'" + Style.RESET_ALL)
    rusted_sword = Weapon("Rusted Sword", "A sword corroded by time, with a dulled edge.", 0.5, 0.5)
    player.inventory.add_equipment(rusted_sword)  # Adding the weapon to the equipment list
    print(Style.BRIGHT + Fore.BLUE + f"\n{player.name} received a Rusted Sword." + Style.RESET_ALL)
    input("\nEnter your inventory to equip weapons and armour. Press Enter to continue...")

    clear_console()





    






