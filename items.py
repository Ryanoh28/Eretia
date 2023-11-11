from utilities import clear_console
import random
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

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
            
            for item_name, count in item_count.items():
                print(f"- {item_name} ({count})")


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
            inventory_choice = input("\nEnter the name of the item you want to use or (B)ack: ").lower().strip()

            if inventory_choice in ['b', 'back']:
                clear_console()  # Clear the console before returning
                return
            elif inventory_choice:
                item_used = self.use_item(inventory_choice, player)
                if item_used:
                    pass
                #print(f"\n{inventory_choice.title()} used successfully.\n")
                else:
                    print("\nItem not found. Try again or type '(B)ack' to return.\n")
                input("Press Enter to continue...")  
            else:
                print("No item name entered. Please enter a valid item name.")

            clear_console()
            print(f"\nInventory: {player.health} Health | {player.gold} Gold\n")



    def use_item(self, item_name, target):
        item_name = item_name.lower()
        matching_items = [item for item in self.items if item_name in item.name.lower()]

        if len(matching_items) == 0:
            print("Item not found in inventory.")
            return False
        else:
            
            item = matching_items[0]
            return self.use_specific_item(item, target)


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
    "Gilded Feather": {"description": "A shiny feather with mystical properties.", "chance": 100},
    "Enchanted Stone": {"description": "A stone radiating magical energy.", "chance": 100}
}

def get_loot_drop():
    # Randomly pick one item to roll for
    chosen_item_name = random.choice(list(LOOT_ITEMS.keys()))
    chosen_item_data = LOOT_ITEMS[chosen_item_name]

    # Roll for the chosen item
    if random.randint(1, 100) <= chosen_item_data["chance"]:
        return [Item(chosen_item_name, chosen_item_data["description"])]
    
    return []

