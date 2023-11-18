from utilities import clear_console
import random
from combat import fight_monster
from items import Item

ORE_EXPERIENCE_POINTS = {
    "Copper Ore": 3,
    "Tin Ore": 4,
    "Iron Ore": 5,
    "Stone": 1, 
    "Coal": 8,
    "Mithril": 12 
}
def mine(player, location, ore_level_table):
    clear_console()

    has_iron_pickaxe = player.inventory.has_item("Iron Pickaxe")

    if has_iron_pickaxe:
        print("You start mining with your Iron Pickaxe...\n")
        success_chance = player.mining_level + 1 + (player.mining_level * 0.20)
    else:
        print("You start mining...\n")
        success_chance = player.mining_level

    energy_cost_per_mine = 10

    if player.energy >= energy_cost_per_mine:
        player.consume_energy(energy_cost_per_mine)
        mining_successful = random.randint(1, 10) <= success_chance

        if mining_successful:
            available_ores = [ore for ore, level in ore_level_table.items() if player.mining_level >= level]
            ore_weights = [ore_level_table[ore] for ore in available_ores]
            ore = random.choices(available_ores, weights=ore_weights, k=1)[0]

            print(f"You have successfully mined {ore}!")
            mined_ore = Item(ore, f"A piece of {ore} mined from the {location}.")
            player.inventory.add_item(mined_ore)

            # Monster encounter check
            if random.randint(1, 4) == 1:
                print("\nAs you mine, a monster emerges from the depths of the mine!")
                input("\nPress enter to continue...")
                fight_monster(player, location)

        else:
            print("Your mining attempt was unsuccessful. All you see is stone!")
            stone_item = Item("Stone", "A common stone, not worth much but can be sold.\n")
            player.inventory.add_item(stone_item)

    else:
        print("You don't have enough energy to mine. Rest to regain energy.")



def gain_mining_experience(player, ore):
    exp = ORE_EXPERIENCE_POINTS.get(ore, 0)
    level_factor = 1 + (player.mining_level - 1) * 0.1  # Scaling factor based on mining level
    exp_gained = int(exp * level_factor)
    player.mining_experience += exp_gained

    print(f"{player.name} gained {exp_gained} mining experience points.")

    # Check for mining level up
    while player.mining_experience >= 100:
        player.mining_experience -= 100
        player.mining_level += 1
        print(f"Congratulations! Your mining level is now {player.mining_level}.")



ORE_LEVEL_TABLE = {
    "Copper Ore": 1,
    "Tin Ore": 1,
    "Iron Ore": 5,
    "Coal": 8
    # Add more ores and their corresponding levels here
}


def mine_in_damp_cave(player):
    player.current_location = 'Damp Cave'
    
    while True:
        continue_mining = input("\nDo you want to mine in the Damp Cave? (Y/N): ").lower()
        if continue_mining == 'y':
            mine(player, 'Damp Cave', ORE_LEVEL_TABLE)
        else:
            break



