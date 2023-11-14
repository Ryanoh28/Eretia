from combat import fight_monster
from utilities import clear_console
from items import get_location_loot
from locations.locationfunctions import rest_in_location

from locations.locationfunctions import rest_in_location

def enter_dark_forest(player, shop):
    player.current_location = 'dark_forest'
    while True:
        clear_console()
        print("You are in the Dark Forest. What would you like to do?\n")
        print("1. Hunt Monsters")
        print("2. Search Dark Forest")
        print("3. Inventory")
        print("4. Rest")
        print("5. Return to Camp")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            fight_monster(player, shop, "Dark Forest")
        elif choice == "2":
            search_dark_forest(player)
        elif choice == "3":
            player.inventory.inventory_menu(player)  
        elif choice == "4":
            clear_console()
            rest_in_location(player)
        elif choice == "5":
            from camp import return_to_camp
            return_to_camp(player, shop)
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")


def search_dark_forest(player):
    clear_console()
    energy_cost_per_search = 10  

    if player.energy >= energy_cost_per_search:
        print("Searching the Dark Forest...\n")
        
        found_item = get_location_loot(DARK_FOREST_LOOT)

        if found_item:
            print(f"You found a {found_item.name}!")
            player.inventory.add_item(found_item)
            #print(f"Added {found_item.name} to inventory")
            player.consume_energy(energy_cost_per_search)  
            #print(f"Used {energy_cost_per_search} energy. Remaining energy: {player.energy}\n")

            examine_choice = input("\nDo you want to examine it? (Y/N): ").lower().strip()
            if examine_choice == 'y':
                clear_console()
                print(f"{found_item.name}: {found_item.description}")
            
            input("\nPress Enter to continue...")  
        else:
            player.consume_energy(energy_cost_per_search)  
            print("You searched the forest but found nothing of interest.")
            print(f"Used {energy_cost_per_search} energy. Remaining energy: {player.energy}\n")
            input("Press Enter to continue...")
    else:
        print("You don't have enough energy to search. Rest to regain energy.")
        input("\nPress Enter to continue...")




DARK_FOREST_LOOT = {
    "Mystic Herb": {"description": "A herb used in the concoction of various potions.", "chance": 35},
    "Ancient Coin": {"description": "An old coin from a forgotten era.", "chance": 10},
    "Lost Necklace": {"description": "A beautiful necklace, lost in time.", "chance": 5},
    "Tangled Vine": {"description": "A common vine, often found entangled in trees.", "chance": 35},
    "Mossy Pebble": {"description": "A small stone covered in soft moss.", "chance": 35},
    "Cracked Pottery Shard": {"description": "A fragment of an ancient clay pot.", "chance": 30}
}
