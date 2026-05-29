from .BlockedConfiguration import BlockedConfiguration
from .SerializableClass import SerializableClass
from .BlockedConfiguration import BlockedConfiguration
from .Item import Item

class Location(SerializableClass):
    def __init__(self, id : int, jmeno : str, x : int, y : int, block : BlockedConfiguration = BlockedConfiguration()):
        SerializableClass.__init__(self, id)
        self.block : BlockedConfiguration = block
        self.jmeno : str = jmeno
        self.x : int = x
        self.y : int = y
        self.items : list[Item] = []

    def to_dict(self) -> dict:
        information = SerializableClass.to_dict(self)
        information["jmeno"] = self.jmeno
        information["x"] = self.x
        information["y"] = self.y
        information["block"] = self.block.to_dict()
        return information

    @staticmethod
    def from_dict(data) -> "Location":
        return Location(
            data["id"],
            data["jmeno"],
            data["x"],
            data["y"],
            data["block"],
        )

    def __repr__(self) -> str:
        return f"Location({self.jmeno}, {self.x}, {self.y})"