from .Item import Item
class Inventory:
    def __init__(self):
        self.items : list[Item] = []
    def to_dict(self) -> dict:
        return {
            "items": [item.to_dict() for item in self.items],
        }
    def add_item(self, item : Item) -> None:
        item.locationX = 1000
        item.locationY = 1000
        self.items.append(item)