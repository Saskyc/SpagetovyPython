import random
from flask import Flask, render_template, request, session, redirect, url_for, jsonify, Response

from Classes.Location import Location
from game.mapa import (
    load_world_data, build_world, get_location,
    get_available_directions, DIRECTION_DELTA, DIRECTION_LABELS
)
from game import inventar as inv
from game import souboj

app = Flask(__name__)
app.secret_key = "muj_uzasny_soukromy_klic"


# ---------------------------------------------------------------------------
# Pomocné funkce
# ---------------------------------------------------------------------------

def init_game(jmeno : str) -> None:
    """Inicializuje novou hru a uloží vše do session."""
    locations_data, items_data = load_world_data()
    locations, world_items = build_world(locations_data, items_data)

    session["hrdina"] = {
        "jmeno": jmeno,
        "x": 0,
        "y": 0,
        "health": 100,
        "equipped_weapon": None,
        "equipped_armor": None,
    }
    session["inventory"] = []
    session["locations"] = locations
    session["world_items"] = world_items
    session["combat"] = None
    session["message"] = f"Vítej, {jmeno}! Tvoje dobrodružství začíná ve Vesnici Prahu."
    session.modified = True


def get_current_location() -> Location:
    hrdina = session.get("hrdina", {})
    return get_location(session.get("locations", []), hrdina.get("x", 0), hrdina.get("y", 0))


def check_random_encounter(location):
    """Zkontroluje, zda dojde k náhodnému střetnutí s nepřítelem."""
    if location.get("enemy_defeated"):
        return None
    enemies = location.get("enemies", [])
    if not enemies:
        return None
    chance = location.get("spawn_chance", 0.0)
    if random.random() < chance:
        return random.choice(enemies)
    return None


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/", methods=["GET"])
def index():
    if "hrdina" not in session:
        return redirect(url_for("start"))
    return redirect(url_for("game"))


@app.route("/start", methods=["GET", "POST"])
def start():
    if request.method == "POST":
        jmeno = request.form.get("jmeno", "").strip()
        if not jmeno:
            return render_template("start.html", error="Zadej jméno hrdiny!")
        init_game(jmeno)
        return redirect(url_for("game"))
    return render_template("start.html")


@app.route("/game", methods=["GET"])
def game():
    if "hrdina" not in session:
        return redirect(url_for("start"))

    # Pokud probíhá souboj, přesměruj na souboj
    if session.get("combat"):
        return redirect(url_for("combat_view"))

    hrdina = session["hrdina"]
    location = get_current_location()
    if not location:
        return redirect(url_for("start"))

    directions = get_available_directions(location)
    dir_labels = {d: DIRECTION_LABELS[d] for d in directions}

    message = session.pop("message", None)
    session.modified = True

    return render_template(
        "index.html",
        hrdina=hrdina,
        location=location,
        dir_labels=dir_labels,
        message=message,
        inventory=session.get("inventory", []),
    )


@app.route("/move/<direction>", methods=["POST"])
def move(direction):
    if "hrdina" not in session:
        return redirect(url_for("start"))

    location = get_current_location()
    if not location:
        return redirect(url_for("game"))

    block = location["block"]
    blocked_map = {"up": block["up"], "down": block["down"], "left": block["left"], "right": block["right"]}

    if direction not in DIRECTION_DELTA or blocked_map.get(direction, True):
        session["message"] = "Tudy se jít nedá."
        session.modified = True
        return redirect(url_for("game"))

    dx, dy = DIRECTION_DELTA[direction]
    new_x = session["hrdina"]["x"] + dx
    new_y = session["hrdina"]["y"] + dy

    new_location = get_location(session["locations"], new_x, new_y)
    if not new_location:
        session["message"] = "Tam nic není."
        session.modified = True
        return redirect(url_for("game"))

    # Kontrola klíčového předmětu (requires_key)
    required_key = new_location.get("requires_key")
    if required_key and not inv.has_key_item(session, required_key):
        session["message"] = f"🔒 Tato cesta je zablokována. Potřebuješ speciální předmět pro průchod!"
        session.modified = True
        return redirect(url_for("game"))

    # Přesun
    session["hrdina"]["x"] = new_x
    session["hrdina"]["y"] = new_y
    session["message"] = f"Přesunul ses do: {new_location['jmeno']}"
    session.modified = True

    # Kontrola náhodného střetnutí
    enemy = check_random_encounter(new_location)
    if enemy:
        souboj.start_combat(session, enemy)
        session.modified = True
        return redirect(url_for("combat_view"))

    return redirect(url_for("game"))


