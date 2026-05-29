from .Entity import Entity
from .Item import Item
from .Inventory import Inventory

class Hrdina(Entity):
    def __init__(self, jmeno : str):
        Entity.__init__(self, jmeno, 0, 0)
        self.inventory : Inventory = Inventory()
    def to_dict(self) -> dict:
        information = Entity.to_dict(self)
        information["inventory"] = self.inventory.to_dict()
        return information