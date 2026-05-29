"""
Souboj modul – logika boje hráče s nepřítelem.
"""
import random
from . import inventar as inv


def start_combat(session_data: dict, enemy_data: dict) -> None:
    """Zahájí souboj – uloží nepřítele do stavu hry."""
    session_data["combat"] = {
        "enemy": {
            "name": enemy_data["name"],
            "health": enemy_data["health"],
            "max_health": enemy_data["health"],
            "attack": enemy_data["attack"],
            "defense": enemy_data["defense"],
            "loot_item": enemy_data.get("loot_item"),
        },
        "log": [f"⚔️ Střetnutí s {enemy_data['name']}!"],
    }


def player_attack(session_data: dict) -> dict:
    """Hráč zaútočí na nepřítele. Vrátí výsledek akce."""
    combat = session_data.get("combat")
    if not combat:
        return {"status": "error", "message": "Žádný souboj neprobíhá."}

    enemy = combat["enemy"]
    attack_bonus = inv.get_attack_bonus(session_data)
    base_damage = random.randint(8, 18)
    player_damage = max(1, base_damage + attack_bonus - enemy["defense"] // 2)

    enemy["health"] = max(0, enemy["health"] - player_damage)
    log = [f"Zaútočil jsi – způsobil jsi {player_damage} poškození. (HP nepřítele: {enemy['health']}/{enemy['max_health']})"]

    if enemy["health"] <= 0:
        return _enemy_defeated(session_data, log)

    # Nepřítel zaútočí
    result = _enemy_attacks(session_data, log)
    return result


def enemy_attack_turn(session_data: dict) -> dict:
    """Pouze útok nepřítele (interní)."""
    pass  # voláno z player_attack


def _enemy_attacks(session_data: dict, log: list) -> dict:
    combat = session_data["combat"]
    enemy = combat["enemy"]
    defense_bonus = inv.get_defense_bonus(session_data)
    base_damage = random.randint(enemy["attack"] - 4, enemy["attack"] + 4)
    enemy_damage = max(1, base_damage - defense_bonus)

    session_data["hrdina"]["health"] -= enemy_damage
    log.append(f"{enemy['name']} zaútočil – způsobil ti {enemy_damage} poškození. (Tvoje HP: {session_data['hrdina']['health']}/100)")
    combat["log"].extend(log)

    if session_data["hrdina"]["health"] <= 0:
        session_data["hrdina"]["health"] = 0
        return {"status": "player_dead", "log": log}

    return {"status": "ongoing", "log": log}


def player_escape(session_data: dict) -> dict:
    """Hráč se pokusí utéct. 50% šance na úspěch."""
    combat = session_data.get("combat")
    if not combat:
        return {"status": "error", "message": "Žádný souboj neprobíhá."}

    if random.random() < 0.5:
        # Útěk se zdařil
        session_data.pop("combat", None)
        return {"status": "escaped", "log": ["🏃 Podařilo se ti utéct!"]}
    else:
        # Útěk selhal – nepřítel zaútočí
        log = ["❌ Útěk se nezdařil!"]
        return _enemy_attacks(session_data, log)


def use_item_in_combat(session_data: dict, item_name: str) -> dict:
    """Použití předmětu během boje. Po použití nepřítel zaútočí."""
    result = inv.use_item(session_data, item_name)
    log = [result["message"]]

    if not result["success"]:
        return {"status": "ongoing", "log": log}

    # Pokud hráč použil potion nebo brnění – nepřítel zaútočí
    combat = session_data.get("combat")
    if combat and combat["enemy"]["health"] > 0:
        enemy_result = _enemy_attacks(session_data, log)
        enemy_result["log"] = log
        return enemy_result

    return {"status": "ongoing", "log": log}


def _enemy_defeated(session_data: dict, log: list) -> dict:
    """Zpracuje porážku nepřítele."""
    combat = session_data["combat"]
    enemy = combat["enemy"]
    log.append(f"🎉 Porazil jsi {enemy['name']}!")

    loot = None
    loot_item_name = enemy.get("loot_item")
    if loot_item_name:
        # Najdeme předmět v world_items a přidáme ho do inventáře
        for item in session_data.get("world_items", []):
            if item["name"] == loot_item_name:
                loot = item.copy()
                loot["locationX"] = 1000
                loot["locationY"] = 1000
                session_data.setdefault("inventory", []).append(loot)
                log.append(f"📦 Získal jsi předmět: {loot_item_name}")
                break

    # Označíme lokaci jako "nepřítel poražen"
    player_x = session_data["hrdina"]["x"]
    player_y = session_data["hrdina"]["y"]
    for loc in session_data.get("locations", []):
        if loc["x"] == player_x and loc["y"] == player_y:
            loc["enemy_defeated"] = True
            break

    combat["log"].extend(log)
    session_data.pop("combat", None)

    # Kontrola win condition
    for loc in session_data.get("locations", []):
        if loc["x"] == player_x and loc["y"] == player_y and loc.get("win_condition"):
            return {"status": "player_won", "log": log}

    return {"status": "enemy_defeated", "log": log, "loot": loot}
