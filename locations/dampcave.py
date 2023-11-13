from utilities import clear_console
import random
from items import Item
from combat import fight_monster, create_monster

def enter_damp_cave(player, shop):
    while True:
        clear_console()
        print("You are in the Damp Cave. What would you like to do?\n")
        print("1. Explore")
        print("2. Search for items")
        print("3. Mine")
        print("4. Return to Camp")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            # Logic for exploring the cave
            pass
        elif choice == "2":
            # Logic for searching for items
            pass
        elif choice == "3":
            mine_in_cave(player, shop)
        elif choice == "4":
            break  # Exit the function, returning the player to the previous menu or location
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

def mine_in_cave(player, shop):
    clear_console()
    print("You start mining...")

    mining_successful = random.randint(1, 10) <= player.mining_level
    exp_gain = {"Copper Ore": 2, "Tin Ore": 2, "Iron Ore": 3}

    if mining_successful:
        ore = random.choices(
            ["Copper Ore", "Tin Ore", "Iron Ore"],
            weights=(60, 30, 10) if player.mining_level < 5 else (30, 40, 30),
            k=1
        )[0]

        print(f"You have successfully mined {ore}!")

        mined_ore = Item(ore, f"A piece of {ore} mined from the Damp Cave.")
        player.inventory.add_item(mined_ore)

        # Gain mining experience
        player.gain_mining_experience(exp_gain[ore])

        if random.randint(1, 4) == 1:
            print("\nAs you mine, a monster emerges from the depths of the cave!")
            fight_monster(player, shop, "Damp Cave")
    else:
        print("Your mining attempt was unsuccessful. Better luck next time!")

    input("\nPress Enter to continue...")






