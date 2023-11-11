#classes.py
import random
from items import Inventory, Potion, Item
from utilities import clear_console
import time
class Human:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.inventory = Inventory()
        self.health = 100  # Default max health for all humans

    def lose_health(self, damage, attacker_strength):
        effective_damage = max(0, damage - (self.defense - attacker_strength))
        self.health -= effective_damage
        self.health = round(self.health, 1)

        if effective_damage > 0:
            print(f"{self.name}'s defense negated some of the damage from the attack!")
        else:
            print(f"{self.name} could not negate any damage from the attack.")

        print(f"{self.name} lost {effective_damage} health and now has {self.health} health.")

        if self.health <= 0:
            self.defeated()
            if self.health <= 0:
                self.defeated()  # Handle the defeat of the player
            else:
                print(f"{self.name} lost {effective_damage} health and now has {self.health} health.\n")


    def defeated(self):
        self.alive = False
        

class Warrior(Human):
    def __init__(self, name):
        super().__init__(name)
        self.last_training_time = 0
        self.training_cooldown = 3600  # Cooldown in seconds (1 hour)
        self.strength = 2
        self.speed = 2
        self.defense = 2
        self.attack = 2
        self.max_health = 100
        self.level = 1
        self.experience = 0
        self.in_combat = False
        self.gold = 0
        self.choice = None

    def training_strength(self):
        current_time = time.time()
        if current_time - self.last_training_time >= self.training_cooldown:
            self.strength += 2
            print(f"{self.name}'s training increased strength by 2 points to {self.strength}.\n")
            self.last_training_time = current_time
        else:
            remaining_time = self.training_cooldown - (current_time - self.last_training_time)
            print(f"Cannot train yet. Please wait for {int(remaining_time)} seconds.\n")
    
    def special_attack(self, target):
        damage = self.strength * self.attack * 1  
        print(f"{self.name} used a strong attack and dealt {damage} damage.\n")
        target.lose_health(damage)  

    def normal_attack(self, target):
    # Initial attack
        damage = self.calculate_attack_damage()
        target.lose_health(damage)
        print(f"{self.name} used a normal attack and dealt {damage} damage.")

    # Check for extra attack based on speed
        if self.speed >= target.speed * 2:
            extra_damage = self.calculate_attack_damage()
            target.lose_health(extra_damage)
            print(f"{self.name} uses their swift speed to attack again, dealing {extra_damage} damage.")
    
    def calculate_attack_damage(self):
        # This method calculates the damage based on strength, attack stat, and random factor
        damage_multiplier = random.uniform(0.7, 1.0)
        damage = self.strength * self.attack * damage_multiplier
        return round(damage, 1)

    def regain_health(self, healing):
        self.health += healing
        if self.health > self.max_health:
            self.health = self.max_health
        self.health = round(self.health, 1)  
        #print(f"{self.name} regained {healing} health and now has {self.health} health.\n")

    def gain_experience(self, amount):
        self.experience += amount
        print(f"\n{self.name} gained {amount} experience points.\n")
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
            clear_console()
            print(f"{self.name} spent {amount} gold.")
            return True
        else:
            print(f"{self.name} does not have enough gold.")
            return False
        
    def check_if_alive(self):
        if self.health <= 0:
            self.defeated()
            return False
        else:
            return True
    
    def handle_player_defeat(self, shop):
        clear_console()
        print(f"{self.name} has been defeated.\n")  
        self.health = self.max_health * 0.5  # Regain 50% of max health
        self.alive = True  # Reset the alive status to True
        print(f"{self.name} stumbled back to camp after being defeated.")
        print(f"{self.name} has regained 50% of their health.")  
        from camp import return_to_camp
        return_to_camp(self, shop)  


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
        alive_status = self.health > 0
        #print(f"Debug: {self.name} is alive: {alive_status}")  # Debug print
        return alive_status


    def monster_attack(self, target):
        damage = self.strength * self.attack * 0.7
        rounded_damage = round(damage, 1)  
        print(f"{self.name} attacked and dealt {rounded_damage} damage to {target.name}.\n")
        return rounded_damage  # Return the damage for further processing in the combat function


    def lose_health(self, damage):
        self.health -= damage
        self.health = round(self.health, 1)
        #print(f"Debug: {self.name}'s health is now {self.health}.")  # Debug print
        if self.health <= 0:
            self.dead()


