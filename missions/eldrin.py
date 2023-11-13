from utilities import clear_console
from items import Weapon, LOOT_ITEMS


def speak_with_eldrin(player):
    clear_console()

    # Check if Mystic Herb quest is completed
    if "mystic_herb_quest" in player.quests:
        if player.quests["mystic_herb_quest"]["completed"]:
            if not player.quests["mystic_herb_quest"].get("reward_given"):
                print("Eldrin: 'Amazing work! Here is your Blade of Verdant Greens, as promised.'")
                player.quests["mystic_herb_quest"]["reward_given"] = True
            else:
                print("Eldrin: 'The Blade of Verdant Greens serves you well.'")
            # Offer Monster Loot quest immediately after giving reward for Mystic Herb quest
            offer_monster_loot_quest(player)
            return
        elif player.inventory.count_item("Mystic Herb") >= 8:
            complete_mystic_herb_quest(player)
            # Offer Monster Loot quest immediately after completing Mystic Herb quest
            offer_monster_loot_quest(player)
            return
        else:
            print(f"Eldrin reminds you, 'Don't forget, {player.name}, I need 8 Mystic Herbs. You can find them in the Dark Forest.'")
            input("\nPress Enter to continue...")
            clear_console()
            return
    else:
        # Offer Mystic Herb quest if not started
        offer_mystic_herb_quest(player)

def offer_monster_loot_quest(player):
    clear_console()
    if "monster_loot_quest" in player.quests and player.quests["monster_loot_quest"]["completed"]:
        if not player.quests["monster_loot_quest"].get("reward_given"):
            print("Eldrin: 'Thank you for bringing me the item from the forest. Here's your reward, as promised.'")
            player.quests["monster_loot_quest"]["reward_given"] = True
        else:
            print("Eldrin: 'I might have more tasks for you soon. Be sure to check back.'")
        input("\nPress Enter to continue...")
        clear_console()
    else:
        print(f"Eldrin the Greenwarden greets you warmly.\n")
        print(f"'Greetings again, {player.name}. I need an item that can only be found by defeating the creatures of the Dark Forest. Bring me any loot item from these monsters, and I'll pay you more than its value.'\n")
        print("(A)ccept the quest")
        print("(D)ecline the quest")
        accept_decline_monster_loot_quest(player)



def offer_mystic_herb_quest(player):
    clear_console()
    print(f"Eldrin the Greenwarden greets you warmly.\n")
    print(f"'Ah, {player.name}, I'm in dire need of Mystic Herbs to prepare vital medicines. Can you bring me 8 of them? In return, I'll forge for you the Blade of Verdant Greens.'\n")
    print("(A)ccept the quest")
    print("(D)ecline the quest")
    accept_decline_mystic_herb_quest(player)

def complete_mystic_herb_quest(player):
    player.inventory.remove_items("Mystic Herb", 8)
    player.quests["mystic_herb_quest"]["completed"] = True
    verdant_blade = Weapon("Blade of Verdant Greens", 1, 2)
    player.available_weapons.append(verdant_blade)
    print(f"Eldrin: 'Amazing work, {player.name}! Here is your Blade of Verdant Greens, as promised.'")

def handle_monster_loot_quest(player):
    loot_found = False
    for loot_item in LOOT_ITEMS.keys():
        if player.inventory.count_item(loot_item) > 0:
            loot_found = True
            player.inventory.remove_items(loot_item, 1)
            reward = 50
            player.gold += reward
            player.quests["monster_loot_quest"]["completed"] = True
            print(f"Eldrin: 'This is exactly what I was looking for! Here is your reward of {reward} gold for your troubles.'")
            break
    if not loot_found:
        print("Eldrin: 'It seems you haven't found what I'm looking for yet. Keep searching in the forest.'")

def accept_decline_monster_loot_quest(player):
    choice = input("\nWhat will you do? ").lower().strip()
    clear_console()
    if choice == 'a':
        player.quests["monster_loot_quest"] = {"accepted": True, "completed": False}
        print("You've accepted Eldrin's quest to gather an item from the forest creatures.")
        print(f"\nEldrin smiles, 'Thank you, {player.name}. Your courage is commendable. The forest creatures hold many secrets. Be cautious and return safely.'")
    elif choice == 'd':
        print("\nYou've decided not to accept the quest right now.")
        print("\nEldrin nods understandingly, 'I see. Should you change your mind, you know where to find me.'")

def accept_decline_mystic_herb_quest(player):
    choice = input("\nWhat will you do? ").lower().strip()
    clear_console()
    if choice == 'a':
        player.quests["mystic_herb_quest"] = {"accepted": True, "completed": False}
        print("You've accepted Eldrin's quest to gather Mystic Herbs.")
        print(f"\nEldrin smiles, 'Thank you, {player.name}. Your help is invaluable. The herbs are often found in the depths of the Dark Forest. Be cautious and return safely.'")
    elif choice == 'd':
        print("\nYou've decided not to accept the quest right now.")
        print("\nEldrin nods understandingly, 'I see. Should you change your mind, you know where to find me.'")