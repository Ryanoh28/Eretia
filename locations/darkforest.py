from combat import fight_monster
from utilities import clear_console

from classes import Item
from items import get_location_loot

def enter_dark_forest(player, shop):
    while True:
        clear_console()
        print("You are in the Dark Forest. What would you like to do?\n")
        choice = input("(H)unt Monsters, (S)earch Dark Forest, or (R)eturn to Camp: ").lower().strip()
        clear_console()

        if choice == "h":
            fight_monster(player, shop, "Dark Forest")  
        elif choice == "s":
            search_dark_forest(player)
        elif choice == "r":
            from camp import return_to_camp
            return_to_camp(player, shop)
            break  
        else:
            print("\nInvalid choice. Please enter 'H' to hunt monsters or 'R' to return to camp.\n")

def search_dark_forest(player):
    energy_cost_per_search = 10  

    if player.energy >= energy_cost_per_search:
        print("Searching the Dark Forest...\n")
        player.consume_energy(energy_cost_per_search)  

        found_item = get_location_loot(DARK_FOREST_LOOT)

        if found_item:
            print(f"You found a {found_item.name}!")
            player.inventory.add_item(found_item)
            
            examine_choice = input("Do you want to examine it? (Y/N): ").lower().strip()
            if examine_choice == 'y':
                clear_console()
                print(f"{found_item.name}: {found_item.description}")
            
            input("\nPress Enter to continue...")  
        else:
            print("You searched the forest but found nothing of interest.")
            input("Press Enter to continue...")
    else:
        print("You don't have enough energy to search. Rest to regain energy.")
        input("Press Enter to continue...")


DARK_FOREST_LOOT = {
    "Mystic Herb": {"description": "A herb used in the concoction of various potions.", "chance": 35},
    "Ancient Coin": {"description": "An old coin from a forgotten era.", "chance": 10},
    "Lost Necklace": {"description": "A beautiful necklace, lost in time.", "chance": 5},
    "Tangled Vine": {"description": "A common vine, often found entangled in trees.", "chance": 35},
    "Mossy Pebble": {"description": "A small stone covered in soft moss.", "chance": 35},
    "Cracked Pottery Shard": {"description": "A fragment of an ancient clay pot.", "chance": 30}
}
