import yaml
import os

from Classes.ItemManager import ItemManager
from Classes.Location import Location
from Classes.World import World
from Classes.Hrdina import Hrdina
from Classes.SaveManager import SaveManager

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

world = World()

with open(os.path.join(__location__,"Definitions\\Locations.yaml"), 'r') as file:
    data = yaml.safe_load(file)
    for i in data:
        world.addLocation(Location.from_dict(i))

print(world.locations)

with open(os.path.join(__location__,"Definitions\\Items.yaml"), 'r') as file:
    data = yaml.safe_load(file)
    for i in data:
        print(ItemManager.from_dict(i))


player = Hrdina("testJmeno")
SaveManager.savePlayer(player)
SaveManager.saveWorld(world)
