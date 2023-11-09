from utilities import clear_console

class Item:
    def __init__(self, name, description, effect=None):
        self.name = name
        self.description = description
        self.effect = effect

class Potion(Item):
    def __init__(self, name, description, healing_amount):
        super().__init__(name, description)
        self.healing_amount = healing_amount

    def use(self, target):
        target.regain_health(self.healing_amount)
        print(f"*{target.name} uses {self.name} and restores {self.healing_amount} health*")

class Inventory:
    def __init__(self):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
        
    def show_inventory(self, player):  
        clear_console()
        print(f"\nInventory: {player.health} Health | {player.gold} Gold\n")  
        if not self.items:
            print("\n*Your inventory is empty*\n")
        else:
            item_count = {}
            for item in self.items:
                item_name = item.name
                item_count[item_name] = item_count.get(item_name, 0) + 1
            
            for item_name, count in item_count.items():
                print(f"- {item_name}: {self.items[0].description} ({count})")
                
    def inventory_menu(self, player):  
        while True:
            clear_console()
            print("\nInventory Menu")
            print(f"Health: {player.health} Health | Gold: {player.gold} Gold\n")
            player.inventory.show_inventory(player)
            inventory_choice = input("\nEnter the name of the item you want to use or (B)ack: ").lower().strip()

            if inventory_choice == 'b':
                return  
            else:
                item_used = player.inventory.use_item(inventory_choice, player)
                if item_used:
                    
                    pass
                else:
                    print("Item not found")
                    pass

    def use_item(self, item_name, target):
        item_name = item_name.lower()
        matching_items = [item for item in self.items if item_name in item.name.lower()]

        if not matching_items:
            print("Item not found in inventory.")
            return False
        elif len(matching_items) > 1:
            print("Multiple items found. Please be more specific:")
            for item in matching_items:
                print(f"- {item.name}: {item.description}")
            return False
        else:
            item = matching_items[0]
            if isinstance(item, Potion):  
                item.use(target)
                self.items.remove(item)
                #print(f"You use {item.name} and restore {item.healing_amount} health.")
                return True
            else:
                print(f"You can't use {item.name} in this way.")
                return False


