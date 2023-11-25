from colorama import Fore, Style
from utilities import clear_console
import random
from datetime import datetime, timedelta
from items import Item


def meadowlands_menu(player):
    while True:
        clear_console()
        print("Welcome to the Meadowlands!")
        print("\nA peaceful area filled with lush greenery and vibrant flora.\n")
        print("1. Horticulture Activities")
        print("2. Talk to the Local Farmer")
        print("3. Return")

        choice = input("\nEnter your choice (1-4): ").strip()
        if choice == "1":
            horticulture_submenu(player)
        elif choice == "2":
            talk_to_farmer(player)
        elif choice == "3":
            from bordertown import leave_town_west
            leave_town_west(player)
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

def horticulture_submenu(player):
    while True:
        clear_console()
        print("=== Horticulture Activities ===\n")
        print("1. Plant Seeds")
        print("2. Check on Planted Crops")
        print("3. Harvest Mature Plants")
        print("4. Inventory")
        print("5. Return to Meadowlands Menu")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            plant_seeds(player)
        elif choice == "2":
            check_crops(player)
        elif choice == "3":
            harvest_plants(player)
        elif choice == "4":
            player.inventory.inventory_menu(player)
        elif choice == "5" or choice == 'Q':
            break  
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")




def plant_seeds(player):
    while True:
        clear_console()
        print("Available Seeds to Plant:")
        for i, plant in enumerate(plants_table, 1):
            print(f"\n{i}. {plant['seed_name']} (Required Level: {plant['req_level']})")

        choice = input("\nEnter your choice (number) or 'Q' to return: \n").strip()

        if choice.lower() == 'q':
            return
        elif choice.isdigit() and 1 <= int(choice) <= len(plants_table):
            clear_console()
            selected_seed = plants_table[int(choice) - 1]['seed_name']
            player.plant_seed(selected_seed)
            input("\nPress Enter to continue...")
        else:
            print("Invalid choice. Please enter a valid number.")




def check_crops(player):
    clear_console()
    player.check_crops()
    input("\nPress Enter to continue...")

def harvest_plants(player):
    while True:
        clear_console()
        if not player.garden:
            print("You have no plants ready for harvest.\n")
            input("Press enter to continue...")
            return
        else:
            print("Select a Plant to Harvest:")
            player.check_crops()
            choice = input("\nEnter the number of the plant to harvest, or 'Q' to return: \n").strip()

            if choice.lower() == 'q':
                return
            elif choice.isdigit():
                choice_number = int(choice)
                clear_console()
                if 0 <= choice_number - 1 < len(player.garden):
                    player.harvest_crops(choice_number)
                else:
                    print("\nInvalid choice. Please enter a valid number.")
            else:
                print("\nInvalid input. Please enter a number.")

        input("\nPress Enter to continue...")



def talk_to_farmer(player):
    clear_console()
    
    if "fish_pie_quest" in player.quests and not player.quests["fish_pie_quest"]["completed"]:
        complete_fish_pie_quest(player)
        return
    
    elif "fish_pie_quest" in player.quests and player.quests["fish_pie_quest"]["completed"]:
        visit_seed_shop(player)
        return

    print(Fore.YELLOW + "Farmer:" + Style.RESET_ALL + " \"Hello there! Are you new to farming and horticulture?\" he asks.\n")
    response = input("Are you new to farming and horticulture? (Y/N): ").strip().lower()

    if response == "y":
        offer_fish_pie_quest(player)
    elif response == "n":
        visit_seed_shop(player)
    else:
        print("\nThe farmer didn't understand your response and continues with his work.")
        input("\nPress Enter to continue...")

