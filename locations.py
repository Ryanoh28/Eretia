from combat import fight_monster
from utilities import clear_console
import random
from classes import Item

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
    if player.search_count < 5:
        print("Searching the Dark Forest...\n")
        found_item = get_location_loot(DARK_FOREST_LOOT)

        if found_item:
            print(f"You found a {found_item.name}!")
            player.inventory.add_item(found_item)
            
            examine_choice = input("Do you want to examine it? (Y/N): ").lower().strip()
            if examine_choice == 'y':
                clear_console()
                print(f"\n{found_item.name}: {found_item.description}")
            
            input("\nPress Enter to continue...")  # Return to the forest menu after pressing enter once.
        else:
            print("You searched the forest but found nothing of interest.")
            input("Press Enter to continue...")

        player.search_count += 1
    else:
        print("You have exhausted your searches in the Dark Forest for now. Return to camp and rest to continue searching.\n")
        input("Press Enter to continue...")




def get_location_loot(loot_table):
    total_chance = sum(info["chance"] for info in loot_table.values())
    roll = random.randint(1, total_chance)

    cumulative_chance = 0
    for name, info in loot_table.items():
        cumulative_chance += info["chance"]
        if roll <= cumulative_chance:
            return Item(name, info["description"])
    
    return None

DARK_FOREST_LOOT = {
    "Mystic Herb": {"description": "A herb used in the concoction of various potions.", "chance": 20},
    "Ancient Coin": {"description": "An old coin from a forgotten era.", "chance": 10},
    "Lost Necklace": {"description": "A beautiful necklace, lost in time.", "chance": 5},
    # Add other items as needed
}
