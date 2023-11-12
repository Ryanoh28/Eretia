from items import Potion, Item
from utilities import clear_console
from locations import enter_dark_forest
from classes import Weapon
from missions import speak_with_eldrin

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
    

def return_to_camp(player, shop):
    while True:
        clear_console()
        print("You are at the camp. What would you like to do?\n")
        print("(T)rain, (L)eave, Ta(V)ern, (R)est, (I)nventory, (S)hop, (Q)uests, (M)enu")
        choice = input("\nEnter your choice: ").lower().strip()

        if choice == "t":
            player.training()
        elif choice == "l":
            leave_camp(player, shop)
        elif choice == "v":
            visit_tavern(player)
        elif choice == "r":
            player.regain_health(100)
            player.reset_search_count()
            print(f"\nYou rested at camp. \nCurrent health: {player.health}\n")
        elif choice == "i":
            player.inventory.inventory_menu(player)
        elif choice == "s":
            shop.shop_menu(player)
        elif choice == "q":
            view_quest_log(player)
        elif choice == "m":
            from game1 import main_menu
            main_menu(player, shop)
        else:
            print("\nInvalid choice. Please enter a valid command.\n")

        input("\nPress Enter to continue...") 

def visit_tavern(player):
    while True:
        clear_console()
        print("You enter the bustling tavern filled with adventurers and townsfolk.\n")
        print("1. Talk to the Camp Captain")
        print("2. Listen to rumors")
        print("3. Speak with Eldrin the Greenwarden")
        print("4. Leave the tavern")
        tavern_choice = input("\nWhat would you like to do? ").lower().strip()

        if tavern_choice == '1':
            converse_with_camp_captain(player)
        elif tavern_choice == '2':
            listen_to_rumors(player)
        elif tavern_choice == '3':
            speak_with_eldrin(player)
        elif tavern_choice == '4':
            clear_console()
            print("You leave the tavern and head back to the camp center.")
            break  # Breaks out of the loop to return to the camp menu
        else:
            print("\nInvalid choice. Please enter a valid option.")
        input("\nPress Enter to continue...")


def listen_to_rumors(player):
    clear_console()
    # Placeholder for future rumor listening functionality
    print("#Not implemented yet, low priority#")
    print("You overhear various adventurers sharing stories and rumors about the lands beyond the camp. Apparently one named 'Crook' has been seen walking around with an extra sword in his pants...")
    

def leave_camp(player, shop):
    while True:
        clear_console()
        print("Where would you like to go?\n")
        choice = input("(D)ark Forest or (B)ack to camp: ").lower().strip()

        if choice == "d":
            enter_dark_forest(player, shop)
            break
        elif choice == "b":
            print("\nYou decide to stay in the camp for now.")
            break
        else:
            print("\nInvalid choice. Please enter 'D' to go to the Dark Forest or 'B' to go back to camp.")

def converse_with_camp_captain(player):
    clear_console()
    print("Camp Captain: 'Greetings, warrior. What brings you to me today?'\n")
    print("1. Ask for advice")
    print("2. Talk with the Captain")
    print("3. Leave the conversation")

    choice = input("\nWhat would you like to do? ").lower().strip()

    if choice == '1':
        clear_console()
        print(f"Camp Captain: \"Remember, use your strengths wisely and learn from each battle. Every challenge is an opportunity to grow stronger.\"")
    elif choice == '2':
        clear_console()
        # dialogue based on Eldrin's quest status
        if "mystic_herb_quest" in player.quests:
            if player.quests["mystic_herb_quest"]["completed"]:
                print(f"Camp Captain: 'I've heard about your success with Eldrin's task. Impressive work, {player.name}. The Blade of Verdant Greens is a fine reward for such dedication.'")
            elif player.quests["mystic_herb_quest"]["accepted"]:
                print(f"Camp Captain: 'Heard you're running around for that old man Eldrin. Be careful in the Dark Forest, {player.name}. It's a dangerous place.'")
            else:
                print(f"Camp Captain: 'Eldrin the Greenwarden often has tasks for willing adventurers. Have you spoken with him in the tavern, {player.name}?'")
        else:
            print(f"Camp Captain: \"There are whispers of strange happenings in the forest. Stay alert and trust your instincts.\"")
    elif choice == '3':
        clear_console()
        print(f"Camp Captain: \"Very well, {player.name}. Stay safe out there.\"")
    else:
        clear_console()
        print("Camp Captain: \"I'm not sure what you mean. Could you please clarify?\"")


    
    

def meet_camp_captain(player):
    clear_console()
    print("As you enter the camp, the captain approaches you with a stern look.")
    input("\nPress Enter to continue...")
    clear_console()

    print(f"Camp Captain: 'Ah, {player.name}, the one who seeks glory in battle! Before you head into the fray, take this Health Potion. You'll need it if you're to survive the dangers that lie ahead.'\n")
    health_potion = Potion("Health Potion", "A potion that restores 50 health.", 50)
    player.inventory.add_item(health_potion)
    input("\nPress Enter to continue...")
    clear_console()
    
    print(f"Camp Captain: 'And take this Rusted Sword as well. It's not much, but it's better than nothing.'")
    rusted_sword = Weapon("Rusted Sword", 0.5, 0.5)
    player.available_weapons.append(rusted_sword)
    print(f"\n{player.name} received a Rusted Sword.")  # Add this line to confirm the receipt
    input("\nPress Enter to continue...")


    clear_console()