class Shop:
    def __init__(self):
        self.items_for_sale = {
            'health potion': {'price': 10, 'object': Potion("Health Potion", "A potion that restores 50 health.", 50)},
        }
        self.item_value = {
            "Gilded Feather": 6, 
            "Enchanted Stone": 20,
            "Health Potion": 5
        }

    def display_items_for_sale(self, player):
        clear_console()
        print("Items for sale:\n")
        for item_name, item_info in self.items_for_sale.items():
            print(f"{item_name.title()}: {item_info['price']} gold")
        print("\nEnter the name of the item you would like to buy or press (Q) to go back.")
        item_choice = input().lower().strip()
        if item_choice != 'q':
            self.buy_item(player, item_choice)

    def buy_item(self, player, partial_item_name):
        if partial_item_name.lower() == 'q':
            return

        matching_items = self.find_item_by_partial_name(partial_item_name)

        if not matching_items:
            print("\nItem not found.")
        elif len(matching_items) == 1:
            item_name, item_info = next(iter(matching_items.items()))
            price = item_info['price']
            item = item_info['object']
            if player.gold >= price:
                player.spend_gold(price)
                player.inventory.add_item(item)
                print(f"\n{item_name.title()} has been added to your inventory\n")
            else:
                print("\nYou do not have enough Gold to buy this item.")
        else:
            print("\nMultiple items found. Please be more specific:")
            for item_name in matching_items:
                print(f"- {item_name.title()}")

        input("\nPress Enter to continue...")
        self.shop_menu(player)
    
    def find_item_by_partial_name(self, partial_name):
        partial_name_lower = partial_name.lower()
        matches = {name: item for name, item in self.items_for_sale.items() if partial_name_lower in name.lower()}
        return matches
    
    def shop_menu(self, player):
        while True:
            clear_console()
            print("Welcome to the Camp Shop!\n")
            print("Choose an option:\n")
            print("1. View items to buy")
            print("2. Sell items")
            print("\n(B)ack")

            choice = input("\nEnter your choice: ").lower()

            if choice in ['1', 'view', 'buy']:
                self.display_items_for_sale(player)
            elif choice in ['2', 'sell']:
                self.sell_items_interface(player)
            elif choice in ['b', 'back']:
                clear_console()  
                break  
            else:
                print("Invalid choice. Please try again.")

    def sell_items_interface(self, player):
        while True:
            clear_console()
            print("\nItems you can sell:")
            for item in player.inventory.items:
                sale_price = self.item_value.get(item.name, 0)
                print(f"- {item.name}: {sale_price} gold")

            print("\nType the name of the item you want to sell or (B)ack to return.")
            item_name_input = input("\nEnter item name: ").lower()

            if item_name_input in ['b', 'back']:
                clear_console()  
                break  
            else:
                self.sell_item(player, item_name_input)


    def sell_partial_match_item(self, player, partial_item_name):
        matching_items = [item for item in player.inventory.items if partial_item_name in item.name.lower()]

        if len(matching_items) == 0:
            print("\nItem not found in inventory. Please try again.\n")
        elif len(matching_items) == 1:
            self.sell_item(player, matching_items[0].name)
        else:
            print("\nMultiple items found. Please be more specific:")
            for item in matching_items:
                print(f"- {item.name}")

        input("Press Enter to continue...")

    def sell_item(self, player, partial_item_name):
        matching_items = [item for item in player.inventory.items if partial_item_name in item.name.lower()]
        if not matching_items:
            print("\nItem not found in inventory. Please try again.\n")
        else:
            item = matching_items[0]
            sale_price = self.item_value.get(item.name, 0)
            player.gold += sale_price
            player.inventory.items.remove(item)
            print(f"\nSold {item.name} for {sale_price} gold.\n")

        input("Press Enter to continue...")

