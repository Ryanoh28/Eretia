from utilities import clear_console
from skills.mining import mine_in_damp_cave
from items import get_location_loot
from locations.locationfunctions import rest_in_location
import random

from locations.locationfunctions import rest_in_location

def enter_damp_cave(player, shop):
    while True:
        clear_console()
        print("You are in the Damp Cave. What would you like to do?\n")
        print("1. Explore the Passages")
        print("2. Search Damp Cave")
        print("3. Mine")
        print("4. Rest")
        print("5. Inventory")
        print("6. Return to Camp")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            # Logic for exploring the cave
            pass
        elif choice == "2":
            search_damp_cave(player)
        elif choice == "3":
            mine_in_damp_cave(player, shop)
        elif choice == "4":
            clear_console()
            rest_in_location(player)
        elif choice == "5":
            player.inventory.inventory_menu(player)
        elif choice == "6":
            break  
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")



DAMP_CAVE_LOOT = {
    "Damp Moss": {"description": "Common moss with basic alchemical properties.", "chance": 40},
    "Flickering Crystal Shard": {"description": "A dimly glowing crystal shard.", "chance": 30},
    "Cave Pearl": {"description": "A rare and beautiful pearl formed in cave pools.", "chance": 15},
    "Ancient Bone Fragment": {"description": "A fragment of bone from an ancient creature.", "chance": 10},
    "Glowing Mushroom": {"description": "A rare mushroom that emits a soft light.", "chance": 4},
    "Ethereal Stone": {"description": "A stone shimmering with otherworldly energy.", "chance": 1}
}

# def search_damp_cave(player):
#     clear_console()  
#     energy_cost_per_search = 10  

#     if player.energy >= energy_cost_per_search:
#         print("Searching the Damp Cave...\n")
#         player.consume_energy(energy_cost_per_search)

#         if random.randint(1, 2) == 1:
#             found_item = get_location_loot(DAMP_CAVE_LOOT)

#             if found_item:
#                 print(f"You found a {found_item.name}!")
#                 player.inventory.add_item(found_item)
                
#                 examine_choice = input("Do you want to examine it? (Y/N): ").lower().strip()
#                 if examine_choice == 'y':
#                     clear_console()
#                     print(f"{found_item.name}: {found_item.description}")
#             else:
#                 print("You searched the cave but found nothing of interest.")
#         else:
#             print("You searched the cave but found nothing this time.")
#     else:
#         clear_console()  
#         print("You don't have enough energy to search. Rest to regain energy.")

#     input("\nPress Enter to continue...")  

def search_damp_cave(player):
    clear_console()  
    energy_cost_per_search = 10  

    if player.energy >= energy_cost_per_search:
        print("Searching the Damp Cave...\n")

        if random.randint(1, 2) == 1:
            found_item = get_location_loot(DAMP_CAVE_LOOT)

            if found_item:
                print(f"You found a {found_item.name}!")
                player.inventory.add_item(found_item)

                player.consume_energy(energy_cost_per_search)
                #print(f"Used {energy_cost_per_search} energy. Remaining energy: {player.energy}")
                
                examine_choice = input("\nDo you want to examine it? (Y/N): ").lower().strip()
                if examine_choice == 'y':
                    clear_console()
                    print(f"{found_item.name}: {found_item.description}")
            else:
                player.consume_energy(energy_cost_per_search)
                print("You searched the cave but found nothing of interest.")
                print(f"Used {energy_cost_per_search} energy. Remaining energy: {player.energy}")
        else:
            
            print("You searched the cave but found nothing this time.")
            player.consume_energy(energy_cost_per_search)
            #print(f"Used {energy_cost_per_search} energy. Remaining energy: {player.energy}")
    else:
        clear_console()  
        print("You don't have enough energy to search. Rest to regain energy.")

    input("\nPress Enter to continue...")  