@app.route("/pick/<item_name>", methods=["POST"])
def pick_item(item_name : str) -> Response:
    if "hrdina" not in session:
        return redirect(url_for("start"))

    location = get_current_location()
    if not location:
        return redirect(url_for("game"))

    # Najdi předmět v lokaci
    for i, item in enumerate(location["predmety"]):
        if item["name"] == item_name:
            inv.add_item(session, item)
            location["predmety"].pop(i)
            session["message"] = f"✅ Sebral jsi: {item_name}"
            session.modified = True
            return redirect(url_for("game"))

    session["message"] = f"Předmět '{item_name}' tu není."
    session.modified = True
    return redirect(url_for("game"))


@app.route("/inventar")
def inventar_view():
    if "hrdina" not in session:
        return redirect(url_for("start"))
    return render_template(
        "inventar.html",
        hrdina=session["hrdina"],
        inventory=session.get("inventory", []),
    )


@app.route("/use/<item_name>", methods=["POST"])
def use_item(item_name):
    if "hrdina" not in session:
        return redirect(url_for("start"))

    result = inv.use_item(session, item_name)
    session["message"] = result["message"]
    session.modified = True

    # Kontrola smrti po použití předmětu (edge case)
    if session["hrdina"]["health"] <= 0:
        return redirect(url_for("konec", result="prohra"))

    return redirect(request.referrer or url_for("inventar_view"))


@app.route("/drop/<item_name>", methods=["POST"])
def drop_item(item_name):
    if "hrdina" not in session:
        return redirect(url_for("start"))

    location = get_current_location()
    result = inv.drop_item(session, item_name, location)
    session["message"] = result["message"]
    session.modified = True
    return redirect(url_for("inventar_view"))


# ---------------------------------------------------------------------------
# Souboj
# ---------------------------------------------------------------------------

@app.route("/combat", methods=["GET"])
def combat_view():
    if "hrdina" not in session:
        return redirect(url_for("start"))
    if not session.get("combat"):
        return redirect(url_for("game"))

    message = session.pop("combat_message", None)
    session.modified = True

    return render_template(
        "souboj.html",
        hrdina=session["hrdina"],
        combat=session["combat"],
        inventory=session.get("inventory", []),
        message=message,
    )


@app.route("/combat/attack", methods=["POST"])
def combat_attack():
    if "hrdina" not in session or not session.get("combat"):
        return redirect(url_for("game"))

    result = souboj.player_attack(session)
    session.modified = True
    return _handle_combat_result(result)


@app.route("/combat/escape", methods=["POST"])
def combat_escape():
    if "hrdina" not in session or not session.get("combat"):
        return redirect(url_for("game"))

    result = souboj.player_escape(session)
    session.modified = True
    return _handle_combat_result(result)


@app.route("/combat/use/<item_name>", methods=["POST"])
def combat_use_item(item_name):
    if "hrdina" not in session or not session.get("combat"):
        return redirect(url_for("game"))

    result = souboj.use_item_in_combat(session, item_name)
    session.modified = True
    return _handle_combat_result(result)


def _handle_combat_result(result):
    status = result.get("status")
    log = result.get("log", [])

    if status == "player_dead":
        session["message"] = " | ".join(log)
        session.modified = True
        return redirect(url_for("konec", result="prohra"))

    if status == "player_won":
        session["message"] = " | ".join(log)
        session.modified = True
        return redirect(url_for("konec", result="vyhra"))

    if status == "enemy_defeated":
        session["message"] = " | ".join(log)
        session.pop("combat", None)
        session.modified = True
        return redirect(url_for("game"))

    if status == "escaped":
        session["message"] = " | ".join(log)
        session.pop("combat", None)
        session.modified = True
        return redirect(url_for("game"))

    # ongoing
    session["combat_message"] = " | ".join(log)
    session.modified = True
    return redirect(url_for("combat_view"))


# ---------------------------------------------------------------------------
# Konec hry
# ---------------------------------------------------------------------------

@app.route("/konec/<result>")
def konec(result):
    hrdina = session.get("hrdina", {})
    message = session.pop("message", None)
    session.modified = True
    return render_template("konec.html", result=result, hrdina=hrdina, message=message)


@app.route("/restart", methods=["POST"])
def restart():
    session.clear()
    return redirect(url_for("start"))


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
