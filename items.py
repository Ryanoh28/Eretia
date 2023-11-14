from utilities import clear_console
import random
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Weapon:
    def __init__(self, name, extra_damage, crit_chance_bonus):
        self.name = name
        self.extra_damage = extra_damage
        self.crit_chance_bonus = crit_chance_bonus


class Potion(Item):
    def __init__(self, name, description, healing_amount):
        super().__init__(name, description)
        self.healing_amount = healing_amount

    def use(self, target):
        if target.health < target.max_health:
            target.regain_health(self.healing_amount)
            #print(f"\n{target.name} uses {self.name} and restores {self.healing_amount} health")
            return True
        else:
            return False

class Inventory:
    def __init__(self):
        self.items = []
        self.equipment = []

    def count_item(self, item_name):
        return sum(1 for item in self.items if item.name == item_name)
    
    def remove_items(self, item_name, count):
        removed_count = 0
        for item in reversed(self.items):
            if item.name == item_name and removed_count < count:
                self.items.remove(item)
                removed_count += 1
    
    def equip_weapon_from_inventory(self, player):
        clear_console()
        print("Available Weapons:")
        # Display list of weapons in player's inventory
        weapon_list = [item for item in player.inventory.items if isinstance(item, Weapon)]
        for index, weapon in enumerate(weapon_list, 1):
            print(f"{index}. {weapon.name}")

        weapon_choice = input("\nEnter the number of the weapon to equip or (B)ack: ").lower().strip()
        if weapon_choice in ['b', 'back']:
            return

        try:
            choice_index = int(weapon_choice) - 1
            if choice_index < 0 or choice_index >= len(weapon_list):
                raise ValueError
            selected_weapon = weapon_list[choice_index]
            player.weapon = selected_weapon
            print(f"\n{player.name} equipped {selected_weapon.name}.\n")
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")
        input("\nPress Enter to continue...")

    def unequip_weapon(self, player):
        clear_console()
        if player.weapon:
            print(f"Unequipping {player.weapon.name}.")
            player.available_weapons.append(player.weapon)  # Add the unequipped weapon back to available weapons
            player.weapon = None
        else:
            print("You have no weapon equipped.")
        input("\nPress Enter to continue...")
 

    def add_equipment(self, equipment):
        self.equipment.append(equipment)

    def remove_equipment(self, equipment):
        if equipment in self.equipment:
            self.equipment.remove(equipment)

    
    def add_item(self, item, print_confirmation=True):
        self.items.append(item)
        if print_confirmation:
            print(f"Added {item.name} to inventory\n")

    def show_equipment(self, player):
        
        if player.weapon:
            weapon = player.weapon
            print(f"Equipped Weapon: {weapon.name}")
            print(f"  - Extra Damage: {weapon.extra_damage}")
            print(f"  - Critical Hit Bonus: {weapon.crit_chance_bonus}")
        else:
            print("No weapon equipped.")
        
    
    def show_inventory(self):
        if not self.items:
            print("\nYour inventory is empty\n")
        else:
            item_count = {}
            for item in self.items:
                item_name = item.name
                item_count[item_name] = item_count.get(item_name, 0) + 1
            
            for index, (item_name, count) in enumerate(item_count.items(), 1):
                print(f"{index}. {item_name} ({count})")

    def show_skill_stats(self, player):
        clear_console()
        print("=== Combat Stats ===")
        print(f"Strength: {player.strength}")
        print(f"Speed: {player.speed}")
        print(f"Defense: {player.defense}")
        print("====================\n")

        print("=== Skill Stats ===")
        print(f"Mining Level: {player.mining_level} (Exp: {player.mining_experience}/100)")
        # Add other skills here as needed
        print("====================\n")

        input("\nPress Enter to return...")
    
    

    def inventory_menu(self, player):
        while True:
            clear_console()
            print(f"\nInventory: {player.health} Health | {player.gold} Gold | {player.energy} Energy\n")

            print("==== Inventory ====")
            self.show_inventory()
            print("====================\n")

            print("==== Equipment ====")
            self.show_equipment(player)
            print("====================\n")

            print("1. Use Item")
            print("2. View Equipment")
            print("3. Equip Weapon")
            print("4. Unequip Weapon")
            print("5. View Stats and Skills")
            print("(B)ack")

            inventory_choice = input("\nWhat would you like to do? ").strip()

            if inventory_choice == '1':
                self.use_item_interface(player)
            elif inventory_choice == '2':
                self.view_equipment(player)
            elif inventory_choice == '3':
                self.equip_weapon_interface(player)
            elif inventory_choice == '4':
                self.unequip_weapon(player)
            elif inventory_choice == '5':
                self.show_skill_stats(player)
            elif inventory_choice in ['b', 'back']:
                clear_console()
                break
            else:
                print("Invalid choice. Please enter a valid option.")



    def use_item_interface(self, player):
        while True:
            clear_console()
            print("==== Inventory ====")
            self.show_inventory()
            print("====================\n")
            
            item_choice = input("\nEnter the number of the item you want to use or (B)ack: ").lower().strip()

            if item_choice in ['b', 'back']:
                break  # Break the inner loop to go back to the main inventory menu
            else:
                try:
                    choice_index = int(item_choice) - 1
                    self.use_item(choice_index, player)
                    input("\nPress Enter to continue...")
                except ValueError:
                    print("Invalid choice. Please enter a valid number or 'B' to go back.")
                except IndexError:
                    print("Item not found. Try again or type 'B' to go back.")
    
    def equip_weapon_interface(self, player):
        clear_console()
        print("=== Available Weapons ===")
        if player.available_weapons:
            for index, weapon in enumerate(player.available_weapons, 1):
                print(f"{index}. {weapon.name}")
            choice = input("\nChoose a weapon to equip or (B)ack: ").lower().strip()
            if choice in ['b', 'back']:
                return
            else:
                try:
                    choice_index = int(choice) - 1
                    selected_weapon = player.available_weapons[choice_index]
                    if player.weapon:
                        print(f"You already have {player.weapon.name} equipped. Unequip it first.")
                    else:
                        player.equip_weapon_for_warrior(selected_weapon)
                        print(f"\nEquipped {selected_weapon.name}.")
                except (ValueError, IndexError):
                    print("Invalid choice. Please enter a valid number.")
                except IndexError:
                    print("Weapon not found. Try again.")
        else:
            print("No available weapons to equip.")
        input("\nPress Enter to continue...")


    def view_equipment(self, player):
        clear_console()
        print("==== Equipment ====")

        # Display the equipped weapon
        if player.weapon:
            weapon = player.weapon
            print(f"Equipped Weapon: {weapon.name}")
            print(f"  - Extra Damage: {weapon.extra_damage}")
            print(f"  - Critical Hit Bonus: {weapon.crit_chance_bonus}")
        else:
            print("No weapon equipped.")

        # Display unequipped weapons
        print("\nAvailable Weapons:")
        if player.available_weapons:
            for weapon in player.available_weapons:
                print(f"- {weapon.name} (Damage: {weapon.extra_damage}, Crit: {weapon.crit_chance_bonus})")
        else:
            print("No additional weapons available.")

        # Armours etc later
        

        print("=================\n")
        input("\nPress Enter to continue...")


    def use_item(self, index, target):
        item_list = [item for item in self.items]
        if index >= 0 and index < len(item_list):
            item = item_list[index]
            if isinstance(item, Potion):
                if target.health < target.max_health:  
                    item.use(target)
                    self.items.remove(item)
                    print(f"Used {item.name}.")
                    return True
                else:
                    print(f"\n{target.name}'s health is already full. Cannot use {item.name}.")
                    return False
            else:
                print(f"You can't use {item.name} in this way.")
                return False
        else:
            print("Item not found in inventory.")
            return False



    def use_specific_item(self, item, target):
        if isinstance(item, Potion):
            if target.health < target.max_health:  
                item.use(target)
                self.items.remove(item)
                print(f"Used {item.name}.")
                return True
            else:
                print(f"\n{target.name}'s health is already full. Cannot use {item.name}.")
                return False
        else:
            print(f"You can't use {item.name} in this way.")
            return False


    def manage_inventory(player):
        print(f"\nInventory: {player.health} Health | {player.gold} Gold\n")
        
        while True:
            player.inventory.show_inventory()
            input("Press Enter to continue...")  
            clear_console()

            print(f"\nInventory: {player.health} Health | {player.gold} Gold\n")
            item_choice = input("Enter the name of the item you want to use or type '(B)ack' to return: \n").lower()

            if item_choice in ['b', 'back']:
                break
            else:
                used = player.inventory.use_item(item_choice, player)
                if used:
                    pass
                    #print(f"\n{item_choice.title()} used successfully.\n")
                else:
                    print("\nYou don't have that item. Try again or type '(B)ack' to return.\n")
                
                input("Press Enter to continue...")

            clear_console()
    
    # Loot Items
LOOT_ITEMS = {
    "Gilded Feather": {"description": "A shiny feather with mystical properties.", "chance": 20},
    "Enchanted Stone": {"description": "A stone radiating magical energy.", "chance": 10},  
    "Twilight Shard": {"description": "A small crystal that glows with the light of the setting sun.", "chance": 5}

}

def get_loot_drop():
    if random.randint(1, 100) <= 30:  # 30% chance for any loot to drop
        cumulative_chance = 0
        roll = random.randint(1, 100)
        for item_name, item_info in LOOT_ITEMS.items():
            cumulative_chance += item_info["chance"]
            if roll <= cumulative_chance:
                return [Item(item_name, item_info["description"])]
    return []  # No loot drops

def get_location_loot(loot_table):
    total_chance = 100  
    roll = random.randint(1, total_chance)

    cumulative_chance = 0
    for name, info in loot_table.items():
        cumulative_chance += info["chance"]
        if roll <= cumulative_chance:
            return Item(name, info["description"])
    
    return None