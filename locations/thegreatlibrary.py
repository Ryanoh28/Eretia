from utilities import clear_console

def visit_great_library(player):
    while True:
        clear_console()
        print("Welcome to the Great Library of Eretia!\n")
        print("Here, you can find knowledge about the world and its history.\n")
        print("1. Explore Floor 1 - History of Eretia")
        print("2. Explore Floor 2 - Known Monsters")
        print("3. Return to the Western Path")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            explore_floor_one(player)
        elif choice == "2":
            explore_floor_two(player)
        elif choice == "3":
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 3.")
            input("\nPress Enter to continue...")

def explore_floor_one(player):
    while True:
        clear_console()
        print("Floor 1: The History of Eretia")
        print("\nChoose a book to read:\n")
        print("1. Eretia Before the Storm")
        print("2. The Great Beast Tide")
        print("3. Heroes of Eretia")
        print("4. Return to the Library Entrance")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            read_eretia_before_the_storm(player)
        elif choice == "2":
            read_great_beast_tide(player)
        elif choice == "3":
            heroes_of_eretia_submenu(player)
        elif choice == "4":
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")
            input("\nPress Enter to continue...")

def heroes_of_eretia_submenu(player):
    while True:
        clear_console()
        print("Heroes of Eretia")
        print("\nChoose a hero's story to read:\n")
        print("1. Duke Beirut")
        print("2. Sylas Willow")
        print("3. Kaelen the Swift")
        print("4. Bronn Ironheart")
        print("5. Lyra Starwhisper")
        print("6. Return to Floor 1")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            read_duke_beirut(player)
        elif choice == "2":
            read_sylas_willow(player)  
        elif choice == "3":
            read_kaelen_the_swift(player)  
        elif choice == "4":
            read_bronn_ironheart(player)  
        elif choice == "5":
            read_lyra_starwhisper(player)  
        elif choice == "6":
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")
            input("\nPress Enter to continue...")

def explore_floor_two(player):
    while True:
        clear_console()
        print("Welcome to Floor 2 of the Great Library: Known Monsters\n")
        print("Select a region to explore its monsters, or learn about the history of the monsters:\n")
        print("1. Monsters of The Dark Forest")
        print("2. Monsters of The Damp Cave")
        print("3. Monsters of The Border")
        print("4. Monsters of The Northern Hills")
        print("5. The Left Behind")
        print("6. Return to the Main Hall")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice in ["1", "2", "3", "4"]:
            region = ["Dark Forest", "Damp Cave", "The Border", "Northern Hills"][int(choice)-1]
            clear_console()
            print(f"Monsters of {region}:\n")
            for monster, lore in monster_lore[region].items():
                print(f"{monster}: {lore}\n")
            input("Press Enter to return to the list of regions...")
        elif choice == "5":
            clear_console()
            print("The Left Behind:\n")
            print("In the annals of Eretia's history, the Great Beast Tide stands as a pivotal event. During this calamity, myriad monstrous beings surged from the depths of the unknown, leaving destruction in their wake. However, not all creatures partook in this onslaught. Some remained hidden, lurking in the shadows of the Dark Forest, the dampness of the Damp Cave, and the chill of the Northern Hills. Over the centuries, these creatures evolved into the native monsters now encountered west of The Border.")
            print("\nIt's crucial to note the stark contrast in the danger these creatures pose compared to their counterparts beyond The Border. The monsters of The Border and beyond are vastly more formidable, a testament to the harsh and unforgiving lands they inhabit.")
            input("\nPress Enter to return to the list of regions...")
        elif choice == "6" or choice == "q":
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")
            input("\nPress Enter to continue...")



