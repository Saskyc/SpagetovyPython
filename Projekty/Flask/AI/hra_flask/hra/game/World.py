from .Location import Location
from .Hrdina import Hrdina
from .Entity import Entity

class World:
    def __init__(self):
        self.locations : list[Location] = []
    def addLocation(self, location : Location) -> "World":
        self.locations.append(location)
        return self
    def getLocation(self, x, y) -> Location | None:
        for location in self.locations:
            if location.x == x and location.y == y:
                return location
        return None

    def fight(self, plr : Hrdina, enemy : Entity):
        print("Fighting started.")
        while True:
            inp = input("Attack/UseItem/Escape: ").lower()
            if(inp == "attack"):
                print("Attacking")
                break
            if(inp == "useitem"):
                print("Use Item")
                break
            if(inp == "escape"):
                print("Escape")
                breakS