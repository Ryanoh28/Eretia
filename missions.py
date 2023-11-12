from utilities import clear_console

def speak_with_eldrin(player):
    clear_console()

    # Check if the player has already accepted the quest and it's not completed
    if "mystic_herb_quest" in player.quests and not player.quests["mystic_herb_quest"]["completed"]:
        print(f"Eldrin reminds you, 'Don't forget, {player.name}, I need 8 Mystic Herbs. You can find them in the Dark Forest.'")
        return 

    clear_console()
    print(f"Eldrin the Greenwarden greets you warmly.\n")
    print(f"'Ah, {player.name}, I'm in dire need of Mystic Herbs to prepare vital medicines. Can you bring me 8 of them? In return, I'll forge for you the Blade of Verdant Greens.'\n")
    print("(A)ccept the quest")
    print("(D)ecline the quest")

    choice = input("\nWhat will you do? ").lower().strip()

    clear_console()
    if choice == 'a':
        # Accepting the quest
        if choice == 'a':
            player.quests["mystic_herb_quest"] = {"accepted": True, "completed": False}
            print("\nYou've accepted Eldrin's quest to gather Mystic Herbs.")
            print(f"\nEldrin smiles, 'Thank you, {player.name}. Your help is invaluable. The herbs are often found in the depths of the Dark Forest. Be cautious and return safely.'")
    elif choice == 'd':
        # Declining the quest
        print("\nYou've decided not to accept the quest right now.")
        print("\nEldrin nods understandingly, 'I see. Should you change your mind, you know where to find me. The forest and its secrets await your courage.'")
    else:
        print("\nInvalid choice. Please decide whether to accept or decline the quest.")
