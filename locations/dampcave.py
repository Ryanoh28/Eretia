from utilities import clear_console
from skills.mining import mine_in_damp_cave
from items import get_location_loot, Item, EnchantedFruit, MageStaff, Rune
from locations.locationfunctions import rest_in_location
from colorama import Fore
import random
from combat import fight_monster



def enter_damp_cave(player):
    player.current_location = 'Damp Cave'
    
    while True:
        clear_console()
        print("You are in the Damp Cave. What would you like to do?\n")
        print("1. Explore the Passages")
        print("2. Mine")
        print("3. Rest")
        print("4. Inventory")
        print("5. Border Town Outskirts")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            explore_passages(player)
        elif choice == "2":
            player.current_location = "Damp Cave"
            
            mine_in_damp_cave(player)
        elif choice == "3":
            clear_console()
            rest_in_location(player)
        elif choice == "4":
            player.inventory.inventory_menu(player)
        elif choice == "5":
            from bordertown import leave_town
            player.current_location = None
            leave_town(player)
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")



def explore_passages(player):
    player.current_location = 'cave_entrance'
    clear_console()
    print("You stand at the entrance of a series of dark, winding tunnels within the Damp Cave.\n")

    while True:
        print("Which direction would you like to explore?\n")
        print("1. Left Tunnel")
        print("2. Right Tunnel")
        print("3. Straight Ahead")
        print("4. Return to Damp Cave Entrance")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            explore_left_tunnel(player)
        elif choice == "2":
            explore_right_tunnel(player)
        elif choice == "3":
            explore_straight_ahead(player)
        elif choice == "4":
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

    enter_damp_cave(player)


def explore_right_tunnel(player, section=1):
    clear_console()
    
    if section == 1:
        print("As you venture deeper into the right tunnel, a hidden chamber is revealed.\n")
        print("The chamber is dimly lit by an eerie, luminescent glow, revealing walls adorned with ancient carvings and scriptures.")
        print("\nWhat would you like to do?\n")
        print("1. Continue walking")
        print("2. Return")
        next_action = input("\nEnter your choice (1-2): ").strip()

    elif section == 2:
        print("The carvings depict the early days of " + Fore.RED + "The Great Beast Tide" + Fore.RESET + ", showing monstrous creatures overwhelming settlements.")
        print("\nWhat would you like to do?\n")
        print("1. Delve deeper into the story")
        print("2. Return")
        next_action = input("\nEnter your choice (1-2): ").strip()

    elif section == 3:
        print("Further down, the story transitions to the formation of " + Fore.GREEN + "Border Town" + Fore.RESET + ", a symbol of " + Fore.CYAN + "hope" + Fore.RESET + " and " + Fore.CYAN + "defiance." + Fore.RESET)
        print("\nWhat would you like to do?\n")
        print("1. Continue uncovering the history")
        print("2. Head back")
        next_action = input("\nEnter your choice (1-2): ").strip()

    elif section == 4:
        print("The narrative honors " + Fore.YELLOW + "the heroes" + Fore.RESET + " and " + Fore.YELLOW + "sacrifices" + Fore.RESET + " made during " + Fore.RED + "The Great Beast Tide." + Fore.RESET 
)
        print("\nAs you reach the end of the carvings, you discover a hidden alcove with an ancient and ornate staff.\n")
        
        mage_staff = MageStaff()
        player.inventory.add_item(mage_staff)
        input("\nPress Enter to return to the cave entrance...")
        explore_passages(player)

    if next_action == "1":
        if section < 4:
            explore_right_tunnel(player, section + 1)
        else:
            input("\nPress Enter to return to the cave entrance...")
            explore_passages(player)
    elif next_action == "2":
        explore_passages(player)
    else:
        print("\nInvalid choice. Please enter a valid number.")
        input("\nPress Enter to continue...")
        explore_right_tunnel(player, section)




