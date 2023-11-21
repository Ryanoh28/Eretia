from combat import combat, create_monster, fight_monster
from items import Armour
from utilities import clear_console
from colorama import Fore, Style
from locations.locationfunctions import rest_in_location

def enter_northern_hills(player):
    player.current_location = 'northern_hills'
    clear_console()
    print("You head towards the Northern Hills...\n")

    if player.first_time_northern_hills:
        print("As you ascend the hills, you see an old man being attacked by a monster!\n")
        monster = create_monster("Northern Hills")  
        combat_result = combat(player, monster)

        if combat_result == "monster_defeated":
            player.first_time_northern_hills = False  
            print("You have defeated the monster!")
            lead_player_to_smithy(player)
        else:
            print("You decide to retreat for now.")
    else:
        show_northern_hills_menu(player)

def lead_player_to_smithy(player):
    clear_console()
    print("Grateful for your help, the old man leads you up the hill to his smithy.\n")
    print(Fore.YELLOW + "Old Man:" + Style.RESET_ALL + " 'I have a task for you.. if you're interested, come speak with me.'")
    
    input("\nPress enter to continue...")
    visit_blacksmith(player)

def show_northern_hills_menu(player):
    clear_console()
    while True:
        player.current_location = 'northern_hills'
        clear_console()
        print("What would you like to do?\n")
        print("1. Visit Smithy")
        print("2. Hunt on the Hills")
        print("3. Inventory")
        print("4. Rest ")
        print("5. View Quests")
        print("6. Return")

        choice = input("\nEnter your choice (1-4): ").strip()
        clear_console()

        if choice == "1":
            visit_blacksmith(player)
        elif choice == "3":
            player.inventory.inventory_menu(player)
        elif choice == "2":
            clear_console()
            fight_monster(player, "Northern Hills")  
        elif choice == "4":
            clear_console()
            rest_in_location(player)  
        elif choice == "5":
            clear_console()
            from bordertown import view_quest_log
            view_quest_log(player)  
        elif choice == "6" or choice == 'q':
            player.current_location = 'border_town'
            from bordertown import leave_town
            leave_town(player)  
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def visit_blacksmith(player):
    while True:
        clear_console()
        print("Northern Hills Blacksmith\n")
        print("What would you like to do?\n")
        print("1. Speak with the Old Blacksmith")
        print("2. View armours for sale")
        print("3. Leave Smithy")


        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            if "blacksmith_quest" in player.quests:
                blacksmith_quest = player.quests["blacksmith_quest"]
                if blacksmith_quest.get("reward_given", False):
                    clear_console()
                    print("Old Man: 'I'm a bit busy now, come back later.'")
                elif blacksmith_quest["completed"]:
                    clear_console()
                    print("Old Man: 'Thank you for bringing the ores. Here is your bronze armour.'")
                    blacksmith_quest["reward_given"] = True
                elif blacksmith_quest["accepted"]:
                    clear_console()
                    if check_ores_in_inventory(player, 5, 5):
                        complete_blacksmith_quest(player)
                    else:
                        print("Old Man: 'Have you brought the ores I asked for?'")
                else:
                    clear_console()
                    offer_blacksmith_quest(player)
            else:
                clear_console()
                offer_blacksmith_quest(player)
            input("\nPress enter to continue...")
        elif choice == "2":
            armour_menu(player)  # Call the armour menu function
        elif choice == "3" or choice == 'q':
            clear_console()
            print("You leave the smithy.")
            break
        else:
            clear_console()
            print("Invalid choice. Please enter a valid number.")
            input("\nPress enter to continue...")

