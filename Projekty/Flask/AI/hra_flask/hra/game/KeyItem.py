from .Item import Item

class KeyItem(Item):
    """Klíčový předmět nutný pro postup nebo výhru."""
    def __init__(self, name: str, x: int, y: int, key_id: str) -> None:
        Item.__init__(self, name, x, y)
        self.key_id: str = key_id  # unikátní ID pro logiku hry

    def to_dict(self) -> dict:
        information = Item.to_dict(self)
        information["key_id"] = self.key_id
        information["type"] = "Item.KeyItem"
        return information

    def __repr__(self) -> str:
        return f"KeyItem({self.name}, key_id={self.key_id})"
