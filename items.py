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

    def view_equipment(self):
            print("\n=== Equipment ===")
            if self.equipped_weapon:
                print(f"Equipped Weapon: {self.equipped_weapon.name}")
            else:
                print("No weapon equipped.")
            print("=================\n")
    
    def equip_weapon(self, player, weapon_name):
        matching_weapons = [item for item in self.items if isinstance(item, Weapon) and item.name == weapon_name]

        if matching_weapons:
            weapon_to_equip = matching_weapons[0]
            if self.equipped_weapon:
                self.unequip_weapon(player)  

            self.equipped_weapon = weapon_to_equip
            player.equip_weapon(weapon_to_equip)
            self.items.remove(weapon_to_equip)
            print(f"\n{weapon_to_equip.name} has been equipped.\n")
        else:
            print("\nWeapon not found in inventory.\n")

    def unequip_weapon(self, player):
        if self.equipped_weapon:
            self.items.append(self.equipped_weapon)
            print(f"\n{self.equipped_weapon.name} has been unequipped and added back to inventory.\n")
            self.equipped_weapon = None
            player.equip_weapon(None)  


    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item.name} to inventory\n")

    def show_inventory(self):
        if not self.items:
            print("\n*Your inventory is empty*\n")
        else:
            item_count = {}
            for item in self.items:
                item_name = item.name
                item_count[item_name] = item_count.get(item_name, 0) + 1
            
            for index, (item_name, count) in enumerate(item_count.items(), 1):
                print(f"{index}. {item_name} ({count})")

    def inventory_menu(self, player):
        while True:
            clear_console()
            print(f"\nInventory: {player.health} Health | {player.gold} Gold\n")
            print("=== Player Stats ===")
            print(f"Level: {player.level}")
            print(f"Experience: {player.experience}/100")
            print(f"Strength: {player.strength}")
            print(f"Speed: {player.speed}")
            print(f"Defense: {player.defense}")
            print("====================\n")

            self.show_inventory()
            print("\n=== Equipment ===")
            print("Equipped Weapon: " + (player.weapon.name if player.weapon else "None"))
            print("=================\n")

            print("1. Use Item")
            print("2. View Equipment")
            print("3. Equip Weapon")
            print("4. Unequip Weapon")
            print("(B)ack")

            inventory_choice = input("\nWhat would you like to do? ").lower().strip()

            if inventory_choice == '1':
                item_choice = input("\nEnter the number of the item you want to use: ").lower().strip()
                try:
                    choice_index = int(item_choice) - 1
                    self.use_item(choice_index, player)
                except ValueError:
                    print("Invalid choice. Please enter a valid number.")
                except IndexError:
                    print("Item not found. Try again.")
            elif inventory_choice == '2':
                self.view_equipment()
            elif inventory_choice == '3':
                weapon_name = input("\nEnter the name of the weapon to equip: ")
                self.equip_weapon(player, weapon_name)
            elif inventory_choice == '4':
                self.unequip_weapon(player)
            elif inventory_choice in ['b', 'back']:
                clear_console()
                break
            else:
                print("Invalid choice. Please enter a valid option.")

            input("\nPress Enter to continue...")
            clear_console()


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
    "Enchanted Stone": {"description": "A stone radiating magical energy.", "chance": 10}
}

def get_loot_drop():
    # Randomly pick one item to roll for
    chosen_item_name = random.choice(list(LOOT_ITEMS.keys()))
    chosen_item_data = LOOT_ITEMS[chosen_item_name]

    # Roll for the chosen item
    if random.randint(1, 100) <= chosen_item_data["chance"]:
        return [Item(chosen_item_name, chosen_item_data["description"])]
    
    return []

