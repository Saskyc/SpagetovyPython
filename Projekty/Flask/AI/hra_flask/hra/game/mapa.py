import yaml
import os
from .Location import Location
from .BlockedConfiguration import BlockedConfiguration
from .ItemManager import ItemManager

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")


def load_world_data():
    """Načte lokace a předměty z YAML souborů. Vrátí (locations_data, items_data)."""
    with open(os.path.join(DATA_DIR, "locations.yaml"), encoding="utf-8") as f:
        locations_data = yaml.safe_load(f)
    with open(os.path.join(DATA_DIR, "items.yaml"), encoding="utf-8") as f:
        items_data = yaml.safe_load(f)
    return locations_data, items_data


def build_world(locations_data, items_data):
    """Sestaví seznam lokací a přiřadí předměty. Vrátí list lokací (jako dict pro session)."""
    # Sestavíme lokace
    locations = []
    for loc_data in locations_data:
        locations.append({
            "id": loc_data["id"],
            "jmeno": loc_data["jmeno"],
            "popis": loc_data["popis"],
            "x": loc_data["x"],
            "y": loc_data["y"],
            "block": loc_data["block"],
            "enemies": loc_data.get("enemies", []),
            "spawn_chance": loc_data.get("spawn_chance", 0.0),
            "requires_key": loc_data.get("requires_key", None),
            "win_condition": loc_data.get("win_condition", False),
            "predmety": [],       # předměty aktuálně v lokaci
            "enemy_defeated": False,  # byl nepřítel poražen?
        })

    # Přiřadíme předměty do lokací (nebo do inventáře pokud x=1000)
    world_items = []
    for item_data in items_data:
        item = ItemManager.from_dict(item_data)
        world_items.append(item.to_dict())

    # Předměty které jsou v lokacích (ne v inventáři)
    for item_dict in world_items:
        if item_dict["locationX"] != 1000:
            for loc in locations:
                if loc["x"] == item_dict["locationX"] and loc["y"] == item_dict["locationY"]:
                    loc["predmety"].append(item_dict)
                    break

    return locations, world_items


def get_location(locations, x, y):
    """Najde lokaci na souřadnicích x,y."""
    for loc in locations:
        if loc["x"] == x and loc["y"] == y:
            return loc
    return None


def get_available_directions(location):
    """Vrátí seznam dostupných směrů z dané lokace."""
    directions = []
    block = location["block"]
    if not block["up"]:
        directions.append("up")
    if not block["down"]:
        directions.append("down")
    if not block["left"]:
        directions.append("left")
    if not block["right"]:
        directions.append("right")
    return directions


DIRECTION_LABELS = {
    "up": "Sever ↑",
    "down": "Jih ↓",
    "left": "Západ ←",
    "right": "Východ →",
}

DIRECTION_DELTA = {
    "up": (0, 1),
    "down": (0, -1),
    "left": (-1, 0),
    "right": (1, 0),
}
