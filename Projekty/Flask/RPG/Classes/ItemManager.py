from .Item import Item
from .Armor import Armor
from .Weapon import Weapon

class ItemManager:
    @staticmethod
    def from_dict(information : dict) -> Item | None:
        type = information["type"]
        name = information["name"]
        x = information["locationX"]
        y = information["locationY"]

        if(type == "Item"):
            return Item(name, x, y)
        if(type == "Item.Armor"):
            defense = information["defense"]
            return Armor(name, x, y, defense)
        if(type == "Item.Weapon"):
            attack = information["attack"]
            penetration = information["penetration"]
            return Weapon(name, x, y, attack, penetration)
        return Item(name, x, y)