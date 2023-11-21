

def rest_in_location(player):
    if "Bedroll" in player.inventory.items:
        bedroll = player.inventory.items["Bedroll"]['object']
        bedroll.use_bedroll(player)
    else:
        print("You don't have a Bedroll in your inventory.")
        input("\nPress Enter to continue...")




def return_to_location(player):
    print("Returning to location:", player.current_location)
    if player.current_location is None:
        print("Location unknown. Redirecting to a default location.")
        player.current_location = 'border_town'
        return_to_border_town(player)
    else:
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
        elif player.current_location == 'lower_bonefields':
            from locations.theborder import lower_bonefields
            lower_bonefields(player)    
        elif player.current_location == 'border_town':
            from bordertown import return_to_border_town
            return_to_border_town(player)
        elif player.current_location == 'crossing':
            from locations.theborder import cross_menu
            cross_menu(player)
        elif player.current_location == 'follow_ancient_road':
            from locations.theborder import follow_ancient_road
            follow_ancient_road(player)
        if player.current_location == 'northern_hills':
            from locations.northernhills import show_northern_hills_menu
            show_northern_hills_menu(player)
        else:
            print("Unknown location. Redirecting to a default location.")
            player.current_location = 'border_town'
            from bordertown import return_to_border_town
            return_to_border_town(player)