def explore_left_tunnel(player, first_time=True):
    clear_console()

    
    energy_cost_per_exploration = 10

    
    if player.energy < energy_cost_per_exploration:
        print("You don't have enough energy to continue exploring. Rest to regain energy.")
        input("\nPress Enter to continue...")
        return

    
    if first_time:
        print("You cautiously venture into the left tunnel. It's dimly lit and the air feels damp.\n")
    else:
        print("You continue down the left tunnel...\n")

    
    player.consume_energy(energy_cost_per_exploration)

    
    found_item = get_location_loot(DAMP_CAVE_LOOT)

    if found_item:
        print(f"You found a {found_item.name}!")
        player.inventory.add_item(found_item)

        examine_choice = input("\nDo you want to examine it? (Y/N): ").lower().strip()
        if examine_choice == 'y':
            clear_console()
            print(f"{found_item.name}: {found_item.description}\n")
            input("Press enter to continue...")

    if random.randint(1, 3) == 1:
        clear_console()
        print("As you explore, a monster emerges from the shadows of the tunnel!")
        input("\nPress enter to continue...")
        fight_monster(player, "Damp Cave")

    clear_console()
    print("What would you like to do next?\n")
    print("1. Continue exploring this tunnel")
    print("2. Return to the tunnel entrance")
    next_action = input("\nEnter your choice (1-2): ").strip()

    if next_action == "1":
        explore_left_tunnel(player, first_time=False)  
    elif next_action == "2":
        explore_passages(player)
    else:
        clear_console()
        print("Invalid choice. Please enter a valid number.")
        input("Press Enter to continue...")

def explore_straight_ahead(player):
    clear_console()
    print("You venture straight into the heart of the cave, where the air grows cooler and the path less certain.\n")

    
    if not rune_sequence_barrier(player):
        return  

    
    continue_choice = input("Do you want to continue deeper into the cave? (Y/N): \n").lower().strip()
    if continue_choice != 'y':
        return

    
    enchanted_grove(player)

    
    echoing_cavern(player)


def rune_sequence_barrier(player):
    clear_console()
    print("You come across a barrier glowing with ancient runes: Earth, Water, Fire.")
    print("A rock, a pool of water, and a glowing mushroom are near the runes.")
    print("You must activate the runes in the correct sequence to pass.\n")

    # Assign numbers to runes
    rune_options = {'1': 'water', '2': 'earth', '3': 'fire'}
    correct_sequence = ['water', 'earth', 'fire']
    attempts = 0

    print("Enter the numbers corresponding to the runes in the sequence you wish to activate them.")
    print("For example, to activate Water, Earth, Fire in sequence, type '1,2,3' and press Enter.")

    while attempts < 3:
        print("\n1: Water, 2: Earth, 3: Fire\n")
        sequence_input = input("Enter your sequence: ").split(',')

        # Convert sequence to rune names
        sequence = [rune_options.get(num.strip(), '') for num in sequence_input]

        if sequence == correct_sequence:
            clear_console()
            print("\nThe barrier dissipates, revealing the path ahead.\n")

            if 'RunesReceived' not in player.flags:
                earth_rune = Rune("Earth Rune", "A rune embodying the essence of Earth.")
                water_rune = Rune("Water Rune", "A rune embodying the essence of Water.")
                fire_rune = Rune("Fire Rune", "A rune embodying the essence of Fire.")

                player.inventory.add_item(earth_rune)
                player.inventory.add_item(water_rune)
                player.inventory.add_item(fire_rune)

                print("You have received three mystical runes: Earth, Water, and Fire.")
                player.flags.add('RunesReceived')
            else:
                print("The path ahead is clear, but you find nothing new here.")

            input("\nPress Enter to continue...")
            clear_console()
            return True
        else:
            print("\nThe barrier remains intact. Something about the sequence is not right.")
            attempts += 1

    print("\nYou're unable to pass the barrier this time. Maybe you should try again later.")
    input("\nPress Enter to return to the previous area...")
    clear_console()
    return False








