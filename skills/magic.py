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


# Spell table with low level spells
spells = {
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

    available_spells = [spell for spell in spells.values() if player.inventory.has_item(spell.rune_type)]
    
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
            clear_console()  # Clear the console after a spell is chosen
            return selected_spell
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")
            input("\nPress Enter to continue...")
            clear_console()
