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
    print("\nSearching the Dark Forest...")
    found_item = get_location_loot(DARK_FOREST_LOOT)
    if found_item:
        print(f"You found a {found_item.name}!")
        player.inventory.add_item(found_item)
    else:
        print("You searched the forest but found nothing of interest.")

def get_location_loot(loot_table):
    roll = random.randint(1, 100)
    for name, info in loot_table.items():
        if roll <= info["chance"]:
            return Item(name, info["description"])
    return None


DARK_FOREST_LOOT = {
    "Mystic Herb": {"description": "A herb used in the concoction of various potions.", "chance": 20},
    "Ancient Coin": {"description": "An old coin from a forgotten era.", "chance": 10},
    "Lost Necklace": {"description": "A beautiful necklace, lost in time.", "chance": 5},
    # Add other items as needed
}
