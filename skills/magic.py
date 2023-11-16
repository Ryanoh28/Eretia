


class Spell:
    def __init__(self, name, mana_cost, rune_type, effect, potency):
        self.name = name
        self.mana_cost = mana_cost
        self.rune_type = rune_type
        self.effect = effect
        self.potency = potency

    def cast(self, player, target):
        if player.mana >= self.mana_cost and self.rune_type in player.inventory.get_rune_types():
            player.consume_mana(self.mana_cost)
            player.inventory.consume_rune(self.rune_type)
            self.effect(player, target, self.potency)
        else:
            print("Not enough Mana or missing rune to cast this spell.")

def heal_spell_effect(player, _, potency):
    player.regain_health(potency)
    print(f"You have been healed for {potency} HP.")

def damage_spell_effect(player, target, potency):
    target.take_damage(potency)
    print(f"Spell hits {target.name} for {potency} damage.")

# Spell table with low level spells
spells = {
    "Earth Healing": Spell("Earth Healing", 25, "Earth Rune", heal_spell_effect, 25),
    "Water Bolt": Spell("Water Bolt", 25, "Water Rune", damage_spell_effect, 10),
    "Fire Blast": Spell("Fire Blast", 25, "Fire Rune", damage_spell_effect, 15)
}