def read_eretia_before_the_storm(player):
    clear_console()
    print("Eretia Before the Storm")
    print("\nIn the age before the Great Beast Tide, Eretia was a realm of unparalleled beauty and tranquillity. The land, lush and fertile, was a mosaic of blooming meadows, dense forests, and crystal-clear rivers. Majestic mountains stood guard at the borders of Eretia, their peaks touching the sky.")
    
    print("\nNations within Eretia lived in harmonious balance. Kingdoms, large and small, thrived under the rule of just and benevolent leaders. Disputes were rare and resolved through dialogue and mutual respect. People from different realms often gathered for grand festivals, celebrating the unity and diversity of their cultures.")
    
    print("\nAgriculture was the cornerstone of Eretian prosperity. The land, blessed by the gods, yielded bountiful harvests. Farmers and druids worked in harmony, ensuring that nature's balance was maintained. The Great Library, a symbol of Eretian wisdom, was a beacon of knowledge, attracting scholars from distant lands to study its vast collection of tomes and scrolls.")
    
    print("\nMagic, a gift bestowed upon the Eretians by celestial beings, was used for healing, enhancing crop growth, and protecting the lands. Mages were revered and formed councils that advised the rulers, ensuring peace and prosperity prevailed across Eretia.")
    
    print("\nThis era of peace, however, was not to last. Unbeknownst to the Eretians, a darkness was brewing at the edges of their world, a prelude to the calamity that would be known as the Great Beast Tide.")
    
    input("\nPress Enter to return to Floor 1...")

def read_great_beast_tide(player):
    clear_console()
    print("The Great Beast Tide")
    print("\nAs you open the book, you find that crucial pages are missing or damaged, making the text unreadable.")
    input("\nPress Enter to return to Floor 1...")

def read_duke_beirut(player):
    clear_console()
    print("Heroes of Eretia - Duke Beirut")
    print("\nDuke Beirut, a revered hero of Eretia, played a pivotal role during the Great Beast Tide.")
    print("Known for his bravery and strength, he drove a large group of monsters away from the Northern Hills.")
    print("His actions paved the way for the construction of Border Town. Legend says that after the war, he ventured beyond the border for adventure and never returned.")
    input("\nPress Enter to return to Floor 1...")

def read_sylas_willow(player):
    clear_console()
    print("Heroes of Eretia - Sylas Willow")
    print("\nSylas Willow, known as the 'Beacon of Hope', was a human mage whose mastery over healing and protective magics was unparalleled. In the darkest days of the Great Beast Tide, his powers shone brightest.")
    
    print("\nDuring the Siege of Elderglen, as the monstrous horde threatened to overrun the city, Sylas erected a barrier of light that held back the tide long enough for civilians to evacuate. Weakened but resolute, he then ventured into the fray, healing the wounded and reviving the fallen.")
    
    print("\nIn the Battle of Crimson Fields, Sylas stood alone against a fearsome Dark Leviathan. With a wave of his staff, he banished the creature, but not before it struck a mortal blow. As he lay dying, his final spell healed dozens of Eretian soldiers, turning the tide of the battle.")
    
    print("\nSylas Willow's sacrifice became a symbol of the ultimate price paid for Eretia's survival. His legacy lives on in the hearts of all who cherish peace and valour.")
    input("\nPress Enter to return to Floor 1...")

def read_kaelen_the_swift(player):
    clear_console()
    print("Heroes of Eretia - Kaelen the Swift")
    print("\nKaelen, an elf renowned for his unmatched speed and archery, earned his title 'the Swift' through feats that seemed almost supernatural. His arrows were said to weave through battlefields, finding their marks with deadly precision.")
    
    print("\nDuring the Siege of Silverpine, Kaelen climbed the highest tower and held off waves of flying monstrosities. His arrows never missed, and his actions saved countless lives. But as the battle raged, a shadowy dragon descended upon the tower. Kaelen fought valiantly, his arrows piercing the beast's hide, but the dragon's fiery breath engulfed him. His sacrifice allowed the city's defenders to rally and eventually win the day.")
    
    print("\nKaelen's memory is honoured by all Eretians, a testament to the belief that one person's courage can turn the tide of battle.")
    input("\nPress Enter to return to Floor 1...")

def read_bronn_ironheart(player):
    clear_console()
    print("Heroes of Eretia - Bronn Ironheart")
    print("\nBronn Ironheart, a dwarven warrior of immense strength and indomitable will, stood as a bastion of hope amidst despair. His battle-axe, forged in the deepest furnaces of the Iron Mountains, felled beasts by the dozens.")
    
    print("\nAt the Battle of Molten Pass, Bronn held the line against an onslaught of creatures. Alone on the bridge, he fought tirelessly, his axe a blur of steel. Though eventually overcome by sheer numbers, his stand allowed hundreds of civilians to escape.")
    
    print("\nBronn's legacy lives on, inspiring songs of bravery and strength in the face of overwhelming odds.")
    input("\nPress Enter to return to Floor 1...")

