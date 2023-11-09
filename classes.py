import random
from items import Inventory
from camp import Potion
class Human:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.inventory = Inventory()
        self.health = 100  # Default max health for all humans

    def lose_health(self, damage):
        self.health -= damage
        self.health = round(self.health, 1)  
        if self.health <= 0:
            self.dead()
        else:
            print(f"{self.name} lost {damage} health and now has {self.health} health.\n")

    def dead(self):
        self.alive = False
        print(f"{self.name} is dead.\n")

class Warrior(Human):
    def __init__(self, name):
        super().__init__(name)
        self.strength = 5
        self.speed = 5
        self.defense = 5
        self.attack = 5
        self.max_health = 100
        self.level = 1
        self.experience = 0
        self.in_combat = False
        self.gold = 0

    def training_strength(self):
        self.strength += 2
        print(f"{self.name}'s training increased strength by 2 points to {self.strength}.\n")
    
    def special_attack(self, target):
        damage = self.strength * self.attack * 1  
        print(f"{self.name} used a strong attack and dealt {damage} damage.\n")
        target.lose_health(damage)  

    def normal_attack(self, target):
        damage_multiplier = random.uniform(0.7, 1.0)  # Random damage multiplier between 0.7 and 1.0
        damage = self.strength * self.attack * damage_multiplier
        rounded_damage = round(damage, 1)  
        print(f"{self.name} used a normal attack and dealt {rounded_damage} damage.\n")
        target.lose_health(rounded_damage)  
        return rounded_damage  

    def regain_health(self, healing):
        self.health += healing
        if self.health > self.max_health:
            self.health = self.max_health
        self.health = round(self.health, 1)  
        print(f"{self.name} regained {healing} health and now has {self.health} health.\n")

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} gained {amount} experience points.\n")
        if self.experience >= 100:
            print(f"{self.name} has enough experience to level up. Speak to the camp captain!\n")

    def check_level_up(self):
        while self.experience >= 100:  # Level up for every 100 experience points
            self.experience -= 100
            self.level += 1
            print(f"{self.name} has leveled up! You are now level {self.level}.\n")
            self.increase_stats()

    def increase_stats(self):
        
        self.strength += 1
        self.speed += 1
        self.defense += 1
        self.attack += 1
        self.max_health += 10
        self.health = self.max_health  # Restore health to new max health
        print(f"{self.name}'s strength, speed, defense, and attack have increased!\n")

    def spend_gold(self, amount):
        if self.gold >= amount:
            self.gold -= amount
            print(f"{self.name} spent {amount} gold.")
            return True
        else:
            print(f"{self.name} does not have enough gold.")
            return False
        
    def check_if_alive(self):
        if self.health <= 0:
            self.dead()
            return False
        else:
            return True
        
class Monster:
    def __init__(self, name, health=60):
        self.alive = True
        self.name = name
        self.health = health
        self.strength = random.randint(1, 8)
        self.speed = random.randint(1, 8)
        self.defense = random.randint(1, 8)
        self.attack = random.randint(1, 8)

    def dead(self):
        self.alive = False

    def check_if_alive(self):
        if self.health <= 0 and self.alive:  # Check if the monster is alive before declaring it dead
            self.dead()
            return False
        else:
            return True

    def monster_attack(self, target):
        damage = self.strength * self.attack * 0.7
        rounded_damage = round(damage, 1)  
        print(f"{self.name} used a normal attack and dealt {rounded_damage} damage to {target.name}.\n")
        target.lose_health(rounded_damage)  
        return rounded_damage  

    def lose_health(self, damage):
        self.health -= damage
        self.health = round(self.health, 1)  
        if self.health <= 0:
            self.dead()

class Shop:
    def __init__(self):
        
        self.items_for_sale = {
            'health potion': (10, Potion("Health Potion", "A potion that restores 50 health.", 50))
        }

    def display_items(self):
        print("Items for sale:")
        for item_name, (price, _) in self.items_for_sale.items():
            print(f"{item_name.title()} - {price} Gold")

    def buy_item(self, player, item_name):
        if item_name in self.items_for_sale:
            price, item = self.items_for_sale[item_name]
            if player.gold >= price:
                player.gold -= price
                player.inventory.add_item(item)
                print(f"You have purchased a {item_name} for {price} Gold.")
            else:
                print("You do not have enough Gold to buy this item.")
        else:
            print("Item not found.")
