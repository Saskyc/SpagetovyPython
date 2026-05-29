"""
Inventar modul – pracuje s předměty uloženými jako dict v session.
"""
from .ItemManager import ItemManager


def get_inventory(session_data: dict) -> list:
    """Vrátí seznam předmětů z herního stavu (session)."""
    return session_data.get("inventory", [])


def add_item(session_data: dict, item_dict: dict) -> None:
    """Přidá předmět do inventáře hráče."""
    item = item_dict.copy()
    item["locationX"] = 1000
    item["locationY"] = 1000
    session_data.setdefault("inventory", []).append(item)


def remove_item(session_data: dict, item_name: str) -> dict | None:
    """Odstraní předmět z inventáře podle jména. Vrátí odstraněný předmět nebo None."""
    inventory = session_data.get("inventory", [])
    for i, item in enumerate(inventory):
        if item["name"] == item_name:
            return inventory.pop(i)
    return None


def use_item(session_data: dict, item_name: str) -> dict:
    """
    Použije předmět z inventáře.
    Vrátí dict: {"success": bool, "message": str, "item": dict|None}
    """
    inventory = session_data.get("inventory", [])
    item_dict = None
    item_index = None

    for i, item in enumerate(inventory):
        if item["name"] == item_name:
            item_dict = item
            item_index = i
            break

    if item_dict is None:
        return {"success": False, "message": f"Předmět '{item_name}' není v inventáři.", "item": None}

    item_type = item_dict.get("type", "Item")

    if item_type == "Item.Potion":
        heal = item_dict.get("heal", 0)
        old_hp = session_data["hrdina"]["health"]
        new_hp = min(100, old_hp + heal)
        session_data["hrdina"]["health"] = new_hp
        inventory.pop(item_index)
        return {
            "success": True,
            "message": f"Použil jsi {item_dict['name']} a obnovil sis {new_hp - old_hp} životů. (HP: {new_hp}/100)",
            "item": item_dict,
        }

    if item_type == "Item.Weapon":
        # Vybaví zbraň – zvýší útok hrdiny
        # Nejdřív odlož starou zbraň (pokud existuje)
        old_weapon = session_data["hrdina"].get("equipped_weapon")
        session_data["hrdina"]["equipped_weapon"] = {
            "name": item_dict["name"],
            "attack": item_dict.get("attack", 0),
            "penetration": item_dict.get("penetration", 0),
        }
        inventory.pop(item_index)
        # Stará zbraň jde zpět do inventáře
        if old_weapon:
            inventory.append({
                "type": "Item.Weapon",
                "name": old_weapon["name"],
                "locationX": 1000,
                "locationY": 1000,
                "attack": old_weapon["attack"],
                "penetration": old_weapon["penetration"],
            })
        return {
            "success": True,
            "message": f"Vybavil sis zbraň {item_dict['name']} (útok: +{item_dict.get('attack', 0)}).",
            "item": item_dict,
        }

    if item_type == "Item.Armor":
        old_armor = session_data["hrdina"].get("equipped_armor")
        session_data["hrdina"]["equipped_armor"] = {
            "name": item_dict["name"],
            "defense": item_dict.get("defense", 0),
        }
        inventory.pop(item_index)
        if old_armor:
            inventory.append({
                "type": "Item.Armor",
                "name": old_armor["name"],
                "locationX": 1000,
                "locationY": 1000,
                "defense": old_armor["defense"],
            })
        return {
            "success": True,
            "message": f"Oblékl sis {item_dict['name']} (obrana: +{item_dict.get('defense', 0)}).",
            "item": item_dict,
        }

    if item_type == "Item.KeyItem":
        return {
            "success": False,
            "message": f"'{item_dict['name']}' je klíčový předmět – nelze použít přímo. Automaticky se aktivuje na správném místě.",
            "item": item_dict,
        }

    return {"success": False, "message": "Tento předmět nelze použít.", "item": item_dict}


def has_key_item(session_data: dict, key_id: str) -> bool:
    """Zkontroluje, zda hráč má klíčový předmět s daným key_id."""
    for item in session_data.get("inventory", []):
        if item.get("type") == "Item.KeyItem" and item.get("key_id") == key_id:
            return True
    return False


def drop_item(session_data: dict, item_name: str, location: dict) -> dict:
    """Odhodí předmět z inventáře do aktuální lokace."""
    item = remove_item(session_data, item_name)
    if item is None:
        return {"success": False, "message": f"Předmět '{item_name}' není v inventáři."}
    item["locationX"] = location["x"]
    item["locationY"] = location["y"]
    location["predmety"].append(item)
    return {"success": True, "message": f"Odhodil jsi {item_name}."}


def get_attack_bonus(session_data: dict) -> int:
    w = session_data["hrdina"].get("equipped_weapon")
    return w["attack"] if w else 0


def get_defense_bonus(session_data: dict) -> int:
    a = session_data["hrdina"].get("equipped_armor")
    return a["defense"] if a else 0
