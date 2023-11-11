from items import Potion
from utilities import clear_console
from locations import enter_dark_forest

def return_to_camp(player, shop):
    while True:
        print("\nYou are back at the camp. What would you like to do?\n")
        choice = input("(T)rain, (L)eave camp, (C)onverse with the captain, (R)est, check (I)nventory, visit the (S)hop, or access the (M)enu: ").lower().strip()
        clear_console()

        if choice == "t":
            #print("*You trained at camp with the recruits*")
            player.training_strength()
        elif choice == "l":
            leave_camp(player, shop)
            break
        elif choice == "c":
            converse_with_camp_captain(player)
        elif choice == "r":
            player.regain_health(20)
            print(f"\nYou have rested and regained health. Current health: {player.health}.\n")
        elif choice == "i":
            player.inventory.inventory_menu(player)
        elif choice == "s":
            shop.shop_menu(player)
        elif choice == "m":
            from game1 import main_menu
            main_menu(player, shop)
        else:
            print("\nInvalid choice. Please enter a valid command.\n")

def leave_camp(player, shop):
    while True:
        clear_console()
        print("Where would you like to go?\n")
        choice = input("(D)ark Forest or (B)ack to camp: ").lower().strip()

        if choice == "d":
            enter_dark_forest(player, shop)
            break
        elif choice == "b":
            print("\nYou decide to stay in the camp for now.")
            break
        else:
            print("\nInvalid choice. Please enter 'D' to go to the Dark Forest or 'B' to go back to camp.")

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
    print(f"\nCamp Captain: 'Remember, use it wisely, and don't hesitate to return should you need more supplies or assistance.'\n")




