class Item:
    def __init__(self, name : str, x : int, y : int):
        self.name : str = name
        self.locationX = x
        self.locationY = y
    def to_dict(self) -> dict:
        return {
            "type": "Item",
            "name": self.name,
            "locationX": self.locationX,
            "locationY": self.locationY,
        }

    def is_in_inventory(self) -> bool:
        return self.locationX == 1000 and self.locationY == 1000

    def __repr__(self) -> str:
        return f"Item({self.name}, {self.locationX}, {self.locationY})"