from ...MyObjects.Weapon import Weapon

class Stick(Weapon):
    def __init__(self):
        super().__init__("Stick", 1, 0)

class ShortWoodenSword(Weapon):
    def __init__(self):
        super().__init__("Wooden Short Sword", 1, 1)

class ShortWoodenSword(Weapon):
    def __init__(self):
        super().__init__("Wooden Long Sword", 3, 2)

class ShortStoneSword(Weapon):
    def __init__(self):
        super().__init__("Stone Short Sword", 5, 3)

class LongStoneSword(Weapon):
    def __init__(self):
        super().__init__("Stone Long Sword", 7, 6)

class ShortIronSword(Weapon):
    def __init__(self):
        super().__init__("Stone Short Sword", 6, 5)

class LongIronSword(Weapon):
    def __init__(self):
        super().__init__("Stone Long Sword", 9, 7)