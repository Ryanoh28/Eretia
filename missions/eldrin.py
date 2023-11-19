from utilities import clear_console
from items import Weapon, LOOT_ITEMS, Item
import time
from colorama import Style, Fore

# def speak_with_eldrin(player):
#     # Handle Mystic Herb Quest
#     if "mystic_herb_quest" in player.quests:
#         mystic_herb_quest = player.quests["mystic_herb_quest"]
#         if mystic_herb_quest["completed"]:
#             if not mystic_herb_quest.get("reward_given"):
#                 clear_console()  
#                 give_mystic_herb_quest_reward(player)
#             else:
                
#                 if "monster_loot_quest" not in player.quests or not player.quests["monster_loot_quest"]["completed"]:
#                     offer_monster_loot_quest(player)
#                 else:
#                     check_back_later_message()
#             return
#         elif player.inventory.count_item("Mystic Herb") >= 8:
#             clear_console()
#             complete_mystic_herb_quest(player)
#             return
#         else:
#             print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + f" '{player.name}, I need 8 Mystic Herbs. You can find them in the Dark Forest.'")
#             time.sleep(3)  # Pause for 3 seconds 
#             clear_console()
#             return

    
#     if "mystic_herb_quest" not in player.quests:
#         offer_mystic_herb_quest(player)
#         return

    
#     if "monster_loot_quest" in player.quests:
#         handle_monster_loot_quest(player)
#     else:
#         check_back_later_message()

def speak_with_eldrin(player):
    
    # Handle Mystic Herb Quest
    if "mystic_herb_quest" in player.quests:
        mystic_herb_quest = player.quests["mystic_herb_quest"]
        if mystic_herb_quest["completed"]:
            if not mystic_herb_quest.get("reward_given"):
                clear_console()  
                give_mystic_herb_quest_reward(player)
            else:
                # Check if there are any other quests to be offered or completed
                if "monster_loot_quest" not in player.quests or not player.quests["monster_loot_quest"]["completed"]:
                    offer_monster_loot_quest(player)
                elif "potion_delivery_quest" not in player.quests:
                    if player.level >= 5:
                        offer_potion_delivery_quest(player)
                    else:
                        print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + f" 'You're doing well, {player.name}. I might have another important task for you once you reach level 5.'")
                elif not player.quests["potion_delivery_quest"]["completed"]:
                    handle_potion_delivery_quest(player)
                else:
                    check_back_later_message()
            return
        elif player.inventory.count_item("Mystic Herb") >= 8:
            clear_console()
            complete_mystic_herb_quest(player)
            return
        else:
            print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + f" '{player.name}, I need 8 Mystic Herbs. You can find them in the Dark Forest.'")
            time.sleep(3)  
            clear_console()
            return

    if "mystic_herb_quest" not in player.quests:
        offer_mystic_herb_quest(player)
        return

    # Handle Monster Loot Quest
    if "monster_loot_quest" in player.quests and not player.quests["monster_loot_quest"]["completed"]:
        handle_monster_loot_quest(player)
    elif "potion_delivery_quest" in player.quests and not player.quests["potion_delivery_quest"]["completed"]:
        handle_potion_delivery_quest(player)
    elif player.level < 5:
        print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + f" 'You're doing well, {player.name}. I might have another important task for you once you reach level 5.'")
    else:
        check_back_later_message()





def offer_potion_delivery_quest(player):
    clear_console()
    print(Fore.GREEN + "Eldrin the Greenwarden" + Style.RESET_ALL + " greets you warmly.\n")
    print(f"'Greetings, {player.name}. The soldiers at the Sentinel Garrison are in dire need of health potions. Can you deliver this batch to the Garrison Commander? I trust you with this task.'\n")
    print("1. Accept the quest")
    print("2. Decline the quest")
    accept_decline_potion_delivery_quest(player)

def handle_potion_delivery_quest(player):
    if "potion_delivery_quest" in player.quests and player.quests["potion_delivery_quest"]["completed"]:
        if not player.quests["potion_delivery_quest"].get("reward_given"):
            # Reward the player
            reward_amount = 80  # Amount of gold to reward the player
            player.gold += reward_amount  # Add the reward to the player's gold
            player.quests["potion_delivery_quest"]["reward_given"] = True

            clear_console()
            print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + f" 'Thank you for delivering the parcel to the Garrison Commander. Here is your reward of {reward_amount} gold as promised.'")
            input("\nPress Enter to continue...")
            clear_console()
        else:
            # If the reward has already been given, display a standard message
            print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + " 'Thank you for your help, brave adventurer. I have no more tasks for you at the moment.'")
            input("\nPress Enter to continue...")
            clear_console()
    else:
        # If the quest has not been completed or does not exist
        print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + " 'How goes the task I have given you?'")
        # input("\nPress Enter to continue...")
        # clear_console()


def accept_decline_potion_delivery_quest(player):
    choice = input("\nWhat will you do? ").lower().strip()
    clear_console()
    if choice == '1':
        player.quests["potion_delivery_quest"] = {"accepted": True, "completed": False}
        parcel = Item("Parcel", "A sealed parcel containing health potions for the Sentinel Garrison.")
        player.inventory.add_item(parcel)

        print("You've accepted Eldrin's quest to deliver health potions to the Sentinel Garrison.\n")
        print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + f" 'Thank you, {player.name}. Your help is invaluable. The Sentinel Garrison is relying on these potions. Deliver them with haste.'")
    elif choice == '2':
        print("\nYou've decided not to accept the quest right now.")
        print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + f" 'I see. Should you change your mind, you know where to find me.'")  
       

