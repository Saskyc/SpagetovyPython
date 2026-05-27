import yaml
import os
from Classes.Location import Location

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__,"Definitions\Locations.yaml"), 'w') as file:
    locations : list[Location] = [Location(1, "Test", 1, 2), Location(2, "Dalsi", 1, 3)]
    yaml.dump([loc.to_dict() for loc in locations], file)