def armour_menu(player):
    while True:
        clear_console()
        print("Armours available for purchase:\n")
        print("1. Bronze Armour: +3 Defence Buff")
        print("   Price: 5 Copper Ore, 5 Tin Ore, 50 Gold")
        print("\n2. Iron Armour: +7 Defence Buff")
        print("   Price: 10 Iron Ore, 200 Gold")
        print("\n3. Steel Armour: +15 Defence Buff")
        print("   Price: 25 Iron Ore, 10 Coal, 600 Gold")
        print("\n4. Back")

        choice = input("\nChoose an armour to purchase or go back: ").strip()

        if choice == '1':
            if player.inventory.count_item("Copper Ore") >= 5 and player.inventory.count_item("Tin Ore") >= 5 and player.gold >= 50:
                player.inventory.remove_items("Copper Ore", 5)
                player.inventory.remove_items("Tin Ore", 5)
                player.gold -= 50
                bronze_armour = Armour("Bronze Armour", "+3 Defence Buff", 3)
                player.inventory.add_equipment(bronze_armour)
                print("You have purchased Bronze Armour.")
            else:
                print("\nYou cannot afford the Bronze Armour.")
            input("\nPress enter to continue...")
        elif choice == '2':
            if player.inventory.count_item("Iron Ore") >= 10 and player.gold >= 200:
                player.inventory.remove_items("Iron Ore", 10)
                player.gold -= 200
                iron_armour = Armour("Iron Armour", "+7 Defence Buff", 7)
                player.inventory.add_equipment(iron_armour)
                print("You have purchased Iron Armour.")
            else:
                print("\nYou cannot afford the Iron Armour.")
            input("\nPress enter to continue...")
        elif choice == '3':
            if player.inventory.count_item("Iron Ore") >= 25 and player.inventory.count_item("Coal") >= 10 and player.gold >= 600:
                player.inventory.remove_items("Iron Ore", 25)
                player.inventory.remove_items("Coal", 10)
                player.gold -= 600
                steel_armour = Armour("Steel Armour", "+15 Defence Buff", 15)
                player.inventory.add_equipment(steel_armour)
                print("You have purchased Steel Armour.")
            else:
                print("\nYou cannot afford the Steel Armour.")
            input("\nPress enter to continue...")

        elif choice == '4' or choice == 'q':
            break
        else:
            print("Invalid choice. Please enter a valid number.")
            input("\nPress enter to continue...")

def check_ores_in_inventory(player, tin_count, copper_count):
    
    return (player.inventory.count_item("Tin Ore") >= tin_count and
            player.inventory.count_item("Copper Ore") >= copper_count)

def complete_blacksmith_quest(player):
    required_tin_count = 5
    required_copper_count = 5

    if player.inventory.count_item("Tin Ore") >= required_tin_count and player.inventory.count_item("Copper Ore") >= required_copper_count:
        player.inventory.remove_items("Tin Ore", required_tin_count)
        player.inventory.remove_items("Copper Ore", required_copper_count)

        player.quests["blacksmith_quest"]["completed"] = True
        player.quests["blacksmith_quest"]["reward_given"] = True  

        bronze_armour = Armour("Bronze Armour", "Sturdy armour crafted by the Northern Hills blacksmith.", defense_boost=3)
        player.inventory.add_equipment(bronze_armour)
        print(Fore.YELLOW + "Old Man:" + Style.RESET_ALL + f" 'Thank you, {player.name}! Here is your Bronze Armour, as promised.'")
        print("You received 'Bronze Armour' from the blacksmith.")
    else:
        print(Fore.YELLOW + "Old Man:" + Style.RESET_ALL + f" '{player.name}, remember, I need 5 Tin Ore and 5 Copper Ore for the armour.'")


def offer_blacksmith_quest(player):
    print(Fore.YELLOW + "Old Man:" + Style.RESET_ALL + " 'I need 5 copper and 5 tin ore to make some bronze armour. Will you bring them to me?'")
    quest_acceptance = input("Accept quest? (Y/N): ").strip().lower()
    if quest_acceptance == 'y':
        print("\nYou have accepted the quest.\n")
        print(Fore.YELLOW + "Old Man:" + Style.RESET_ALL + " 'I knew you wouldn't let me down.'")
        player.quests["blacksmith_quest"] = {"accepted": True, "completed": False}
        #input("\nPress enter to continue...")
    else:
        print("\nYou have declined the quest.")
