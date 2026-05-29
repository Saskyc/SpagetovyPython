from .Item import Item
from .Location import Location

class Armor(Item):
    def __init__(self, name : str, x : int, y : int, defense : int) -> None:
        Item.__init__(self, name, x, y)
        self.defense = defense
    def to_dict(self) -> dict:
        information = Item.to_dict(self)
        information["defense"] = self.defense
        information["type"] = "Item.Armor"
        return information
    def __repr__(self) -> str:
        return f"Armor({self.name}, {self.locationX}, {self.locationY}, {self.defense})"