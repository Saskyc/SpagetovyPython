from .Location import Location

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