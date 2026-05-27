import yaml
import os
from Classes.Location import Location
from Classes.World import World

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

world = World()

with open(os.path.join(__location__,"Definitions\Locations.yaml"), 'r') as file:
    data = yaml.safe_load(file)
    for i in data:
        world.addLocation(Location.from_dict(i))
print(world.locations)