def give_mystic_herb_quest_reward(player):
    verdant_blade = Weapon("Blade of Verdant Greens", "A weapon crafted by Eldrin the Greenwarden, shimmering with a verdant glow.", 1, 2)
    player.available_weapons.append(verdant_blade)
    player.quests["mystic_herb_quest"]["reward_given"] = True
    clear_console()
    print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + f" 'Amazing work! Here is your Blade of Verdant Greens, as promised.'")
    input("\nPress Enter to continue...")
    clear_console()

def complete_mystic_herb_quest(player):
    if player.inventory.count_item("Mystic Herb") >= 8:
        player.inventory.remove_items("Mystic Herb", 8)
        player.quests["mystic_herb_quest"]["completed"] = True
        verdant_blade = Weapon("Blade of Verdant Greens", "A weapon crafted by Eldrin the Greenwarden, shimmering with a verdant glow.", 1, 2)
        player.available_weapons.append(verdant_blade)
        print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + f" 'Amazing work, {player.name}! Here is your Blade of Verdant Greens, as promised.\n'")
        print("You received 'The Blade of Verdant Greens' from Eldrin. ")
        player.quests["mystic_herb_quest"]["reward_given"] = True
    else:
        print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + f" '{player.name}, don't forget, I need 8 Mystic Herbs. You can find them in the Dark Forest.'")


def offer_monster_loot_quest(player):
    clear_console()
    if "monster_loot_quest" in player.quests:
        if player.quests["monster_loot_quest"]["completed"]:
            if not player.quests["monster_loot_quest"].get("reward_given"):
                print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + f" 'Thank you for bringing me the item from the forest. Here's your reward, as promised.'")
                player.quests["monster_loot_quest"]["reward_given"] = True
                input("\nPress Enter to continue...")
                clear_console()
            else:
                print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + f" 'I might have more tasks for you soon. Be sure to check back.'")
                input("\nYou turn around...")
                clear_console()
            return
        elif player.quests["monster_loot_quest"]["accepted"]:
            handle_monster_loot_quest(player)
            return

    # Offer the Monster Loot quest if not started
    print("Eldrin the Greenwarden greets you warmly.\n")
    print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + f"'Greetings again, {player.name}. I need an item that can only be found by defeating the creatures of the Dark Forest. Bring me any loot item from these monsters, and I'll pay you more than its value.'\n")
    print("1. Accept the quest")
    print("2. Decline the quest")
    accept_decline_monster_loot_quest(player)



def offer_mystic_herb_quest(player):
    clear_console()
    print(Fore.GREEN + "Eldrin the Greenwarden" + Style.RESET_ALL + " greets you warmly.\n")
    print(f"'Ah, {player.name}, I'm in dire need of Mystic Herbs to prepare vital medicines. Can you bring me 8 of them? In return, I'll forge for you the Blade of Verdant Greens.'\n")
    print("1. Accept the quest")
    print("2. Decline the quest")
    accept_decline_mystic_herb_quest(player)



def handle_monster_loot_quest(player):
    loot_found = False
    for loot_item in LOOT_ITEMS.keys():
        if player.inventory.count_item(loot_item) > 0:
            loot_found = True
            player.inventory.remove_items(loot_item, 1)
            reward = 50
            player.gold += reward
            player.quests["monster_loot_quest"]["completed"] = True
            print("You walked up to Eldrin after completing the mission...\n")
            print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + f" 'This is exactly what I was looking for! Here is your reward of {reward} gold for your troubles.'")
            #input("\nPress Enter to continue...")
            #clear_console()
            return  
    if not loot_found:
        print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + f" 'It seems you haven't found what I'm looking for yet. Keep searching in the forest.'")
        input("\nPress Enter to continue...")
        clear_console()
        return  






# ... rest of your code ...

def check_back_later_message():
    clear_console()
    print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + f" 'Thank you for your help, brave adventurer. I have no more tasks for you at the moment. Check back later, and I might have new challenges for you.'")
    # No need for an additional input if it's just to continue without decision-making or significant acknowledgment.


def accept_decline_monster_loot_quest(player):
    choice = input("\nWhat will you do? ").lower().strip()
    clear_console()
    if choice == '1':
        player.quests["monster_loot_quest"] = {"accepted": True, "completed": False}
        print("You've accepted Eldrin's quest to gather an item from the forest creatures.\n")
        
        print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + f"'Thank you, {player.name}. Your courage is commendable. The forest creatures hold many secrets. Be cautious and return safely.'")
    elif choice == '2':
        print("\nYou've decided not to accept the quest right now.")
        print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + f" 'I see. Should you change your mind, you know where to find me.'")

def accept_decline_mystic_herb_quest(player):
    choice = input("\nWhat will you do? ").lower().strip()
    clear_console()
    if choice == '1':
        player.quests["mystic_herb_quest"] = {"accepted": True, "completed": False}
        print("You've accepted Eldrin's quest to gather Mystic Herbs.\n")
        print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + f" 'Thank you, {player.name}. Your help is invaluable. The herbs are often found in the depths of the Dark Forest. Be cautious and return safely.'")
    elif choice == '2':
        print("\nYou've decided not to accept the quest right now.")
        print(Fore.GREEN + "Eldrin:" + Style.RESET_ALL + f" 'I see. Should you change your mind, you know where to find me.'")