import random

class Plant:
    def __init__(self, name, req_level, growth_time, planting_xp, care_xp, harvesting_xp, yield_range):
        self.name = name
        self.req_level = req_level
        self.growth_time = growth_time  # in minutes
        self.planting_xp = planting_xp
        self.care_xp = care_xp
        self.harvesting_xp = harvesting_xp
        self.yield_range = yield_range  # tuple (min, max)

class HorticultureSkill:
    def __init__(self, player):
        self.player = player
        self.level = player.horticulture_level
        self.xp = player.horticulture_experience
        self.garden = []  

    def plant(self, plant):
        if self.player.horticulture_level >= plant.req_level:
            if self.player.inventory.remove_item(plant.name + " Seed"):
                self.garden.append(plant)
                self.player.horticulture_xp += plant.planting_xp
                print(f"Planted {plant.name}. Gained {plant.planting_xp} XP in horticulture.")
                self.check_level_up()
            else:
                print("You do not have the required seeds.")
        else:
            print("Your horticulture level is not high enough to plant this.")

    def check_level_up(self):
        while self.player.horticulture_xp >= 100:  
            self.player.horticulture_xp -= 100
            self.player.horticulture_level += 1
            print(f"Congratulations! Your horticulture level is now {self.player.horticulture_level}.")

    def harvest(self, plant):
        if plant in self.garden:
            self.garden.remove(plant)
            yield_amount = random.randint(plant.yield_range[0], plant.yield_range[1])
            self.player.inventory.add_item(plant.name, yield_amount)
            self.player.horticulture_xp += plant.harvesting_xp
            print(f"Harvested {yield_amount} {plant.name}. Gained {plant.harvesting_xp} XP in horticulture.")
            self.check_level_up()

plants_table = [
    {"name": "Simple Herb", "req_level": 1, "growth_time": 30, "planting_xp": 5, "care_xp": 2, "harvesting_xp": 10, "yield_range": (1, 3)},
    {"name": "Moonflower", "req_level": 5, "growth_time": 60, "planting_xp": 10, "care_xp": 3, "harvesting_xp": 20, "yield_range": (1, 2)},
    {"name": "Starleaf", "req_level": 10, "growth_time": 120, "planting_xp": 20, "care_xp": 5, "harvesting_xp": 40, "yield_range": (1, 4)},
    {"name": "Sunblossom", "req_level": 15, "growth_time": 180, "planting_xp": 30, "care_xp": 8, "harvesting_xp": 60, "yield_range": (2, 5)},
    {"name": "Eldertree Sapling", "req_level": 20, "growth_time": 360, "planting_xp": 50, "care_xp": 15, "harvesting_xp": 100, "yield_range": (1, 1)}
]

