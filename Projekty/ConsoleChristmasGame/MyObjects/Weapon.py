from .Item import Item

class Weapon(Item):
    def __init__(self, name : str, damage : int, penetration : int):
        super().__init__(name)
        self.damage = damage
        self.penetration = penetration