#classes.py
import random
from items import Inventory, Cauldron, Bedroll, Pickaxe, HealthPotion, ManaPotion, Rune
from utilities import clear_console

class Human:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.inventory = Inventory()
        self.health = 100  # Default max health for all humans

   
    def lose_health(self, damage, attacker_strength):
        damage_reduction = max(0, self.defence - attacker_strength)
        effective_damage = max(1, damage - damage_reduction)  # Ensure minimum damage of 1

        self.health -= effective_damage
        self.health = round(self.health, 1)

        if damage_reduction > 0:
            print("\n=============================================")
            print(f"{self.name}'s defence negated {damage_reduction} points of damage from the attack!")
            print("=============================================")
        print("\n=============================================")
        print(f"{self.name} lost {effective_damage} health and now has {self.health} health.")
        print("=============================================")

        if self.health <= 0:
            self.defeated()
        
    def defeated(self):
        self.alive = False


class Warrior(Human):
    def __init__(self, name):
        super().__init__(name)
        # Initial attributes
        self.current_location = None
        self.energy = 100
        self.weapon = None
        self.available_weapons = []
        self.quests = {}
        self.strength = 2
        self.speed = 2
        self.defence = 2
        self.attack = 2
        self.max_health = 100
        self.level = 1
        self.experience = 0
        self.in_combat = False
        self.gold = 0
        self.choice = None
        self.training_count = 0
        self.search_count = 0
        self.mining_experience = 0
        self.mining_level = 1
        self.echo_cavern_completed = False
        self.flags = set()
        self.mana = 50
        self.max_mana = 50
    
    def regain_energy(self, amount):
        self.energy += amount
        if self.energy > 100:
            self.energy = 100
    
    def can_rest(self):
        return self.health < 100 or self.energy < 100

    def consume_energy(self, amount):
        if self.energy >= amount:
            self.energy -= amount
            #print(f"Used {amount} energy.")
            return True
        else:
            print("Not enough energy!")
            return False

    def consume_mana(self, amount):
        if self.mana >= amount:
            self.mana -= amount
            return True
        else:
            print("Not enough mana!")
            return False
        
    def regain_mana(self, amount):
        self.mana += amount
        if self.mana > 50:  # Assuming 50 is the max mana
            self.mana = 50
        print(f"{self.name} regained {amount} mana.")    

    def regenerate_energy(self, amount=100):  
        self.energy = min(self.energy + amount, 100)
        

    def gain_mining_experience(self, exp):
        self.mining_experience += exp
        print(f"Gained {exp} mining experience.")

        while self.mining_experience >= 100:
            self.mining_experience -= 100
            self.mining_level += 1
            print(f"Congratulations! Your mining level is now {self.mining_level}.")
            
    def equip_weapon_for_warrior(self, selected_weapon):
        if self.weapon is not None:
            print(f"\nYou already have {self.weapon.name} equipped. Unequip it first.")
            return
        if selected_weapon in self.available_weapons:
            self.weapon = selected_weapon  
            self.available_weapons.remove(selected_weapon)  
            #print(f"\n{self.name} equipped {selected_weapon.name}.")
        else:
            print("This weapon is not available to equip.")


    def unequip_weapon(self, player):
        if player.weapon:
            player.unequip_weapon()
            print(f"Unequipped {player.weapon.name}.")
        else:
            print("You have no weapon equipped.")


    def reset_search_count(self):
        self.search_count = 0
        

    def training(self):
        while self.training_count < 3:
            clear_console()
            print("What would you like to train?\n")
            print("1. Strength")
            print("2. Speed")
            print("3. Defence")
            print("4. Return to previous menu\n")

            stat_choice = input("Enter your choice (1-4): ").strip()

            if stat_choice == "1":
                self.strength += 1
                print(f"\n{self.name}'s strength increased to {self.strength}.")
                self.training_count += 1
            elif stat_choice == "2":
                self.speed += 1
                print(f"\n{self.name}'s speed increased to {self.speed}.")
                self.training_count += 1
            elif stat_choice == "3":
                self.defence += 1
                print(f"\n{self.name}'s defence increased to {self.defence}.")
                self.training_count += 1
            elif stat_choice == "4":
                print("\nReturning to previous menu.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

            input("\nPress Enter to continue...") 

        if self.training_count >= 3:
            clear_console()
            print("You have completed your training sessions for this level.")
            input("\nPress Enter to continue...")

    def critical_attack(self, target):
        crit_damage_bonus = self.weapon.extra_damage if self.weapon else 0
        damage = round((self.strength * 2) + crit_damage_bonus, 1)
        weapon_name = self.weapon.name if self.weapon else "fists"
        print("=============================================")
        print(f"{self.name} used a critical attack with {weapon_name} and dealt {damage} damage.")
        print("=============================================")
        target.monster_lose_health(damage)

    def normal_attack(self, target):
        weapon_name = self.weapon.name if self.weapon else "fists"  

        crit_chance = 5  # Base critical hit chance
        if self.weapon:
            crit_chance += self.weapon.crit_chance_bonus

        if random.randint(1, 100) <= crit_chance:
            self.critical_attack(target)
        else:
            base_damage = round(self.strength * random.uniform(1, 1.5), 1)
            total_damage = base_damage + (self.weapon.extra_damage if self.weapon else 0)
            target.monster_lose_health(total_damage)
            print("=============================================")
            print(f"{self.name} used a normal attack with {weapon_name} and dealt {total_damage} damage.")
            print("=============================================")

        if self.speed >= target.speed * 2:
            extra_damage = round(self.strength * random.uniform(1, 1.5), 1)
            extra_damage += self.weapon.extra_damage if self.weapon else 0
            target.monster_lose_health(extra_damage)
            print(f"{self.name} uses their swift speed to attack again with {weapon_name}, dealing {extra_damage} damage.")
            print("=============================================")

    def regain_health(self, healing):
        self.health += healing
        if self.health > self.max_health:
            self.health = self.max_health
        self.health = round(self.health, 1)  
        #print(f"{self.name} regained {healing} health and now has {self.health} health.\n")

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} gained {amount} experience points.\n")

        
        self.check_level_up()


    def check_level_up(self):
        while self.experience >= 100:  
            self.experience -= 100
            self.level += 1
            self.training_count = 0  
            print(f"{self.name} has leveled up! You are now level {self.level}.\n")
            #self.increase_stats()


    def increase_stats(self):
        
        self.strength += 1 
        self.speed += 1
        self.defence += 1
        self.attack += 1
        #self.max_health += 10
        self.health = self.max_health  
        print(f"{self.name}'s strength, speed, defence, and attack have increased!\n")

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
    
    def handle_player_defeat(self):
        clear_console()
        print(f"\n{self.name} has been defeated.\n\n")  
        self.health = self.max_health * 0.5  # Regain 50% of max health
        self.alive = True
        print(f"{self.name} stumbled back to town after being defeated.\n")
        print(f"{self.name} has regained 50% of their health.\n")  
        input("Press Enter to return to town...\n")  
        from bordertown import return_to_border_town
        return_to_border_town(self)



