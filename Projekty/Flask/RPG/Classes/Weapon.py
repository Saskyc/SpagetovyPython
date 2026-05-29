from .Item import Item
from .Location import Location

class Weapon(Item):
    def __init__(self, name : str, x : int, y : int, attack : int, penetration : int) -> None:
        Item.__init__(self, name, x, y)
        self.attack: int = attack
        self.penetration = penetration
    def to_dict(self) -> dict:
        information = Item.to_dict(self)
        information["attack"] = self.attack
        information["penetration"] = self.penetration
        information["type"] = "Item.Weapon"
        return information
    def __repr__(self) -> str:
        return f"Weapon({self.name}, {self.locationX}, {self.locationY}, {self.attack}, {self.penetration})"
