from items import Inventory, Potion
from utilities import clear_console
from classes import Shop

def return_to_camp(player, shop):
    print("\nYou are back at the camp. What would you like to do?\n")
    while True:
        choice = input("(T)rain, (S)hop, (C)onverse with the captain, (R)est, or (L)eave camp? ").lower()
        clear_console()

        if choice == "t":
            player.training_strength()
        elif choice == "r":
            player.regain_health(20)  # Regenerate 20 health points
            print(f"\nYou have rested and regenerated health. Current health: {player.health}.\n")
        elif choice == "c":
            converse_with_camp_captain(player)
        elif choice == "s":
            shop = Shop()
            shop.display_items()
            item_choice = input("Enter the name of the item you would like to buy: ").lower()
            shop.buy_item(player, item_choice)

        elif choice == "l":
            print("\nYou leave the camp ready to encounter another monster.\n")
            break  # Exit the camp loop to go to combat
        
        else:
            print("\nInvalid choice. Please enter 'T' to train, 'C' to converse, 'R' to rest, or 'L' to leave camp.\n")

def post_combat_options(player):
    leave_choice = input("Would you like to (C)ontinue fighting, (R)eturn to camp, or check (I)nventory? ").lower()
    if leave_choice == "r":
        player.in_combat = False
    elif leave_choice == "c":
        print("\nYou prepare to encounter another monster.\n")
    elif leave_choice == "i":
        manage_inventory(player)
    else:
        print("Invalid choice. Please enter 'C' to continue, 'R' to return, or 'I' to check inventory.\n")

def manage_inventory(player):
    while True:
        
        player.inventory.show_inventory(player)
        item_choice = input("Choose an item to use or type '(B)ack' to return: \n").lower()

        if item_choice in ['b', 'back']:
            clear_console()
            print("Returning to previous options.\n")
            break
        else:
            used = player.inventory.use_item(item_choice, player)
            if used:
                break  
            else:
                clear_console()
                print("\nYou don't have that item. Try again or type '(B)ack' to return.\n")

def converse_with_camp_captain(player):
    level_ups = 0  
    while player.experience >= 100:  
        player.level += 1
        player.experience -= 100  
        level_ups += 1  
        player.increase_stats()  
    
    if level_ups > 0:
        clear_console()
        print(f"\nCamp Captain: \"Congratulations, {player.name}! Your hard work has paid off and you've been granted {level_ups} {'level' if level_ups == 1 else 'levels'}. You are now level {player.level}.\"\n")
    else:
        clear_console()
        print(f"\nCamp Captain: \"You're not ready to level up yet, {player.name}. Keep fighting to gain more experience!\"\n")

def meet_camp_captain(player):
    clear_console()
    print("\nAs you enter the camp, the captain approaches you with a stern look.")
    print(f"Camp Captain: 'Ah, {player.name}, the one who seeks glory in battle! Before you head into the fray, take this Health Potion. You'll need it if you're to survive the dangers that lie ahead.'\n")
    
    health_potion = Potion("Health Potion", "A potion that restores 50 health.", 50)
    player.inventory.add_item(health_potion)
    print(f"Camp Captain: 'Remember, use it wisely, and don't hesitate to return should you need more supplies or assistance.'\n")




