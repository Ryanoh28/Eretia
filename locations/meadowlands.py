from utilities import clear_console
from skills.horticulture import HorticultureSkill

def meadowlands_menu(player):
    while True:
        clear_console()
        print("Welcome to the Meadowlands!")
        print("A peaceful area filled with lush greenery and vibrant flora.\n")
        print("1. Explore the Meadowlands")
        print("2. Horticulture Activities")
        print("3. Talk to the Local Farmer (for seeds and advice)")
        print("4. Return to Border Town")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            pass
            #explore_meadowlands(player)
        elif choice == "2":
            horticulture_submenu(player)
        elif choice == "3":
            pass
            #talk_to_farmer(player)
        elif choice == "4":
            print("\nReturning to Border Town.")
            from bordertown import return_to_border_town
            return_to_border_town(player)
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

def horticulture_submenu(player):
    while True:
        print("\n=== Horticulture Activities ===")
        print("1. Plant Seeds")
        print("2. Check on Planted Crops")
        print("3. Harvest Mature Plants")
        print("4. Return to Meadowlands Menu")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            plant_seeds(player)
        elif choice == "2":
            pass
            #check_crops(player)
        elif choice == "3":
            pass
            #harvest_plants(player)
        elif choice == "4":
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

def plant_seeds(player):
    seed_names = [item_name for item_name, item_info in player.inventory.items.items() if "Seed" in item_name]
    seed_counts = {seed_name: player.inventory.count_item(seed_name) for seed_name in seed_names}

    if not seed_names:
        print("You have no seeds to plant. Consider talking to the local farmer to get some.")
        return

    print("Select the seeds you want to plant:")
    for i, (seed_name, count) in enumerate(seed_counts.items(), 1):
        print(f"{i}. {seed_name} (Quantity: {count})")

    choice = input("\nEnter your choice (number): ").strip()

    if choice.isdigit() and 1 <= int(choice) <= len(seed_names):
        selected_seed = seed_names[int(choice) - 1]

        player.inventory.remove_items(selected_seed, 1)

        # Logic to plant the selected seed
        print(f"You have planted {selected_seed}.")
        # Add code here for adding the seed to the garden
    else:
        print("Invalid choice. Please enter a valid number.")


