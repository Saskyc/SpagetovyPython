class Location:
    def __init__(self, jmeno : str, x : int, y : int):
        self.jmeno : str = jmeno
        self.x : int = x
        self.y : int = y

    def to_dict(self):
        return {
            "jmeno": self.jmeno,
            "x": self.x,
            "y": self.y
        }

    @staticmethod
    def from_dict(data):
        return Location(
            data["jmeno"],
            data["x"],
            data["y"]
        )

    def __repr__(self):
        return f"Location({self.jmeno}, {self.x}, {self.y})"