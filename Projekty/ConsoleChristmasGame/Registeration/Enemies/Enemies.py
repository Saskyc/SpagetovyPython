from ...MyObjects.Hostile import Hostile
class Spider(Hostile):
    def __init__(self : "Hostile"):
        super().__init__(40, 1, 3)
        self.name : str = "Spider"
        self.health : int = 5

class Zombie(Hostile):
    def __init__(self : "Hostile"):
        super().__init__(60, 5, 15)
        self.name : str = "Zombie"
        self.health : int = 20