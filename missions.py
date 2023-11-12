from utilities import clear_console
from items import Weapon

def speak_with_eldrin(player):
    clear_console()

    # Check if the quest has been completed
    if "mystic_herb_quest" in player.quests:
        if player.quests["mystic_herb_quest"]["completed"]:
            print("Eldrin: 'Thank you again for your help. The Blade of Verdant Greens serves you well.'")
            return
        elif player.inventory.count_item("Mystic Herb") >= 8:
            # Player completes the quest
            player.inventory.remove_items("Mystic Herb", 8)
            player.quests["mystic_herb_quest"]["completed"] = True
            verdant_blade = Weapon("Blade of Verdant Greens", 1, 2)
            player.available_weapons.append(verdant_blade)
            print(f"Eldrin: 'Amazing work, {player.name}! Here is your Blade of Verdant Greens, as promised.'")
            return
    
    # Check if the quest is in progress but not completed
    if "mystic_herb_quest" in player.quests and not player.quests["mystic_herb_quest"]["completed"]:
        print(f"Eldrin reminds you, 'Don't forget, {player.name}, I need 8 Mystic Herbs. You can find them in the Dark Forest.'")
        return 

    # Initial interaction with Eldrin
    print(f"Eldrin the Greenwarden greets you warmly.\n")
    print(f"'Ah, {player.name}, I'm in dire need of Mystic Herbs to prepare vital medicines. Can you bring me 8 of them? In return, I'll forge for you the Blade of Verdant Greens.'\n")
    print("(A)ccept the quest")
    print("(D)ecline the quest")

    choice = input("\nWhat will you do? ").lower().strip()

    clear_console()
    if choice == 'a':
        player.quests["mystic_herb_quest"] = {"accepted": True, "completed": False}
        print("You've accepted Eldrin's quest to gather Mystic Herbs.")
        print(f"\nEldrin smiles, 'Thank you, {player.name}. Your help is invaluable. The herbs are often found in the depths of the Dark Forest. Be cautious and return safely.'")
    elif choice == 'd':
        print("\nYou've decided not to accept the quest right now.")
        print("\nEldrin nods understandingly, 'I see. Should you change your mind, you know where to find me. The forest and its secrets await your courage.'")
    else:
        print("\nInvalid choice. Please decide whether to accept or decline the quest.")

