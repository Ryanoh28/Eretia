from misc.utilities import clear_console
import random
from colorama import Style, Fore
from prettytable import PrettyTable
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class ReadableItem(Item):
    def __init__(self, name, description, potion_type):
        super().__init__(name, description)
        self.potion_type = potion_type

    def use(self, player):
        print(f"\nYou read the {self.name}.")
        player.known_potions[self.potion_type] = True
        print(f"\nThe knowledge of concocting {self.potion_type} sinks in, and the item disappears from your inventory.")
        player.inventory.remove_items(self.name, 1)


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
        
class FishingRod(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
class MageStaff(Item):
    def __init__(self):
        super().__init__("Mage Staff", "A mystical staff used by mages to channel magical energy.")

class Rune(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

def gain_concoction_experience(player, xp_gained):
    player.concoction_experience += xp_gained
    print(f"\n{player.name} gained {xp_gained} concoction experience points.")

    while player.concoction_experience >= 100 + (10 * (player.concoction_level - 1)):
        player.concoction_experience -= 100 + (10 * (player.concoction_level - 1))
        player.concoction_level += 1
        print(f"\nCongratulations! Your concoction level is now {player.concoction_level}.")


class Cauldron(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def use(self, player):
        clear_console()
        print("Would you like to concoct a potion? (Y/N): \n")
        choice = input().lower().strip()
        if choice == 'y':
            clear_console()
            self.concoct_potion(player)

    def concoct_potion(self, player):
        potion_options = self.get_available_potions(player)
        if not potion_options:
            print("\nYou do not have the knowledge or ingredients to concoct any potions.")
            
            return

        print("Choose a potion to concoct:\n")
        for i, potion in enumerate(potion_options, 1):
            print(f"{i}. {potion['name']}")

        choice = input("\nEnter your choice, or 'Q' to return: ").lower().strip()
        clear_console()
        if choice.isdigit() and 1 <= int(choice) <= len(potion_options):
            selected_potion = potion_options[int(choice) - 1]
            self.create_potion(selected_potion, player)
        elif choice == 'q':
            return
        else:
            print("\nInvalid choice.")

    def get_available_potions(self, player):
        available_potions = []
        if player.known_potions.get("Health Potion") and player.inventory.count_item("Simple Herb") >= 5:
            available_potions.append({
                "name": "Health Potion",
                "ingredients": {"Simple Herb": 5},
                "potion_class": HealthPotion,
                "xp": 5
            })

        if player.known_potions.get("Mana Potion") and player.inventory.count_item("Simple Herb") >= 3 and player.inventory.count_item("Moonflower Seed") >= 1:
            available_potions.append({
                "name": "Mana Potion",
                "ingredients": {"Simple Herb": 3, "Moonflower Seed": 1},
                "potion_class": ManaPotion,
                "xp": 8
            })

        return available_potions

    def create_potion(self, potion_info, player):
        for ingredient, quantity in potion_info["ingredients"].items():
            player.inventory.remove_items(ingredient, quantity)
        potion = potion_info["potion_class"]()
        player.inventory.add_item(potion)
        player.concoction_experience += potion_info["xp"]
        gain_concoction_experience(player, potion_info["xp"])
        print(f"\nYou successfully concocted a {potion_info['name']}! You gained {potion_info['xp']} concoction experience points.")
        




class Pickaxe(Item):
    def __init__(self, name, description, boost):
        super().__init__(name, description)
        self.boost = boost


class HealthPotion:
    def __init__(self):
        self.name = "Health Potion"
        self.description = "A potion that restores health."
        self.healing_amount = 50

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
        self.description = "A potion that restores mana."
        self.mana_amount = 50

    def use(self, target):
        if target.mana < target.max_mana:
            mana_restore_amount = min(self.mana_amount, target.max_mana - target.mana)
            target.regain_mana(mana_restore_amount)
            print(f"{target.name} uses {self.name} and restores {mana_restore_amount} mana.")
            return True
        else:
            print(f"{target.name}'s mana is already full. Cannot use {self.name}.")
            return False
class EnergyPotion:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, target):
        target.energy += 500
        print(f"\n{target.name}'s energy has been increased by 500!")
        return True


class EnchantedFruit(Item):
    def __init__(self, name, description, experience):
        super().__init__(name, description)
        self.experience = experience

    def use(self, target):
        target.gain_experience(self.experience)
        print(f"{target.name} consumes the {self.name}.")
        return True  

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




def display_status(player):
    
    if player.health > 75:
        health_color = Fore.GREEN
    elif 40 < player.health <= 75:
        health_color = Fore.YELLOW
    else:
        health_color = Fore.RED

    
    status = (
        f"Status: Health: {health_color}{player.health}{Style.RESET_ALL} | "
        f"Energy: {player.energy} | Mana: {player.mana} | "
        f"Gold: {player.gold} | Level: {player.level} | "
        f"Experience: {player.experience}/{player.experience_required}\n"
    )

    print(status)
class Inventory:
    def __init__(self):
        self.items = {}
        self.equipment = []
        self.items_per_page = 10

    def equip_armour(self, player):
        clear_console()
        print("Available Armour:")
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

            if player.armour:  
                player.defence -= player.armour.defense_boost
            player.armour = selected_armour
            player.defence += selected_armour.defense_boost  

            input(f"\n{player.name} equipped {selected_armour.name}.\n")
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")
 
  
    def equip_weapon_from_inventory(self, player):
        clear_console()
        print("Available Weapons:")
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

            if player.weapon:
                print(f"\n{player.name} unequipped {player.weapon.name} and placed it back into the inventory.\n")
                self.equipment.append(player.weapon)

            player.weapon = selected_weapon
            self.equipment.remove(selected_weapon) 
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
        if item_name in self.items and self.items[item_name]['quantity'] >= count:
            self.items[item_name]['quantity'] -= count
            if self.items[item_name]['quantity'] <= 0:
                del self.items[item_name]
            return True
        else:
            return False
    


 

    def add_equipment(self, equipment):
        self.equipment.append(equipment)
        

    def remove_equipment(self, equipment):
        if equipment in self.equipment:
            self.equipment.remove(equipment)

    def add_item(self, item, quantity=1, print_confirmation=True, found_quantity=1):
    
        if isinstance(item, dict):
            item_name = item.get('name', 'Unknown')
        else:
            item_name = item.name

        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'object': item, 'quantity': quantity}

        if print_confirmation:
            if found_quantity > 1:
                print(Fore.LIGHTBLUE_EX + f"Added {item_name} ({found_quantity}) to inventory" + Style.RESET_ALL)
            else:
                print(Fore.LIGHTBLUE_EX + f"Added {item_name} to inventory" + Style.RESET_ALL)


    
    def show_equipment(self, player):
        table = PrettyTable()
        table.field_names = ["Slot", "Equipped Item", "Stats"]

        if player.weapon:
            weapon = player.weapon
            table.add_row(["Weapon", weapon.name, f"Extra Damage: {weapon.extra_damage}, Critical Hit Bonus: {weapon.crit_chance_bonus}"])
        else:
            table.add_row(["Weapon", "No weapon equipped", ""])

        table.add_row(["---", "---", "---"])

        if player.armour:
            armour = player.armour
            table.add_row(["Armour", armour.name, f"Defense Boost: {armour.defense_boost}"])
        else:
            table.add_row(["Armour", "No armour equipped", ""])

        print(table)


        
    
    def show_inventory(self, page=1):
        if not hasattr(self, 'items_per_page'):
            self.items_per_page = 10  # Set a default value if not already set

        if not self.items:
            print("\nYour inventory is empty.\n")
            return

        # Calculate total pages
        total_items = len(self.items)
        total_pages = (total_items - 1) // self.items_per_page + 1

        # Validate page number
        if page > total_pages or page < 1:
            print(f"\nInvalid page number. Please enter a number between 1 and {total_pages}.\n")
            return

        # Determine items for the current page
        start_index = (page - 1) * self.items_per_page
        end_index = start_index + self.items_per_page
        current_page_items = list(self.items.items())[start_index:end_index]

        # Create and print the table for current page
        table = PrettyTable()
        table.field_names = ["#", "Item Name", "Quantity"]

        for index, (item_name, item_info) in enumerate(current_page_items, start_index + 1):
            quantity = item_info['quantity']
            table.add_row([index, item_name.title(), quantity])

        print("================ Inventory =================")
        print(table)
        print(f"\nPage {page} of {total_pages}\n")

        # Optionally, add navigation instructions here
        # For example: print("Enter 'next' to go to the next page, 'prev' to go to the previous pag
    
    # def show_inventory(self):
    #     if not self.items:
    #         print("\nYour inventory is empty.\n")
    #     else:
    #         print("================ Inventory =================")

    #         table = PrettyTable()
    #         table.field_names = ["#", "Item Name", "Quantity"]

    #         for index, (item_name, item_info) in enumerate(self.items.items(), 1):
    #             quantity = item_info['quantity']
    #             table.add_row([index, item_name.title(), quantity])

    #         print(table)



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

        next_level_exp_mining = 100 + (10 * (player.mining_level - 1))
        print(f"Mining Level: {player.mining_level} (Exp: {player.mining_experience}/{next_level_exp_mining})")
        next_level_exp_horticulture = 100 + (10 * (player.horticulture_level - 1))
        print(f"Horticulture Level: {player.horticulture_level} (Exp: {player.horticulture_experience}/{next_level_exp_horticulture})")
        next_level_exp_fishing = 100 + (10 * (player.fishing_level - 1))
        print(f"Fishing Level: {player.fishing_level} (Exp: {player.fishing_experience}/{next_level_exp_fishing})")
        next_level_exp_concoction = 100 + (10 * (player.concoction_level - 1))
        print(f"Concoction Level: {player.concoction_level} (Exp: {player.concoction_experience}/{next_level_exp_concoction})")

        print("====================\n")


        input("\nPress Enter to return...")

    
    
    def equipment_menu(self, player):
        while True:
            clear_console()
            print("========================== Equipped Items ===========================")
            self.show_equipment(player)
            print("========================== Equipment Menu ===========================")
            
            print("\n1. Equip Weapon")
            print("2. Equip Armour")
            print("3. View All Equipment")
            print("4. Back")

            choice = input("\nEnter your choice: ").strip()

            if choice == '1':
                self.equip_weapon_from_inventory(player)
            elif choice == '2':
                self.equip_armour(player)
            elif choice == '3':
                self.view_all_equipment(player)
            elif choice == '4' or choice == 'q':
                break
            else:
                print("Invalid choice. Please enter a valid number.")
                input("\nPress enter to continue...")


    
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
        current_page = 1
        while True:
            clear_console()
            display_status(player)
            self.show_inventory(page=current_page)

            #self.show_equipment(player)

            print("1. Use Item")
            print("2. Equipment Menu")
            print("3. View Stats and Skills")
            print("4. View Logbook")
            print("5. Next Page")
            print("6. Previous Page")
            print("7. Back")

            inventory_choice = input("\nWhat would you like to do? ").strip()

            if inventory_choice == '1':
                self.use_item_interface(player)
            elif inventory_choice == '2':
                self.equipment_menu(player)
            elif inventory_choice == '3':
                self.show_skill_stats(player)
            elif inventory_choice == '4':
                player.view_logbook()
            elif inventory_choice == '5':
                current_page += 1
            elif inventory_choice == '6':
                if current_page > 1:
                    current_page -= 1
            elif inventory_choice == '7' or inventory_choice == 'q':
                break
            else:
                print("Invalid choice. Please enter a valid option.")



 
    def use_item_interface(self, player):
        while True:
            clear_console()
            self.show_inventory()
            print("============================================\n")
            
            item_choice = input("\nEnter the number of the item you want to use or 'Q' to return: \n").lower().strip()

            if item_choice in ['b', 'back', 'q']:
                clear_console()
                return False  
            else:
                try:
                    choice_index = int(item_choice) - 1
                    if self.use_item(choice_index, player):
                        input("\nPress Enter to continue...")
                        clear_console()
                        return True  
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


    def use_item(self, index, target):
        item_list = list(self.items.keys())
        if 0 <= index < len(item_list):
            item_name = item_list[index]
            item = self.items[item_name]['object']

            if hasattr(item, 'use'):
                if item.use(target):  
                    self.remove_items(item_name, 1)  
                    
                    return True
                else:
                    
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

