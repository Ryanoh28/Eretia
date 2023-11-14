from utilities import clear_console
import random
from combat import fight_monster
from items import Item

ORE_EXPERIENCE_POINTS = {
    "Copper Ore": 5,
    "Tin Ore": 8,
    "Iron Ore": 12
}

def gain_mining_experience(player, ore):
    
    exp = ORE_EXPERIENCE_POINTS.get(ore, 0)
    player.mining_experience += exp
    print(f"Gained {exp} mining experience.")

    if player.mining_experience >= 100:
        player.mining_experience -= 100
        player.mining_level += 1
        print(f"Congratulations! Your mining level is now {player.mining_level}.")


def mine_in_damp_cave(player, shop):
    clear_console()
    print("You start mining...")
    energy_cost_per_mine = 10  

    if player.energy >= energy_cost_per_mine:
        player.consume_energy(energy_cost_per_mine)  

        mining_successful = random.randint(1, 10) <= player.mining_level

        if mining_successful:
            ore = random.choices(
                ["Copper Ore", "Tin Ore", "Iron Ore"],
                weights=(60, 30, 10) if player.mining_level < 5 else (30, 40, 30),
                k=1
            )[0]

            print(f"You have successfully mined {ore}!")

            mined_ore = Item(ore, f"A piece of {ore} mined from the Damp Cave.")
            player.inventory.add_item(mined_ore)

            gain_mining_experience(player, ore)

            if random.randint(1, 4) == 1:
                print("\nAs you mine, a monster emerges from the depths of the cave!")
                fight_monster(player, shop, "Damp Cave")
        else:
            print("Your mining attempt was unsuccessful. All you see is stone!")
    else:
        print("You don't have enough energy to mine. Rest to regain energy.")

    input("\nPress Enter to continue...")

######/\/\/\/\/\/\/\####DAMP CAVE MINING#########/\/\/\/\/\/\/\#################