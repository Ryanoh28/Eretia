
def rest_in_location(player):
    if player.inventory.has_item("Bedroll"):
       
        bedroll = next(item for item in player.inventory.items if item.name == "Bedroll")
        bedroll.use_bedroll(player)
    else:
        print("\nYou need a Bedroll to rest here.")
        input("Press Enter to continue...")