def read_lyra_starwhisper(player):
    clear_console()
    print("Heroes of Eretia - Lyra Starwhisper")
    print("\nLyra Starwhisper, a sorceress of great renown, wielded the arcane arts with a grace and power that few could match. Her command of elemental magic was unparalleled, a beacon of hope in the darkest hours of the Great Beast Tide.")

    print("\nDuring the direst moment of the siege on the Great Library, where ancient knowledge was threatened by the encroaching beasts, Lyra stood as the last line of defence. She summoned a vortex of wind and lightning, creating a barrier that no beast could penetrate.")

    print("\nAs the monstrous tide battered against her spell, Lyra's strength waned. With a final, defiant cry, she unleashed all her magical energy, obliterating the attackers but also dissipating her own form. The tempest she conjured was so potent that not a single creature could approach the Library, but it cost Lyra her physical existence.")

    print("\nLyra Starwhisper's sacrifice is etched in the annals of Eretia, remembered as the selfless act of a guardian who saved the repository of centuries of knowledge. Her spirit is said to linger in the arcane halls of the Great Library, forever entwined with the magic she so dearly loved.")
    input("\nPress Enter to return to Floor 1...")


# Monster Lore
monster_lore = {
    "Dark Forest": {
        "Dark Forest Wolf": "Fabled for their shadowy fur, these wolves move silently in the dark, making them formidable predators.",
        "Forest Ape": "These apes are known for their intelligence and strength, often using tools and working in groups.",
        "Shadow Stalker": "A ghostly presence in the forest, it's said they can become invisible in the shadows.",
        "Mystic Owlbeast": "Wise and mystical creatures, rumoured to possess ancient knowledge.",
        "Thorned Lurker": "Camouflaged amongst the thorny undergrowth, they ambush unsuspecting prey.",
        "Whispering Wraith": "Spirits of the forest, their whispers are often heard but seldom seen."
    },
    "Damp Cave": {
        "Cave Bat": "These large bats use echolocation to navigate the pitch-black caves.",
        "Grey Slime": "An amorphous creature, absorbing anything it touches.",
        "Rock Troll": "Sturdy as the rocks they live amongst, they are fearsome when provoked.",
        "Luminous Fungoid": "A bioluminescent fungus creature, illuminating the caves with a ghostly light.",
        "Echo Serpent": "Known for their hypnotic hissing that echoes through the caves.",
        "Crystaline Beetle": "Their hardened crystal shells are as beautiful as they are tough."
    },
    "The Border": {
        "Blighted Sentinel": "Guardians corrupted by dark magic, they now attack anyone approaching the Border.",
        "Feral Shadehound": "Shadowy canines that roam the Border, their eyes glowing with malice.",
        "Ravaged Harpy": "Once beautiful, now twisted creatures with a screeching cry.",
        "Corrupted Ent": "These ents have turned malevolent, their branches now weapons.",
        "Nightmare Wisp": "Floating orbs of light that lead travellers to their doom.",
        "Barren Drake": "Dragons stripped of their fiery breath, wandering the wastelands of the Border."
    },
    "Echoing Cavern": {
        "Illusionary Monster": "A mysterious creature that can take the form of a traveller's deepest fear."
    },
    "Northern Hills": {
        "Frost-Feathered Eagle": "Majestic birds with icy feathers, their cry as cold as the wind.",
        "Stonehide Boar": "Boars with skin as tough as stone, charging at anything that moves.",
        "Gale Howler Wolf": "Wolves that hunt in the fierce winds of the hills, howling hauntingly.",
        "Hill Serpent": "Giant serpents that slither through the hills, their presence sensed but seldom seen.",
        "Mist Wraith": "Ethereal beings that glide through the fog, enveloping their prey.",
        "Hill Hound": "Sturdy and loyal, these hounds are both feared and respected by the locals."
    }
}





