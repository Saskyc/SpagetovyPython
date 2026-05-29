from .Item import Item

class Potion(Item):
    def __init__(self, name: str, x: int, y: int, heal: int) -> None:
        Item.__init__(self, name, x, y)
        self.heal: int = heal

    def to_dict(self) -> dict:
        information = Item.to_dict(self)
        information["heal"] = self.heal
        information["type"] = "Item.Potion"
        return information

    def __repr__(self) -> str:
        return f"Potion({self.name}, {self.heal}hp)"
