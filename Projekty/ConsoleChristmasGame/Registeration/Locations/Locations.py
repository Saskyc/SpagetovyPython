from ...MyObjects.Location import Location

class Tavern(Location):
    def __init__(self : "Location"):
        super().__init__()
        self.name : str = "Tavern"

class Blacksmith(Location):
    def __init__(self : "Location"):
        super().__init__()
        self.name : str = "Blacksmith"

class Cesta(Location):
    def __init__(self : "Location"):
        super().__init__()
        self.name : str = "Cesta"

class Cave(Location):
    def __init__(self : "Location"):
        super().__init__()
        self.name : str = "Cave"