class Monster:
    def __init__(self, name, health, strength_max, speed_max, defence_max, level=1):
        self.alive = True
        self.name = name
        self.level = level
        self.health = health

        # Base stats for the monster's level
        self.strength = 2 + (level - 1)
        self.speed = 2 + (level - 1)
        self.defence = 2 + (level - 1)

        # Simulate training by randomly distributing extra stat points
        for _ in range(level * 2):  # 2 training points per level
            self.add_random_stat_point()
    
    def add_random_stat_point(self):
        stat_choice = random.choice(['strength', 'speed', 'defence'])
        if stat_choice == 'strength':
            self.strength += 1
        elif stat_choice == 'speed':
            self.speed += 1
        elif stat_choice == 'defence':
            self.defence += 1


    

    def dead(self):
        self.alive = False

    def check_if_alive(self):
        alive_status = self.health > 0
        #print(f"Debug: {self.name} is alive: {alive_status}")  # Debug print
        return alive_status
    
    def monster_attack(self, target):
        # First attack
        damage_multiplier = random.uniform(0.8, 1.3)
        damage = self.strength * damage_multiplier
        rounded_damage = max(1, round(damage, 1))  # Ensure minimum damage is 1
        print("\n---------------------------------------------")
        print(f"{self.name} attacked and dealt {rounded_damage} damage to {target.name}.")
        print("---------------------------------------------")
        
        target.lose_health(rounded_damage, self.strength)

        # Check for a second attack based on speed
        if self.speed >= target.speed * 2:
            second_attack_damage = max(1, round(self.strength * damage_multiplier * 0.5, 1))  # 50% damage for the second attack
            print("\n---------------------------------------------")
            print(f"{self.name} uses their swift speed to attack again, dealing {second_attack_damage} damage.")
            print("---------------------------------------------")
            target.lose_health(second_attack_damage, self.strength)
    

    def monster_lose_health(self, damage):
        self.health -= damage
        self.health = round(self.health, 1)
        #print(f"Debug: {self.name}'s health is now {self.health}.")  # Debug print
        if self.health <= 0:
            self.dead()




