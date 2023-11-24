import random


monster_names = {
    "Dark Forest": [
        "Dark Forest Wolf", 
        "Forest Ape", 
        "Shadow Stalker", 
        "Mystic Owlbeast",   
        "Thorned Lurker",    
        "Whispering Wraith"  
    ],
    "Damp Cave": [
        "Cave Bat", 
        "Grey Slime", 
        "Rock Troll", 
        "Luminous Fungoid",  
        "Echo Serpent",      
        "Crystaline Beetle"  
    ],
    "The Border": [
        "Blighted Sentinel", 
        "Feral Shadehound", 
        "Ravaged Harpy", 
        "Corrupted Ent", 
        "Nightmare Wisp", 
        "Barren Drake"
    ],
    "Northern Hills": [
        "Frost-Feathered Eagle", 
        "Stonehide Boar", 
        "Gale Howler Wolf", 
        "Hill Serpent", 
        "Mist Wraith",
        "Hill Hound"
    ]
}

def generate_mission():
    monster_areas = list(monster_names.keys())
    kill_count = random.randint(2, 14)
    monster_area = random.choice(monster_areas)

    # Select a random monster from the chosen area
    monster_name = random.choice(monster_names[monster_area])

    mission = {
        "monster": monster_name,
        "area": monster_area,
        "required_kills": kill_count,
        "gold_reward": kill_count * 20,
        "current_kills": 0
    }

    return mission

def accept_mission(player, mission):
    if len(player.logbook['missions']) < 3:
        player.logbook['missions'].append(mission)
        print(f"Mission accepted: {mission['monster']} in {mission['area']} ({mission['required_kills']} kills).")
    else:
        print("You can only accept up to 3 missions at a time.")

def complete_mission(player, mission):
    if mission['current_kills'] >= mission['required_kills']:
        player.gold += mission['gold_reward']
        print(f"Mission completed! Earned {mission['gold_reward']} gold.")
        player.logbook['missions'].remove(mission)
    else:
        print("Mission not yet completed.")
