class Enemy:
    def __init__(self, name: str, health: int, attack: int, defense: int, loot_item: str | None = None):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defense = defense
        self.loot_item = loot_item  # jméno předmětu co nepřítel upustí

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "health": self.health,
            "max_health": self.max_health,
            "attack": self.attack,
            "defense": self.defense,
            "loot_item": self.loot_item,
        }

    @staticmethod
    def from_dict(data: dict) -> "Enemy":
        e = Enemy(data["name"], data["max_health"], data["attack"], data["defense"], data.get("loot_item"))
        e.health = data["health"]
        return e

    def __repr__(self) -> str:
        return f"Enemy({self.name}, hp={self.health}/{self.max_health})"
