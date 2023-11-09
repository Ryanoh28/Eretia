from combat import fight_monster
from utilities import clear_console

def enter_dark_forest(player):
    while True:
        clear_console()
        print("\nYou are in the Dark Forest. What would you like to do?")
        choice = input("(H)unt Monsters or (R)eturn to Camp: ").lower().strip()

        if choice == "h":
            #print("\nYou look around and find a Monster Wolf to fight...\n") Handled in combat.py
            fight_monster(player)
            
        elif choice == "r":
            from camp import return_to_camp
            return_to_camp(player)
            break  
        else:
            print("\nInvalid choice. Please enter 'H' to hunt monsters or 'R' to return to camp.\n")
