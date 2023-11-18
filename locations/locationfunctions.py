def rest_in_location(player):
    if "Bedroll" in player.inventory.items:
        bedroll = player.inventory.items["Bedroll"]['object']
        bedroll.use_bedroll(player)
    else:
        print("You don't have a Bedroll in your inventory.")
        input("\nPress Enter to continue...")


def return_to_location(player):
    if player.current_location == 'dark_forest':
        from locations.darkforest import enter_dark_forest
        enter_dark_forest(player)
    elif player.current_location == 'damp_cave':
        from locations.dampcave import enter_damp_cave
        enter_damp_cave(player)
    elif player.current_location == 'cave_entrance':
        from locations.dampcave import explore_passages
        explore_passages(player)
    elif player.current_location == 'the_border':  
        from locations.theborder import enter_the_border
        enter_the_border(player)
    
    
    # Add more elif statements for other locations if needed
