import yaml
import os
from Classes.Location import Location
from Classes.Item import Item
from Classes.Armor import Armor
from Classes.Weapon import Weapon

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))



with open(os.path.join(__location__,"Definitions\\Locations.yaml"), 'w') as file:
    locations : list[Location] = [
        Location(1, "Test", 1, 2),
        Location(2, "Dalsi", 1, 3)
    ]
    yaml.dump([i.to_dict() for i in locations], file)

with open(os.path.join(__location__,"Definitions\\Items.yaml"), 'w') as file:
    items : list[Item] = [
        Item("ItemTest", 0, 0),
        Armor("ArmoTest", 0, 0, 20),
        Weapon("WeaponTest", 0, 0, 5, 5),
    ]
    yaml.dump([i.to_dict() for i in items], file)