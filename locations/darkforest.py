from misc.combat import fight_monster
from misc.utilities import clear_console
from misc.items import get_location_loot
from locations.locationfunctions import rest_in_location



def enter_dark_forest(player):
    player.current_location = 'dark_forest'
    while True:
        clear_console()
        print("You are in the Dark Forest. What would you like to do?\n")
        print("1. Hunt Monsters")
        print("2. Search Dark Forest")
        print("3. Inventory")
        print("4. Rest")
        print("5. Border Town Outskirts")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            fight_monster(player, "Dark Forest")
        elif choice == "2":
            search_dark_forest(player)
        elif choice == "3":
            player.inventory.inventory_menu(player)  
        elif choice == "4":
            clear_console()
            rest_in_location(player)
        elif choice == "5":
            from locations.bordertown import leave_town
            player.current_location = 'border_town'
            leave_town(player)
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")


def search_dark_forest(player):
    player.current_location = 'dark_forest'
    clear_console()
    energy_cost_per_search = 10  

    while True:
        if player.energy >= energy_cost_per_search:
            print("Searching the Dark Forest...\n")
            
            found_item = get_location_loot(DARK_FOREST_LOOT)

            if found_item:
                print(f"You found a {found_item.name}!")
                player.inventory.add_item(found_item)
                player.consume_energy(energy_cost_per_search)  

                examine_choice = input("\nDo you want to examine it? (Y/N): ").lower().strip()
                if examine_choice == 'y':
                    clear_console()
                    print(f"{found_item.name}: {found_item.description}")
                    input("\nPress enter to continue...")
                
            else:
                player.consume_energy(energy_cost_per_search)  
                print("You searched the forest but found nothing of interest.")
                print(f"Used {energy_cost_per_search} energy. Remaining energy: {player.energy}\n")

        else:
            print("You don't have enough energy to search. Rest to regain energy.")
            input("\nPress enter to continue...")
            break

        # Ask the player if they want to continue searching or leave
        clear_console()
        print("What would you like to do next?\n")
        print("1. Continue Searching")
        print("2. Leave the Dark Forest")
        next_action = input("\nEnter your choice (1-2): ").strip()

        if next_action != "1":
            break
        clear_console()





DARK_FOREST_LOOT = {
    "Mystic Herb": {"description": "A herb used in the concoction of various potions.", "chance": 35},
    "Ancient Coin": {"description": "An old coin from a forgotten era.", "chance": 10},
    "Lost Necklace": {"description": "A beautiful necklace, lost in time.", "chance": 5},
    "Tangled Vine": {"description": "A common vine, often found entangled in trees.", "chance": 35},
    "Mossy Pebble": {"description": "A small stone covered in soft moss.", "chance": 35},
    "Cracked Pottery Shard": {"description": "A fragment of an ancient clay pot.", "chance": 30}
}
