from combat import fight_monster
from utilities import clear_console

def enter_dark_forest(player, shop):
    while True:
        clear_console()
        print("\nYou are in the Dark Forest. What would you like to do?")
        choice = input("(H)unt Monsters or (R)eturn to Camp: ").lower().strip()
        clear_console()

        if choice == "h":
            fight_monster(player, shop)
        elif choice == "r":
            from camp import return_to_camp
            return_to_camp(player, shop)
            break
        else:
            print("\nInvalid choice. Please enter 'H' to hunt monsters or 'R' to return to camp.\n")