class Shop:
    def __init__(self):
        self.items_for_sale = {
            'health potion': {'price': 20, 'object': HealthPotion()},
            'mana potion': {'price': 20, 'object': ManaPotion()},
            'cauldron': {'price': 100, 'object': Cauldron("Cauldron", "An iron cauldron for brewing potions.")},
            'bedroll': {'price': 50, 'object': Bedroll("Bedroll", "A durable bedroll for resting outdoors.")},
            'Iron Pickaxe': {'price': 60, 'object': Pickaxe("Iron Pickaxe", "A sturdy pickaxe made of iron. Increases mining efficiency.", 20)}
        }



        
        self.item_value = {
            "Gilded Feather": 6, 
            "Enchanted Stone": 10,
            "Health Potion": 5,
            "Mystic Herb": 3,  
            "Ancient Coin": 5,  
            "Lost Necklace": 10,  
            "Rusted Sword": 5,
            "Blade of Verdant Greens": 15,
            "Tangled Vine": 1,
            "Mossy Pebble": 1,
            "Cracked Pottery Shard": 2,
            "Twilight Shard": 40,
            "Copper Ore": 5,  
            "Tin Ore": 8,
            "Iron Ore": 12,
            "Damp Moss": 2,
            "Flickering Crystal Shard": 4,
            "Cave Pearl": 14,
            "Ancient Bone Fragment": 10,
            "Glowing Mushroom": 30,
            "Ethereal Stone": 100,
            "Stone": 1,
            "Fossilised Bone": 10,
            "Iron Pickaxe": 30,
            "Earth Rune": 25,
            "Water Rune": 25,
            "Fire Rune": 25,
            
        }

    

    def display_items_for_sale(self, player):
        while True:
            clear_console()
            print(f"You have {player.gold} gold.\n")
            print("Items for sale:\n")
            item_list = list(self.items_for_sale.keys())
            for index, item_name in enumerate(item_list, 1):
                price = self.items_for_sale[item_name]['price']
                print(f"{index}. {item_name.title()}: {price} gold")

            
            print("\nEnter the number of the item you would like to buy or press (Q) to go back.")
            choice = input().lower().strip()

            if choice == 'q':
                break  
            else:
                try:
                    choice_index = int(choice) - 1
                    if choice_index < 0 or choice_index >= len(item_list):
                        raise ValueError
                    selected_item_name = item_list[choice_index]
                    self.buy_item(player, selected_item_name)
                except (ValueError, IndexError):
                    print("Invalid choice. Please enter a valid number.")

    def buy_item(self, player, item_name):
        item_info = self.items_for_sale.get(item_name, None)
        if item_info:
            price = item_info['price']
            item = item_info['object']
            try:
                clear_console()
                quantity = int(input(f"How many {item_name}s would you like to buy? Enter quantity: "))
                if quantity < 1:
                    raise ValueError
            except ValueError:
                print("Invalid quantity. Please enter a valid number.")
                return

            total_cost = price * quantity
            if player.gold >= total_cost:
                player.spend_gold(total_cost)
                for _ in range(quantity):
                    player.inventory.add_item(item, print_confirmation=False)
                print(f"\n{quantity} {item_name.title()}(s) have been added to your inventory.\n")
            else:
                print("\nYou do not have enough gold to buy this quantity.")
        else:
            print("\nItem not found.")
        
        input("\nPress Enter to continue...")

    
    def shop_menu(self, player):
        while True:
            clear_console()
            print("Welcome to Border General!\n")
            print("Choose an option:\n")
            print("1. View items to buy")
            print("2. Sell items")
            print("3. Back")

            choice = input("\nEnter your choice: ").lower()

            if choice in ['1', 'view', 'buy']:
                self.display_items_for_sale(player)
            elif choice in ['2', 'sell']:
                self.sell_items_interface(player)
            elif choice in ['3', 'b', 'q']:
                clear_console()  
                break  
            else:
                print("Invalid choice. Please try again.")

    def sell_items_interface(self, player):
        while True:
            clear_console()
            print("Items and Weapons you can sell:\n")
            item_list = []
            item_count = {}

            for item_name, item_info in player.inventory.items.items():
                item_count[item_name] = item_info['quantity']
                item_list.append(item_name)

            for weapon in player.available_weapons:
                item_list.append(weapon.name)
                item_count[weapon.name] = 1  

            for index, item_name in enumerate(item_list, 1):
                sale_price = self.item_value.get(item_name, 0)
                quantity = item_count[item_name]
                print(f"{index}. {item_name} ({quantity}) - {sale_price} gold each")

            print("\nType the number of the item you want to sell or (Q) to return.")
            choice = input("\nEnter your choice: ").lower()

            if choice in ['b', 'back', "q"]:
                clear_console()
                break
            else:
                try:
                    choice_index = int(choice) - 1
                    if choice_index < 0 or choice_index >= len(item_list):
                        raise ValueError
                    selected_item_name = item_list[choice_index]
                    self.sell_item(player, selected_item_name, item_count[selected_item_name])
                except (ValueError, IndexError):
                    print("Invalid choice. Please enter a valid number.")
    
 

    def sell_item(self, player, item_name, available_quantity):
        if available_quantity == 1:
            quantity_to_sell = 1
        else:
            print(f"\nHow many {item_name}s do you want to sell? (Available: {available_quantity}, 'A' for all)")
            choice = input("Enter quantity or 'A': ").lower()

            if choice in ['a', 'all']:
                quantity_to_sell = available_quantity
            else:
                try:
                    quantity_to_sell = int(choice)
                    if quantity_to_sell < 1 or quantity_to_sell > available_quantity:
                        raise ValueError
                except ValueError:
                    print("Invalid quantity. Please enter a valid number.")
                    return

        sale_price = self.item_value.get(item_name, 0)
        total_sale_price = sale_price * quantity_to_sell
        
        # Check if the item is a weapon or a regular item
        if item_name in [weapon.name for weapon in player.available_weapons]:
            # Remove the weapon from available weapons
            for _ in range(quantity_to_sell):
                weapon_to_remove = next(weapon for weapon in player.available_weapons if weapon.name == item_name)
                player.available_weapons.remove(weapon_to_remove)
        else:
            # Decrease the quantity of the item in the inventory
            player.inventory.items[item_name]['quantity'] -= quantity_to_sell
            if player.inventory.items[item_name]['quantity'] <= 0:
                del player.inventory.items[item_name]

        player.gold += total_sale_price
        clear_console()
        print(f"\nSold {quantity_to_sell} {item_name}(s) for {total_sale_price} gold.\n")
        input("Press Enter to continue...")


    
  
    

    
