from utilities import clear_console
from classes import Monster

class Spell:
    def __init__(self, name, mana_cost, rune_type, effect, potency):
        self.name = name
        self.mana_cost = mana_cost
        self.rune_type = rune_type
        self.effect = effect
        self.potency = potency

    def cast(self, player, target):
        if player.mana >= self.mana_cost and player.inventory.has_item(self.rune_type):
            print(f"Casting {self.name}...")
            player.consume_mana(self.mana_cost)
            player.inventory.remove_items(self.rune_type, 1)
            self.effect(player, target, self.potency)
            input("\nPress Enter to continue...")
            clear_console()
        else:
            if player.mana < self.mana_cost:
                print("Not enough Mana to cast this spell.")
            else:
                print(f"Missing {self.rune_type} rune.")
            input("\nPress Enter to continue...")
            clear_console()

def heal_spell_effect(player, _, potency):
    player.regain_health(potency)
    print(f"You have been healed for {potency} HP.")

def damage_spell_effect(player, target, potency):
    if isinstance(target, Monster):
        target.monster_lose_health(potency)
        print(f"Spell hits {target.name} for {potency} damage.")



lowspells = {
    "Earth Healing": Spell("Earth Healing", 25, "Earth Rune", heal_spell_effect, 25),
    "Water Bolt": Spell("Water Bolt", 25, "Water Rune", damage_spell_effect, 10),
    "Fire Blast": Spell("Fire Blast", 25, "Fire Rune", damage_spell_effect, 15)
}

def spell_menu(player, target):
    clear_console()
    has_staff = player.inventory.has_item("Mage Staff")

    if not has_staff:
        print("You need a Mage Staff to cast spells.")
        input("\nPress Enter to continue...")
        clear_console()
        return None

    print(f"Current Mana: {player.mana}/{player.max_mana}")
    print("Available Spells:\n")

    # Determine which spell list to use based on player level
    if player.level >= 10:
        available_spells = [spell for spell in highspells.values() if player.inventory.has_item(spell.rune_type)]
    else:
        available_spells = [spell for spell in lowspells.values() if player.inventory.has_item(spell.rune_type)]

    for index, spell in enumerate(available_spells, 1):
        print(f"{index}. {spell.name} (Mana Cost: {spell.mana_cost}, Rune: {spell.rune_type})")

    print("\nEnter the number of the spell you want to cast or (B)ack to return.")

    while True:
        choice = input("\nEnter your choice: ").lower().strip()

        if choice in ['b', 'back']:
            clear_console()
            return None

        try:
            choice_index = int(choice) - 1
            if choice_index < 0 or choice_index >= len(available_spells):
                raise ValueError
            selected_spell = available_spells[choice_index]

            
            if selected_spell in highspells.values() and player.level < 10:
                print("You need to be at least level 10 to cast this spell.")
                input("\nPress Enter to continue...")
                clear_console()
                continue

            clear_console()  
            return selected_spell
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")
            input("\nPress Enter to continue...")
            clear_console()



def stone_skin_effect(player, _, potency):
    duration = 2  
    player.increase_defence_temporarily(potency, duration)
    player.stone_skin_turns_remaining = duration
    print("Stone Skin coveres your body granting you extra protection.")

def tidal_wave_effect(player, target, potency):
    
    if isinstance(target, Monster):
        target.monster_lose_health(potency)
        print(f"Tidal Wave hits {target.name} for {potency} damage.")

def inferno_effect(player, target, potency):
    
    if isinstance(target, Monster):
        target.monster_lose_health(potency)
        print(f"Inferno engulfs {target.name}, dealing {potency} damage.")

# Dictionary of high-level spells
highspells = {
    "Stone Skin": Spell("Stone Skin", 25, "Earth Rune", stone_skin_effect, 12),
    "Tidal Wave": Spell("Tidal Wave", 35, "Water Rune", tidal_wave_effect, 30),
    "Inferno": Spell("Inferno", 60, "Fire Rune", inferno_effect, 40)
}