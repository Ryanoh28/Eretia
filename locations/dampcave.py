from utilities import clear_console
from skills.mining import mine_in_damp_cave
from items import get_location_loot, Item, get_location_loot
from locations.locationfunctions import rest_in_location

import random
from combat import fight_monster



def enter_damp_cave(player, shop):
    player.current_location = 'damp_cave'
    while True:
        clear_console()
        print("You are in the Damp Cave. What would you like to do?\n")
        print("1. Explore the Passages")
        print("2. Mine")
        print("3. Rest")
        print("4. Inventory")
        print("5. Return to Border Town")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            explore_passages(player, shop)
        elif choice == "2":
            mine_in_damp_cave(player, shop)
        elif choice == "3":
            clear_console()
            rest_in_location(player)
        elif choice == "4":
            player.inventory.inventory_menu(player)
        elif choice == "5":
            from bordertown import return_to_border_town
            player.current_location = None
            return_to_border_town(player, shop)
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")



def explore_passages(player, shop):
    player.current_location = 'cave_entrance'
    clear_console()
    print("You stand at the entrance of a series of dark, winding tunnels within the Damp Cave.\n")

    while True:
        print("Which direction would you like to explore?\n")
        print("1. Left Tunnel")
        print("2. Right Tunnel")
        print("3. Straight Ahead")
        print("4. Return to Damp Cave Entrance")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            explore_left_tunnel(player, shop)
        elif choice == "2":
            explore_right_tunnel(player, shop)
            pass
        elif choice == "3":
            #explore_straight_ahead(player, shop)
            pass
        elif choice == "4":
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

    enter_damp_cave(player, shop)

def explore_right_tunnel(player, shop, section=1):
    clear_console()
    
    if section == 1:
        print("As you venture deeper into the right tunnel, a hidden chamber is revealed.")
        print("The chamber is dimly lit by an eerie, luminescent glow, revealing walls adorned with ancient carvings and scriptures.")
        print("\nWhat would you like to do?\n")
        print("1. Continue walking")
        print("2. Return")
        next_action = input("\nEnter your choice (1-2): ").strip()

    elif section == 2:
        print("The carvings depict the early days of the Great Beast Tide, showing monstrous creatures overwhelming settlements and everything else in its path.")
        print("\nWhat would you like to do?\n")
        print("1. Delve deeper into the story")
        print("2. Return")
        next_action = input("\nEnter your choice (1-2): ").strip()

    elif section == 3:
        print("Further down, the story transitions to the formation of Border Town, a symbol of hope and defiance situated on the outer edges of Eretia to offer a point of resistance to any future attack.")
        print("\nWhat would you like to do?\n")
        print("1. Continue uncovering the history")
        print("2. Head back")
        next_action = input("\nEnter your choice (1-2): ").strip()

    elif section == 4:
        print("The narrative honors the heroes and sacrifices made during the Great Beast Tide, ending with a significant turning point where the monsters were forced back over the border.")
        print("\nWhat would you like to do?\n")
        print("1. Reflect on the stories")
        print("2. Leave")
        next_action = input("\nEnter your choice (1-2): ").strip()

    # Process the player's choice
    if next_action == "1":
        if section < 4:
            explore_right_tunnel(player, shop, section + 1)
        else:
            clear_console()
            print("\nYou've reached the end of the carvings, filled with a sense of awe at the history before you. What you have just read reaffirms your decision to venture out to the edges of Eretia.")
            input("\nPress Enter to return to the cave entrance...")
            explore_passages(player, shop)
    elif next_action == "2":
        explore_passages(player, shop)
    else:
        print("\nInvalid choice. Please enter a valid number.")
        input("\nPress Enter to continue...")
        explore_right_tunnel(player, shop, section)



def explore_left_tunnel(player, shop, first_time=True):
    clear_console()

    
    energy_cost_per_exploration = 10

    
    if player.energy < energy_cost_per_exploration:
        print("You don't have enough energy to continue exploring. Rest to regain energy.")
        input("\nPress Enter to continue...")
        return

    
    if first_time:
        print("You cautiously venture into the left tunnel. It's dimly lit and the air feels damp.\n")
    else:
        print("You continue down the left tunnel...\n")

    
    player.consume_energy(energy_cost_per_exploration)

    
    found_item = get_location_loot(DAMP_CAVE_LOOT)

    if found_item:
        print(f"You found a {found_item.name}!")
        player.inventory.add_item(found_item)

        examine_choice = input("\nDo you want to examine it? (Y/N): ").lower().strip()
        if examine_choice == 'y':
            clear_console()
            print(f"{found_item.name}: {found_item.description}\n")
            input("Press enter to continue...")

    if random.randint(1, 3) == 1:
        clear_console()
        print("As you explore, a monster emerges from the shadows of the tunnel!")
        input("\nPress enter to continue...")
        fight_monster(player, shop, "Damp Cave")

    clear_console()
    print("What would you like to do next?\n")
    print("1. Continue exploring this tunnel")
    print("2. Return to the tunnel entrance")
    next_action = input("\nEnter your choice (1-2): ").strip()

    if next_action == "1":
        explore_left_tunnel(player, shop, first_time=False)  
    elif next_action == "2":
        explore_passages(player, shop)
    else:
        clear_console()
        print("Invalid choice. Please enter a valid number.")
        input("Press Enter to continue...")








DAMP_CAVE_LOOT = {
    "Damp Moss": {"description": "Common moss with basic alchemical properties.", "chance": 40},
    "Flickering Crystal Shard": {"description": "A dimly glowing crystal shard.", "chance": 25},
    "Cave Pearl": {"description": "A rare and beautiful pearl formed in cave pools.", "chance": 15},
    "Ancient Bone Fragment": {"description": "A fragment of bone from an ancient creature.", "chance": 10},
    "Glowing Mushroom": {"description": "A rare mushroom that emits a soft light.", "chance": 4},
    "Ethereal Stone": {"description": "A stone shimmering with otherworldly energy.", "chance": 1},
    "Fossilized Bone": {"description": "A bone from an ancient creature, long extinct.", "chance": 10}
}










