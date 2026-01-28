from .Npc import Npc
from .Location import Location

class Location:
    def __init__(self : "Location"):
        self.name : str = "Location"
        self.locations : list = []
        self.npcs : list = []
        self.enemies : list = []

    @staticmethod
    def remove(self : "Location", npc : "Npc") -> None:
        try:
            self.npcs.remove(npc)
            self.enemies.remove(npc)
        except:
            pass