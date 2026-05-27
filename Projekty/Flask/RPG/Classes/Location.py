from .SerializableClass import SerializableClass
class Location(SerializableClass):
    def __init__(self, id : int, jmeno : str, x : int, y : int):
        SerializableClass.__init__(id)
        self.id = id
        self.jmeno : str = jmeno
        self.x : int = x
        self.y : int = y

    def to_dict(self):
        return {
            "jmeno": self.jmeno,
            "id": self.id,
            "x": self.x,
            "y": self.y
        }

    @staticmethod
    def from_dict(data):
        return Location(
            data["id"],
            data["jmeno"],
            data["x"],
            data["y"]
        )

    def __repr__(self):
        return f"Location({self.jmeno}, {self.x}, {self.y})"