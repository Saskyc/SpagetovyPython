from .Location import Location
from .Friendly import Friendly
from .Hostile import Hostile
from .Item import Item
from .Weapon import Weapon
from .Npc import Npc
from .Text import Color

class Status:
    def __init__(self):
        self.Location : "Location" = None
        self.TalkingWith : "Friendly" = None
        self.FightingWith : "Hostile" = None

class Inventory:
    def __init__(self):
        self.Items : list[Item] = []
        self.Armor : list = []
        self.EquippedWeapon : "Weapon" = None

class Player:
    def __init__(self):
        self.Hp : int = 100
        self.Coin : int = 0
        self.inventory = Inventory()
        self.status = Status()
    def removeCoin(self, number : int) -> None:
        self.Coin = self.Coin - number
        if self.Coin < 0:
            self.Coin = 0
    def addCoin(self, number : int) -> None:
        self.Coin += number
    def attack(self, entity : "Npc"):
        entity.health = entity.health - self.inventory.EquippedWeapon.damage
    def stats(self) -> None:
        print(f"{Color.Reset}Player overview:\n HP: {self.Hp}\n Coin: {self.Coin}\n Location: {self.status.Location.name}")