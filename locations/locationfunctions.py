


def rest_in_location(player):
    if player.inventory.has_item("Bedroll"):
       
        bedroll = next(item for item in player.inventory.items if item.name == "Bedroll")
        bedroll.use_bedroll(player)
    else:
        print("You need a Bedroll to rest here.")
        input("\nPress Enter to continue...")

def return_to_location(player, shop):
    if player.current_location == 'dark_forest':
        from locations.darkforest import enter_dark_forest
        enter_dark_forest(player, shop)
    elif player.current_location == 'damp_cave':
        from locations.dampcave import enter_damp_cave
        enter_damp_cave(player, shop)
    elif player.current_location == 'cave_entrance':
        from locations.dampcave import explore_passages
        explore_passages(player, shop)