def enchanted_grove(player):
    clear_console()
    print("You find yourself in a serene grove, illuminated by bioluminescent plants.")
    
    print("\n1. Drink from the Healing Spring")
    print("2. Pick a fruit from the Enchanted Tree")
    print("3. Continue deeper into the cave")
    print("4. Return to the cave entrance")
    
    choice = input("\nEnter your choice (1-4): ").strip()

    if choice == "1":
        clear_console()
        player.max_health = 100  # or any other logic for drinking from the spring
        print("\nYou drink from the Healing Spring. Your health has been restored.")
        input("\nPress Enter to continue...")
        enchanted_grove(player)

    elif choice == "2":
        enchanted_fruit = EnchantedFruit("Enchanted Fruit", "A magical fruit that grants 50 experience when consumed.", 50)
        player.inventory.add_item(enchanted_fruit)
        clear_console()
        print("You pick a fruit from the Enchanted Tree. The tree withers away after you pluck the fruit.")
        input("\nPress Enter to continue...")
        enchanted_grove(player)

    elif choice == "3":
        echoing_cavern(player)

    elif choice == "4":
        explore_passages(player)

    else:
        print("\nInvalid choice. Please enter a valid number.")
        input("\nPress Enter to continue...")
        enchanted_grove(player)



    
    

def echoing_cavern(player):
    clear_console()
    print("You enter a cavern where every sound echoes, creating a disorienting effect.")
    
    print("\n1. Investigate Strange Sounds")
    print("2. Return to the cave entrance")
    
    choice = input("\nEnter your choice (1-2): ").strip()

    if choice == "1":
        # First, the player follows the echoes
        follow_the_echoes(player)
    elif choice == "2":
        explore_passages(player)
    else:
        print("\nInvalid choice. Please enter a valid number.")
        input("\nPress Enter to continue...")
        echoing_cavern(player)


def generate_echo_pattern():
    return [str(random.randint(1, 3)) for _ in range(4)]

def follow_the_echoes(player):
    clear_console()
    print("You decide to follow the echoes resonating through the cavern.")

    if player.echo_cavern_completed:
        print("\nYou remember the way through the cavern. There's nothing new to find here.")
        input("\nPress Enter to continue...")
        clear_console()
        echoing_cavern(player)
        return

    print("As you progress, the echoes form a pattern. To navigate successfully, you must remember and replicate the pattern.\n")

    pattern = generate_echo_pattern()
    print("You hear a sequence of sounds: " + " ".join(pattern))
    input("\nPress Enter to continue...")
    clear_console()

    player_response = input("Enter the sequence you heard (use numbers 1-3, separated by spaces): ").strip().split()
    clear_console()
    
    if player_response == pattern:
        print("You successfully navigate through the echoing cavern, finding yourself in a hidden alcove.")
        if not player.echo_cavern_completed:
            print("In the alcove, you discover a small stash of gold and a cluster of Mystic Herbs.\n")
            player.gold += 50
            mystic_herb = Item("Mystic Herb", "A herb used in the concoction of various potions.")
            player.inventory.add_item(mystic_herb, quantity=6)
            print("You gain 50 gold and 6 Mystic Herbs.")
            player.echo_cavern_completed = True

            input("\nPress Enter to continue...")
            clear_console()
            confront_illusionary_monster(player)
        else:
            print("The alcove is empty, as you've already taken its treasures.")
            input("\nPress Enter to continue...")
            clear_console()
            echoing_cavern(player)
    else:
        print("You lose your way in the echoes. After some wandering, you find yourself back at the cavern entrance.")
        input("\nPress Enter to continue...")
        clear_console()
        echoing_cavern(player)




