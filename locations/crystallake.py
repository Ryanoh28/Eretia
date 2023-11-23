from utilities import clear_console
import random
from items import Item
from locations.locationfunctions import rest_in_location

def enter_crystal_lake(player):
    location = "Crystal Lake"  
    while True:
        clear_console()
        print("You look up and down a massive lake stemming from a faraway waterfall\n")
        print("1. Fish in the lake")
        print("2. Inventory")
        print("3. Rest")
        print("4. Return")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            if player.inventory.has_item("Fishing Rod"):
                fishing(player, location, FISH_LEVEL_TABLE)  
            else:
                print("\nYou need a Fishing Rod to fish.")
                input("\nPress enter to continue...")
        elif choice == "2":
            player.inventory.inventory_menu(player)
        elif choice == "4":
            from bordertown import leave_town_west
            leave_town_west(player)
        elif choice == "3":
            clear_console()
            rest_in_location(player) 
        else:
            input("\nInvalid choice. Please enter a number between 1 and 3.")





def fishing(player, location, FISH_LEVEL_TABLE):
    clear_console()

    has_fishing_rod = player.inventory.has_item("Fishing Rod")

    if has_fishing_rod:
        print("You start fishing with your Fishing Rod...\n")
        success_chance = player.fishing_level + 1 + (player.fishing_level * 0.20)
    else:
        print("You start fishing...\n")
        success_chance = player.fishing_level

    energy_cost_per_cast = 10

    if player.energy >= energy_cost_per_cast:
        player.consume_energy(energy_cost_per_cast)
        fishing_successful = random.randint(1, 10) <= success_chance

        if fishing_successful:
            available_fish = [fish for fish, level in FISH_LEVEL_TABLE.items() if player.fishing_level >= level]
            fish_weights = [FISH_LEVEL_TABLE[fish] for fish in available_fish]
            caught_fish = random.choices(available_fish, weights=fish_weights, k=1)[0]

            print(f"You have successfully caught a {caught_fish}!\n")
            caught_fish_item = Item(caught_fish, f"A {caught_fish} caught from the {location}.")
            gain_fishing_experience(player, caught_fish)
            player.inventory.add_item(caught_fish_item)
            input("\nPress enter to continue...") 

            gain_fishing_experience(player, caught_fish)

        else:
            print("Your fishing attempt was unsuccessful. No fish bite this time.\n")
            input("Press enter to continue...")  

    else:
        print("\nYou don't have enough energy to fish. Rest to regain energy.")
        input("\nPress enter to continue...")  



def gain_fishing_experience(player, caught_fish):
    exp = FISH_EXPERIENCE_POINTS.get(caught_fish, 0)
    level_factor = 1 + (player.fishing_level - 1) * 0.1
    exp_gained = int(exp * level_factor)
    player.fishing_experience += exp_gained

    #print(f"{player.name} gained {exp_gained} fishing experience points.")

    while player.fishing_experience >= 100 + (10 * (player.fishing_level - 1)):
        player.fishing_experience -= 100 + (10 * (player.fishing_level - 1))
        player.fishing_level += 1
        print(f"Congratulations! Your fishing level is now {player.fishing_level}.")



FISH_LEVEL_TABLE = {
    "Small Fish": 1,
    "Medium Fish": 3,
    "Large Fish": 6,
    "Rare Fish": 10
    
}

FISH_EXPERIENCE_POINTS = {}

for fish, level in FISH_LEVEL_TABLE.items():
    FISH_EXPERIENCE_POINTS[fish] = level

