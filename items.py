from utilities import clear_console
import random
from colorama import Style, Fore

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description




class EyeOfInsight(Item):
    def __init__(self):
        super().__init__("Eye of Insight", "A mystical artifact that reveals the true nature of your foes.")

    def use(self, monster):
        print(f"\nUsing {self.name}...\n")
        print(f"Monster Name: {monster.name}")
        print(f"Strength: {monster.strength}")
        print(f"Speed: {monster.speed}")
        print(f"Defence: {monster.defence}")
        input("Press enter to continue...")
        

class MageStaff(Item):
    def __init__(self):
        super().__init__("Mage Staff", "A mystical staff used by mages to channel magical energy.")

class Rune(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
class Cauldron(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def use(self, player):
        print("\nWould you like to concoct a potion? (Y/N): ")
        choice = input().lower().strip()
        if choice == 'y':
            self.concoct_potion(player)

    def concoct_potion(self, player):
        if "Health Potion Recipe" in [item.name for item in player.inventory.items]:
            if player.inventory.count_item("Mystic Herb") >= 2:
                # Remove ingredients and add potion
                player.inventory.remove_items("Mystic Herb", 2)
                health_potion = HealthPotion()  # Creating an instance of HealthPotion
                player.inventory.add_item(health_potion)
                print("\nYou successfully concocted a Health Potion!")
            else:
                print("\nYou don't have enough Mystic Herbs to concoct a Health Potion.")
        else:
            print("\nYou do not have the required recipe to concoct a potion.")
        input("\nPress Enter to continue...")

class Pickaxe(Item):
    def __init__(self, name, description, boost):
        super().__init__(name, description)
        self.boost = boost


class HealthPotion:
    def __init__(self):
        self.name = "Health Potion"
        self.description = "A potion that restores 25 health."
        self.healing_amount = 25

    def use(self, target):
        if target.health < target.max_health:
            heal_amount = min(self.healing_amount, target.max_health - target.health)
            target.regain_health(heal_amount)
            print(f"{target.name} uses {self.name} and restores {heal_amount} health.")
            return True
        else:
            print(f"{target.name}'s health is already full. Cannot use {self.name}.")
            return False

class ManaPotion:
    def __init__(self):
        self.name = "Mana Potion"
        self.description = "A potion that restores 25 mana."
        self.mana_amount = 25

    def use(self, target):
        if target.mana < target.max_mana:
            mana_restore_amount = min(self.mana_amount, target.max_mana - target.mana)
            target.regain_mana(mana_restore_amount)
            print(f"{target.name} uses {self.name} and restores {mana_restore_amount} mana.")
            return True
        else:
            print(f"{target.name}'s mana is already full. Cannot use {self.name}.")
            return False


class EnchantedFruit(Item):
    def __init__(self, name, description, experience):
        super().__init__(name, description)
        self.experience = experience

    def use(self, target):
        target.gain_experience(self.experience)
        print(f"{target.name} consumes the {self.name}.")
        return True  # Indicate that the use was successful


class EnergyPotion:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, player):
        player.energy = 500
        print(f"\n{player.name}'s energy has been boosted to 500!")



class Bedroll(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def use_bedroll(self, target):
        health_regain = 75
        energy_regain = 75
        target.regain_health(health_regain)
        target.regain_energy(energy_regain)
        print(f"{target.name} uses the {self.name}, regaining {health_regain} health and {energy_regain} energy.")
        input("\nPress enter to continue...")
        return True


class Armour:
    def __init__(self, name, description, defense_boost):
        self.name = name
        self.description = description
        self.defense_boost = defense_boost

class Weapon:
    def __init__(self, name, description, extra_damage, crit_chance_bonus):
        self.name = name
        self.description = description
        self.extra_damage = extra_damage
        self.crit_chance_bonus = crit_chance_bonus

class Inventory:
    def __init__(self):
        self.items = {}
        self.equipment = []

    def equip_armour(self, player):
        clear_console()
        print("Available Armour:")
        # Display list of armours in player's inventory
        armour_list = [item for item in self.equipment if isinstance(item, Armour)]
        for index, armour in enumerate(armour_list, 1):
            print(f"{index}. {armour.name}")

        armour_choice = input("\nEnter the number of the armour to equip or (Q) to return: ").lower().strip()
        if armour_choice in ['b', 'back', 'q']:
            return

        try:
            choice_index = int(armour_choice) - 1
            if choice_index < 0 or choice_index >= len(armour_list):
                raise ValueError
            selected_armour = armour_list[choice_index]

            if player.armour:  # Unequip current armour if any
                player.defence -= player.armour.defense_boost
            player.armour = selected_armour
            player.defence += selected_armour.defense_boost  # Increase defence stat

            print(f"\n{player.name} equipped {selected_armour.name}.\n")
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")

    def unequip_armour(self, player):
        clear_console()
        if player.armour:
            print(f"Unequipping {player.armour.name}.")
            player.defence -= player.armour.defense_boost  # Decrease defence stat
            self.equipment.append(player.armour)  # Add the unequipped armour back to equipment
            player.armour = None
        else:
            print("You have no armour equipped.")
        input("\nPress Enter to continue...")

  
    def equip_weapon_from_inventory(self, player):
        clear_console()
        print("Available Weapons:")
        # Display list of weapons in player's inventory
        weapon_list = [item for item in self.equipment if isinstance(item, Weapon)]
        for index, weapon in enumerate(weapon_list, 1):
            print(f"{index}. {weapon.name}")

        weapon_choice = input("\nEnter the number of the weapon to equip or (Q) to return: ").lower().strip()
        if weapon_choice in ['b', 'back', 'q']:
            return

        try:
            choice_index = int(weapon_choice) - 1
            if choice_index < 0 or choice_index >= len(weapon_list):
                raise ValueError
            selected_weapon = weapon_list[choice_index]
            player.weapon = selected_weapon
            self.equipment.remove(selected_weapon)  # Remove the equipped weapon from equipment list
            print(f"\n{player.name} equipped {selected_weapon.name}.\n")
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")
        input("\nPress Enter to continue...")

    def unequip_weapon(self, player):
        clear_console()
        if player.weapon:
            print(f"Unequipping {player.weapon.name}.")
            self.equipment.append(player.weapon)  # Add the unequipped weapon back to equipment list
            player.weapon = None
        else:
            print("You have no weapon equipped.")
        input("\nPress Enter to continue...")
    
    def has_item(self, item_name):
        return item_name in self.items


    def count_item(self, item_name):
        return self.items.get(item_name, {'quantity': 0})['quantity']

    def remove_items(self, item_name, count):
        if item_name in self.items:
            self.items[item_name]['quantity'] -= count
            if self.items[item_name]['quantity'] <= 0:
                del self.items[item_name]
    
    

 

    def add_equipment(self, equipment):
        self.equipment.append(equipment)

    def remove_equipment(self, equipment):
        if equipment in self.equipment:
            self.equipment.remove(equipment)

    
    def add_item(self, item, quantity=1, print_confirmation=True, found_quantity=1):
        item_name = item.name

        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'object': item, 'quantity': quantity}

        if print_confirmation:
            if found_quantity > 1:
                print(Style.BRIGHT + Fore.BLUE + f"Added {item_name} ({found_quantity}) to inventory\n" + Style.RESET_ALL)
            else:
                print(Style.BRIGHT + Fore.BLUE + f"Added {item_name} to inventory\n" + Style.RESET_ALL)


    def show_equipment(self, player):
        print("\n==== Equipment ====")
        
        # Display the equipped weapon
        if player.weapon:
            weapon = player.weapon
            print(f"Equipped Weapon: {weapon.name}")
            print(f"  - Extra Damage: {weapon.extra_damage}")
            print(f"  - Critical Hit Bonus: {weapon.crit_chance_bonus}")
            print()  # Adding a space after the weapon section
        else:
            print("No weapon equipped.\n")  # Ensure there's a space even when no weapon is equipped

        # Display the equipped armor
        if player.armour:
            armour = player.armour
            print(f"Equipped Armour: {armour.name}")
            print(f"  - Defense Boost: {armour.defense_boost}")
        else:
            print("No armour equipped.")

        print("====================")

        
    
    def show_inventory(self):
        if not self.items:
            print("\nYour inventory is empty.\n")
        else:
            print("==== Inventory ====")
            for index, (item_name, item_info) in enumerate(self.items.items(), 1):
                quantity = item_info['quantity']
                print(f"{index}. {item_name} ({quantity})")



    def show_skill_stats(self, player):
        clear_console()
        print("=== Combat Stats ===")
        print(f"Strength: {player.strength}")
        print(f"Speed: {player.speed}")

        # Check for equipped armor and its defense boost
        armor_defense_boost = player.armour.defense_boost if player.armour else 0
        if armor_defense_boost > 0:
            print(f"Defence: {player.defence} " + Fore.GREEN + f"(+{armor_defense_boost})" + Style.RESET_ALL)
        else:
            print(f"Defence: {player.defence}")

        print("====================\n")

        print("=== Skill Stats ===")
        print(f"Mining Level: {player.mining_level} (Exp: {player.mining_experience}/100)")
        print(f"Horticulture Level: {player.horticulture_level} (Exp: {player.horticulture_experience}/100)")

        print("====================\n")

        input("\nPress Enter to return...")

    
    
    def equipment_menu(self, player):
        while True:
            clear_console()
            print("==== Equipment Menu ====")
            print("1. Equip Weapon")
            print("2. Unequip Weapon")
            print("3. Equip Armour")
            print("4. Unequip Armour")
            print("5. View All Equipment")
            print("6. Back")

            choice = input("\nEnter your choice: ").strip()

            if choice == '1':
                self.equip_weapon_from_inventory(player)
            elif choice == '2':
                self.unequip_weapon(player)
            elif choice == '3':
                self.equip_armour(player)
            elif choice == '4':
                self.unequip_armour(player)
            elif choice == '5':
                self.view_all_equipment(player)
            elif choice == '6' or choice == 'q':
                break
            else:
                print("Invalid choice. Please enter a valid number.")
                input("\nPress enter to continue...")

    # def view_all_equipment(self, player):
    #     clear_console()
    #     print("==== All Equipment ====")
    #     if player.weapon:
    #         print(f"Weapon: {player.weapon.name}")
    #     if player.armour:
    #         print(f"Armour: {player.armour.name}")
    #     if not player.weapon and not player.armour:
    #         print("No equipment available.")
    #     input("\nPress enter to continue...")
    
    def view_all_equipment(self, player):
        clear_console()
        print("==== All Equipment ====")

        if player.weapon:
            print(f"Equipped Weapon: {player.weapon.name}")
        else:
            print("No weapon equipped.")

        if player.armour:
            print(f"Equipped Armour: {player.armour.name}")
        else:
            print("No armour equipped.")

        print("\nAvailable Weapons:")
        unequipped_weapons = [item for item in self.equipment if isinstance(item, Weapon) and item != player.weapon]
        if unequipped_weapons:
            for weapon in unequipped_weapons:
                print(f"- {weapon.name}")
        else:
            print("No additional weapons available.")

        print("\nAvailable Armours:")
        unequipped_armours = [item for item in self.equipment if isinstance(item, Armour) and item != player.armour]
        if unequipped_armours:
            for armour in unequipped_armours:
                print(f"- {armour.name}")
        else:
            print("No additional armours available.")

        print("====================")
        input("\nPress enter to continue...")


    
    def inventory_menu(self, player):
        while True:
            clear_console()
            print(f"Status: {player.health} Health | {player.energy} Energy | {player.mana} Mana | {player.gold} Gold | Level: {player.level} | Experience: {player.experience}/{player.experience_required}\n")
            self.show_inventory()  

            self.show_equipment(player)  

            print("1. Use Item")
            print("2. Equipment Menu")
            print("3. View Stats and Skills")
            print("4. View Logbook")
            print("5. Back")  

            inventory_choice = input("\nWhat would you like to do? ").strip()

            if inventory_choice == '1':
                self.use_item_interface(player)
            elif inventory_choice == '2':
                self.equipment_menu(player) 
            elif inventory_choice == '3':
                self.show_skill_stats(player)
            elif inventory_choice == '4':
                player.view_logbook()
            elif inventory_choice == '5' or inventory_choice == 'q':
                break
            else:
                print("Invalid choice. Please enter a valid option.")



 
    def use_item_interface(self, player):
        while True:
            clear_console()
            
            self.show_inventory()
            print("====================\n")
            
            item_choice = input("\nEnter the number of the item you want to use or (B)ack: ").lower().strip()

            if item_choice in ['b', 'back', 'q']:
                clear_console()  # Clear console when going back to combat
                break  # Break the inner loop to go back to the main inventory menu
            else:
                try:
                    choice_index = int(item_choice) - 1
                    if self.use_item(choice_index, player):
                        input("\nPress Enter to continue...")
                    else:
                        input("\nPress Enter to continue...")
                except ValueError:
                    print("Invalid choice. Please enter a valid number or 'B' to go back.")
                    input("\nPress Enter to continue...")
                except IndexError:
                    print("Item not found. Try again or type 'B' to go back.")
                    input("\nPress Enter to continue...")

    
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
        #input("\nPress Enter to continue...")


    # #def view_equipment(self, player):
    #     clear_console()
    #     print("==== Equipment ====")

    #     # Display the equipped weapon
    #     if player.weapon:
    #         weapon = player.weapon
    #         print(f"Equipped Weapon: {weapon.name}")
    #         print(f"  - Extra Damage: {weapon.extra_damage}")
    #         print(f"  - Critical Hit Bonus: {weapon.crit_chance_bonus}")
    #     else:
    #         print("No weapon equipped.")

    #     # Display unequipped weapons
    #     print("\nAvailable Weapons:")
    #     if player.available_weapons:
    #         for weapon in player.available_weapons:
    #             print(f"- {weapon.name} (Damage: {weapon.extra_damage}, Crit: {weapon.crit_chance_bonus})")
    #     else:
    #         print("No additional weapons available.")

    #     # Armours etc later
        

        # print("=================\n")
        # input("\nPress Enter to continue...")

    def use_item(self, index, target):
        item_list = list(self.items.keys())
        if 0 <= index < len(item_list):
            item_name = item_list[index]
            item = self.items[item_name]['object']

            if hasattr(item, 'use'):
                if item.use(target):  # Check if the use was successful
                    self.remove_items(item_name, 1)  # Remove one item after successful use
                    #print(f"Used {item.name}.")
                    return True
                else:
                    #print(f"Cannot use {item.name}.")
                    return False




    def manage_inventory(player):
        print(f"\nInventory: {player.health} Health | {player.gold} Gold\n")
        
        while True:
            player.inventory.show_inventory()
            input("Press Enter to continue...")  
            clear_console()

            print(f"\nInventory: {player.health} Health | {player.gold} Gold\n")
            item_choice = input("Enter the name of the item you want to use or type '(B)ack' to return: \n").lower()

            if item_choice in ['b', 'back', 'q']:
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
    "Gilded Feather": {"name": "Gilded Feather", "description": "A shiny feather with mystical properties.", "chance": 20},
    "Enchanted Stone": {"name": "Enchanted Stone", "description": "A stone radiating magical energy.", "chance": 10},
    "Twilight Shard": {"name": "Twilight Shard", "description": "A small crystal that glows with the light of the setting sun.", "chance": 5},
    "Earth Rune": {"name": "Earth Rune", "object": Rune("Earth Rune", "A rune embodying the essence of Earth."), "chance": 15},
    "Water Rune": {"name": "Water Rune", "object": Rune("Water Rune", "A rune embodying the essence of Water."), "chance": 15},
    "Fire Rune": {"name": "Fire Rune", "object": Rune("Fire Rune", "A rune embodying the essence of Fire."), "chance": 15},
    # ... other items
}

def get_loot_drop():
    if random.randint(1, 100) <= 30:  #30% any loot
        cumulative_chance = 0
        roll = random.randint(1, 100)
        for item_info in LOOT_ITEMS.values():
            cumulative_chance += item_info["chance"]
            if roll <= cumulative_chance:
                if "object" in item_info:
                    return [item_info["object"]]  
                else:
                    
                    return [Item(item_info["name"], item_info["description"])]
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