def complete_fish_pie_quest(player):
    fish_needed = 3
    fish_types = ["Small Fish", "Medium Fish", "Large Fish", "Rare Fish"]
    total_fish_count = sum(player.inventory.count_item(fish) for fish in fish_types)

    if player.quests.get("fish_pie_quest", {}).get("accepted") and not player.quests["fish_pie_quest"]["completed"]:
        if total_fish_count >= fish_needed:
            for fish in fish_types:
                while fish_needed > 0 and player.inventory.count_item(fish) > 0:
                    player.inventory.remove_items(fish, 1)
                    fish_needed -= 1

            player.quests["fish_pie_quest"]["completed"] = True

            simple_herb_seed = Item("Simple Herb Seed", "A seed of a simple herb")
            
            print(Fore.YELLOW + "Farmer:" + Style.RESET_ALL + " \"Thank you for the fish! Here are some Simple Herb Seeds to start your journey.\"\n")
            player.inventory.add_item(simple_herb_seed, quantity=3)
        else:
            print(Fore.YELLOW + "Farmer:" + Style.RESET_ALL + " \"You still need more fish for the pie. Keep fishing!\"\n")
    else:
        print("You have not accepted or have already completed this quest.")
    input("\nPress Enter to continue...")


def offer_fish_pie_quest(player):
    clear_console()
    print(Fore.YELLOW + "Farmer:" + Style.RESET_ALL + " \"That's wonderful! I could use some help. I'm making a fish pie for my wife and need 3 fish. Can you bring them to me? I'll give you some seeds to start your journey!\"\n")
    print("1. Accept the quest")
    print("2. Decline the quest")

    choice = input("\nWhat will you do? ").lower().strip()
    clear_console()
    if choice == '1':
        player.quests["fish_pie_quest"] = {"accepted": True, "completed": False, "reward_given": False, "fish_collected": 0}
        print(Fore.YELLOW + "Farmer:" + Style.RESET_ALL + " \"Thank you! I'm counting on you for those fish.\"\n")
        print("You've accepted the Fish Pie Quest.")
    elif choice == '2':
        print(Fore.YELLOW + "Farmer:" + Style.RESET_ALL + " \"I see. Should you change your mind, I'll be here waiting.\"")
    else:
        print("Invalid choice. Please try again.")
        offer_fish_pie_quest(player)
    input("\nPress Enter to continue...")


def visit_seed_shop(player):
    from classes import Shop
    clear_console()
    print("Welcome! Do you want to buy any Simple Herb Seeds or Moonflower Seeds?")

    seed_shop_items = {
        'Simple Herb Seed': {'price': 3, 'object': Item("Simple Herb Seed", "A basic herb seed")},
        'Moonflower Seed': {'price': 10, 'object': Item("Moonflower Seed", "A beautiful and rare flower seed")}
    }

    seed_shop = Shop()
    seed_shop.items_for_sale = seed_shop_items  

    seed_shop.display_items_for_sale(player)
    input("\nPress Enter to continue...")

def gain_horticulture_experience(player, xp_gained):
    player.horticulture_experience += xp_gained
    print(f"\n{player.name} gained {xp_gained} horticulture experience points.")

    while player.horticulture_experience >= 100 + (10 * (player.horticulture_level - 1)):
        player.horticulture_experience -= 100 + (10 * (player.horticulture_level - 1))
        
        player.horticulture_level += 1
        print(Fore.YELLOW + f"\nCongratulations! Your horticulture level is now {player.horticulture_level}." + Style.RESET_ALL)






plants_table = [
    {"seed_name": "Simple Herb Seed", "plant_name": "Simple Herb", "req_level": 1, "growth_time": 10, "planting_xp": 1, "harvesting_xp": 3, "yield_range": (1, 2)},
    {"seed_name": "Moonflower Seed", "plant_name": "Moonflower", "req_level": 5, "growth_time": 15, "planting_xp": 3, "harvesting_xp": 5, "yield_range": (1, 2)},
    {"seed_name": "Starleaf Seed", "plant_name": "Starleaf", "req_level": 10, "growth_time": 20, "planting_xp": 3, "harvesting_xp": 6, "yield_range": (1, 2)},
    {"seed_name": "Sunblossom Seed", "plant_name": "Sunblossom", "req_level": 15, "growth_time": 25, "planting_xp": 4, "harvesting_xp": 7, "yield_range": (1, 2)},
    {"seed_name": "Eldertree Sapling Seed", "plant_name": "Eldertree Sapling", "req_level": 20, "growth_time": 60, "planting_xp": 10, "harvesting_xp": 10, "yield_range": (1, 1)}
]



