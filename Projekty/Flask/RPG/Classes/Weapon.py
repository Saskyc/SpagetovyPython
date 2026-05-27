from .Item import Item
from .Location import Location

class Weapon(Item):
    def __init__(self, name : str, location : Location, attack : int):
        super().__init__(name, location)
        self.attack : int = attack
