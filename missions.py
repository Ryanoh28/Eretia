from utilities import clear_console
from items import Weapon, LOOT_ITEMS

def speak_with_eldrin(player):
    clear_console()

    # Check if the Mystic Herb quest has been completed
    if "mystic_herb_quest" in player.quests:
        if player.quests["mystic_herb_quest"]["completed"]:
            print("Eldrin: 'Thank you again for your help. The Blade of Verdant Greens serves you well.'")
            offer_forest_loot_quest(player)
            return
        elif player.inventory.count_item("Mystic Herb") >= 8:
            complete_mystic_herb_quest(player)
            return
        else:
            print(f"Eldrin reminds you, 'Don't forget, {player.name}, I need 8 Mystic Herbs. You can find them in the Dark Forest.'")
            return
    else:
        # Offer the Mystic Herb quest if not started
        offer_mystic_herb_quest(player)

def offer_forest_loot_quest(player):
    clear_console()
    
    if "monster_loot_quest" in player.quests:
        if player.quests["monster_loot_quest"]["completed"]:
            print("Eldrin: 'Thank you for bringing me the item from the forest. Here's your reward, as promised.'")
            return
        elif player.quests["monster_loot_quest"]["accepted"]:
            handle_forest_loot_quest(player)
            return
    
    # Offer the Forest Loot quest
    print(f"Eldrin the Greenwarden greets you warmly.\n")
    print(f"'Greetings again, {player.name}. I need an item that can only be found by defeating the creatures of the Dark Forest. Bring me any loot item from these monsters, and I'll pay you double its value.'\n")
    print("(A)ccept the quest")
    print("(D)ecline the quest")

    accept_decline_forest_loot_quest(player)

def offer_mystic_herb_quest(player):
    clear_console()
    print(f"Eldrin the Greenwarden greets you warmly.\n")
    print(f"'Ah, {player.name}, I'm in dire need of Mystic Herbs to prepare vital medicines. Can you bring me 8 of them? In return, I'll forge for you the Blade of Verdant Greens.'\n")
    print("(A)ccept the quest")
    print("(D)ecline the quest")
    accept_decline_mystic_herb_quest(player)

def complete_mystic_herb_quest(player):
    clear_console()
    player.inventory.remove_items("Mystic Herb", 8)
    player.quests["mystic_herb_quest"]["completed"] = True
    verdant_blade = Weapon("Blade of Verdant Greens", 1, 2)
    player.available_weapons.append(verdant_blade)
    print(f"Eldrin: 'Amazing work, {player.name}! Here is your Blade of Verdant Greens, as promised.'")

def handle_forest_loot_quest(player):
    clear_console()
    loot_found = False
    for loot_item in LOOT_ITEMS.keys():
        if player.inventory.count_item(loot_item) > 0:
            loot_found = True
            player.inventory.remove_item(loot_item, 1)
            reward = 30
            player.gold += reward
            player.quests["monster_loot_quest"]["completed"] = True
            print(f"Eldrin: 'This is exactly what I was looking for! Here is your reward of {reward} gold for your troubles.'")
            break

    if not loot_found:
        print("Eldrin: 'It seems you haven't found what I'm looking for yet. Keep searching in the forest.'")

def accept_decline_forest_loot_quest(player):
    clear_console()
    choice = input("\nWhat will you do? ").lower().strip()

    if choice == 'a':
        player.quests["monster_loot_quest"] = {"accepted": True, "completed": False}
        print("You've accepted Eldrin's quest to gather an item from the forest creatures.")
        print(f"\nEldrin smiles, 'Thank you, {player.name}. Your courage is commendable. The forest creatures hold many secrets. Be cautious and return safely.'")
    elif choice == 'd':
        print("\nYou've decided not to accept the quest right now.")
        print("\nEldrin nods understandingly, 'I see. Should you change your mind, you know where to find me.'")
    else:
        print("\nInvalid choice. Please decide whether to accept or decline the quest.")

def accept_decline_mystic_herb_quest(player):
    clear_console()
    choice = input("\nWhat will you do? ").lower().strip()

    if choice == 'a':
        player.quests["mystic_herb_quest"] = {"accepted": True, "completed": False}
        print("You've accepted Eldrin's quest to gather Mystic Herbs.")
        print(f"\nEldrin smiles, 'Thank you, {player.name}. Your help is invaluable. The herbs are often found in the depths of the Dark Forest. Be cautious and return safely.'")
    elif choice == 'd':
        print("\nYou've decided not to accept the quest right now.")
        print("\nEldrin nods understandingly, 'I see. Should you change your mind, you know where to find me.'")
    else:
        print("\nInvalid choice. Please decide whether to accept or decline the quest.")


