from .Entity import Entity
from .Item import Item

class Hrdina(Entity):
    def __init__(self, jmeno : str):
        super().__init__(jmeno, 0, 0)
        self.inventar : list[Item] = []