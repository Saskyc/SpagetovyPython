from .Item import Item
from .Armor import Armor
from .Weapon import Weapon
from .Potion import Potion
from .KeyItem import KeyItem

class ItemManager:
    @staticmethod
    def from_dict(information: dict) -> Item | None:
        t = information["type"]
        name = information["name"]
        x = information["locationX"]
        y = information["locationY"]

        if t == "Item.Armor":
            return Armor(name, x, y, information["defense"])
        if t == "Item.Weapon":
            return Weapon(name, x, y, information["attack"], information["penetration"])
        if t == "Item.Potion":
            return Potion(name, x, y, information["heal"])
        if t == "Item.KeyItem":
            return KeyItem(name, x, y, information["key_id"])
        return Item(name, x, y)
