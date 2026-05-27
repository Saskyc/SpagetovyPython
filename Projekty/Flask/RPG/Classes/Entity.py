class Entity:
    def __init__(self, jmeno : str, x : int, y : int):
        self.jmeno : str = jmeno
        self.x : int = x
        self.y : int = y
        self.health : int = 100