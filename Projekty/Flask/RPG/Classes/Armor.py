from .Item import Item
from .Location import Location

class Armor(Item):
    def __init__(self, name : str, location : Location):
        Item.__init__(self, name, location)