def confront_illusionary_monster(player):
    clear_console()
    print("As you continue down the passageway, an Illusionary Monster that's been lurking in the shadows appears in front of you.\n")

    print("A monstrous figure materializes before you, its form shifting and changing. It speaks in a deep, echoing voice.")
    print("'Mortal, before you can proceed, you must answer my questions. Your answers will determine your fate.'\n")

    alignment_score = 0

    questions = [
        {"question": "Do you believe in sacrificing a few for the greater good? (Y/N)\n", "good": "n", "evil": "y"},
        {"question": "Is it acceptable to steal to feed a starving family? (Y/N)\n", "good": "y", "evil": "n"},
        {"question": "Should mercy be shown to those who have wronged others? (Y/N)\n", "good": "y", "evil": "n"},
        {"question": "Is power more important than compassion? (Y/N)\n", "good": "n", "evil": "y"},
        {"question": "Would you betray a friend to gain something of great personal importance? (Y/N)\n", "good": "n", "evil": "y"}
    ]

    for q in questions:
        print(q["question"])
        answer = input("Answer (Y/N): ").lower().strip()
        clear_console()
        if answer == q["good"]:
            alignment_score += 1
        elif answer == q["evil"]:
            alignment_score -= 1

    if alignment_score > 0:
        print("\n'The path of righteousness is yours. Leaders of the human race during the perilous times of ancient often had to make such decisions...' The illusion fades away, revealing the way forward.")
        input("\nPress Enter to enter the Mage's abode...")
        enter_mages_abode(player)
    else:
        print("\n'Your heart harbors darkness. Now, face the consequences of your choices.'")
        input("\nPress Enter to confront the monster...")
        fight_illusionary_monster(player)

def enter_mages_abode(player):
    clear_console()
    print("You step into the Mage's abode, a space filled with mystical energies and arcane artifacts.")
    
    print("\nAn elderly mage, with eyes that hold centuries of wisdom, greets you. 'Ah, the one who has journeyed through the cave. I have indeed been watching your progress.'")
    
    print("\n'The path you've chosen and the choices you've made reveal much about you. It's time for you to learn the art of potion concoction,' the Mage continues.\n")

    health_potion_recipe = Item("Health Potion Recipe", "A recipe for concocting Health Potions using Mystic Herbs.")
    player.inventory.add_item(health_potion_recipe)
    print("\nThe Mage hands you a scroll. 'This is the recipe for a basic Health Potion. To create one, you'll need two Mystic Herbs and a Cauldron.'")

    while True:
        print("\nWhat would you like to do?\n")
        print("1. Ask the Mage about the scriptures")
        print("2. Ask who he is")
        print("3. Return")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            clear_console()
            print("The Mage nods solemnly. 'The scriptures you saw tell of the Great Beast Tide, a cataclysm from over 20,000 years ago. It's a reminder of our past failures and the importance of remaining vigilant.'")
            input("\nPress Enter to continue...")
            clear_console()
        elif choice == "2":
            clear_console()
            print("The Mage gives a mysterious smile. 'Who I am is of little consequence. What matters is your journey and the strength you gather along the way. Use your time wisely.'")
            input("\nPress Enter to continue...")
            clear_console()
        elif choice == "3":
            break
        else:
            print("\nInvalid choice. Please enter a valid number.")
            input("\nPress Enter to continue...")

    print("\n'Remember, the path of magic is complex and demanding. Use this knowledge wisely.'")
    input("\nPress Enter to leave the Mage's abode and return to the cave entrance...")
    explore_passages(player)


def fight_illusionary_monster(player):
    from classes import Monster
    monster = Monster("Illusionary Monster", 200, 10, 10, 10, 10)
    fight_monster(player, "Echoing Cavern", monster)





DAMP_CAVE_LOOT = {
    "Damp Moss": {"description": "Common moss with basic alchemical properties.", "chance": 40},
    "Flickering Crystal Shard": {"description": "A dimly glowing crystal shard.", "chance": 25},
    "Cave Pearl": {"description": "A rare and beautiful pearl formed in cave pools.", "chance": 15},
    "Ancient Bone Fragment": {"description": "A fragment of bone from an ancient creature.", "chance": 10},
    "Glowing Mushroom": {"description": "A rare mushroom that emits a soft light.", "chance": 4},
    "Ethereal Stone": {"description": "A stone shimmering with otherworldly energy.", "chance": 1},
    "Fossilised Bone": {"description": "A bone from an ancient creature, long extinct.", "chance": 10}
}










