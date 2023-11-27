from misc.utilities import clear_console
import random
from misc.items import Item
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
            from locations.bordertown import leave_town_west
            leave_town_west(player)
        elif choice == "3":
            clear_console()
            rest_in_location(player) 
        else:
            input("\nInvalid choice. Please enter a number between 1 and 3.")



def calculate_rare_fish_weight_linear(player_level):
    max_level = 100
    min_weight = 4
    max_weight = 75

    if player_level >= max_level:
        return max_weight
    else:
        return min_weight + (player_level - 1) * ((max_weight - min_weight) / (max_level - 1))


def fishing(player, location, FISH_LEVEL_TABLE):
    clear_console()
    has_fishing_rod = player.inventory.has_item("Fishing Rod")
    success_chance = player.fishing_level + 1 if has_fishing_rod else player.fishing_level
    energy_cost_per_cast = 10

    if player.energy >= energy_cost_per_cast:
        player.consume_energy(energy_cost_per_cast)
        fishing_successful = random.randint(1, 10) <= success_chance

        if fishing_successful:
            rare_fish_weight = calculate_rare_fish_weight_linear(player.fishing_level)
            adjusted_fish_weights = {
                "Small Fish": max(1, 10 - player.fishing_level),  
                "Medium Fish": max(1, player.fishing_level - 4) if player.fishing_level >= 5 else 0,  
                "Large Fish": max(1, player.fishing_level - 14) if player.fishing_level >= 15 else 0,  
                "Rare Fish": rare_fish_weight if player.fishing_level >= 25 else 0  
            }

            available_fish = [fish for fish, level in FISH_LEVEL_TABLE.items() if player.fishing_level >= level]
            fish_weights = [adjusted_fish_weights[fish] for fish in available_fish]
            caught_fish = random.choices(available_fish, weights=fish_weights, k=1)[0]

            print(f"You have successfully caught a {caught_fish}!\n")
            caught_fish_item = Item(caught_fish, f"A {caught_fish} caught from the {location}.")
            gain_fishing_experience(player, caught_fish)
            player.inventory.add_item(caught_fish_item)
            input("\nPress enter to continue...")
        else:
            print("Your fishing attempt was unsuccessful. No fish bite this time.\n")
            player.fishing_experience += 1
            print(f"You gained 1 fishing experience point.\n")
            input("Press enter to continue...")  
    else:
        print("\nYou don't have enough energy to fish. Rest to regain energy.")
        input("\nPress enter to continue...")  

    
def gain_fishing_experience(player, caught_fish):
    FISH_EXPERIENCE_POINTS = {
        "Small Fish": 3,
        "Medium Fish": 6,
        "Large Fish": 10,
        "Rare Fish": 20
    }
    exp = FISH_EXPERIENCE_POINTS.get(caught_fish, 0)
    player.fishing_experience += exp
    while player.fishing_experience >= 100 + (10 * (player.fishing_level - 1)):
        player.fishing_experience -= 100 + (10 * (player.fishing_level - 1))
        player.fishing_level += 1
        print(f"\nCongratulations! Your fishing level is now {player.fishing_level}.")



def calculate_rare_fish_weight(player_level):
    max_level = 100
    min_weight = 4
    max_weight = 75  

    if player_level >= max_level:
        return max_weight
    else:
        
        return min_weight + (player_level - 1) * ((max_weight - min_weight) / (max_level - 1))



FISH_EXPERIENCE_POINTS = {
    "Small Fish": 3,
    "Medium Fish": 6,
    "Large Fish": 10,
    "Rare Fish": 20
}


FISH_LEVEL_TABLE = {
    "Small Fish": 1,  
    "Medium Fish": 5,  
    "Large Fish": 15,  
    "Rare Fish": 25  
}



