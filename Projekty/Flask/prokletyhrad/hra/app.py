"""
app.py
Hlavní Flask aplikace – routes a session management.
"""
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash

from game.hrdina import Hrdina
from game.mapa import Mapa, nacti_svet
from game.inventar import Inventar, Predmet
from game.souboj import Nepritel, kolo_souboje

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "tajny-klic-pro-vyvoj-123")


# ── Pomocné funkce ────────────────────────────────────────────────────────────

def _nacti_svet_a_mapu() -> tuple[dict, Mapa]:
    """Načte data světa a sestaví Mapa objekt se stavem ze session."""
    data = nacti_svet()
    mapa = Mapa(data)
    if "stav_predmetu" in session:
        mapa.nacti_stav_predmetu(session["stav_predmetu"])
    return data, mapa


def _uloz_session(hrdina: Hrdina, mapa: Mapa, lokace_id: str):
    """Uloží stav hry do session."""
    session["hrdina"] = hrdina.do_dict()
    session["lokace_id"] = lokace_id
    session["stav_predmetu"] = mapa.stav_predmetu()
    session.modified = True


def _hrdina_ze_session() -> Hrdina | None:
    if "hrdina" not in session:
        return None
    return Hrdina.z_dict(session["hrdina"])


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/", methods=["GET", "POST"])
def index():
    """Úvodní stránka – zadání jména hrdiny."""
    if request.method == "POST":
        jmeno = request.form.get("jmeno", "").strip()
        if not jmeno:
            flash("Zadej jméno hrdiny!", "chyba")
            return redirect(url_for("index"))

        hrdina = Hrdina(jmeno)
        data, mapa = _nacti_svet_a_mapu()
        # Resetujeme svět
        mapa_cista = Mapa(data)
        _uloz_session(hrdina, mapa_cista, "vesnice")
        return redirect(url_for("hra"))

    return render_template("index.html")


@app.route("/hra")
def hra():
    """Hlavní herní obrazovka – zobrazí aktuální lokaci."""
    hrdina = _hrdina_ze_session()
    if not hrdina:
        return redirect(url_for("index"))

    data, mapa = _nacti_svet_a_mapu()
    lokace_id = session.get("lokace_id", "vesnice")
    lokace = mapa.get(lokace_id)

    # Předměty dostupné v lokaci jako Predmet objekty
    inv = Inventar(data["predmety"])
    predmety_lokace = [inv.predmet(pid) for pid in lokace.predmety if inv.predmet(pid)]
    predmety_hrdiny = inv.seznam_hrdiny(hrdina)

    return render_template(
        "index_hra.html",
        hrdina=hrdina,
        lokace=lokace,
        sousede=lokace.sousedni_lokace(mapa),
        predmety_lokace=predmety_lokace,
        predmety_hrdiny=predmety_hrdiny,
        smery=Mapa.SMER_NAZVY,
    )


@app.route("/pohyb/<smer>")
def pohyb(smer: str):
    """Pohyb do sousední lokace."""
    hrdina = _hrdina_ze_session()
    if not hrdina:
        return redirect(url_for("index"))

    data, mapa = _nacti_svet_a_mapu()
    lokace_id = session["lokace_id"]
    lokace = mapa.get(lokace_id)
    cil_id = lokace.sousede.get(smer)

    if not cil_id:
        flash("Tímto směrem se jít nedá.", "info")
        return redirect(url_for("hra"))

    cil = mapa.get(cil_id)

    # Kontrola klíčového předmětu
    if cil.vyzaduje_predmet and not hrdina.ma_predmet(cil.vyzaduje_predmet):
        flash(cil.vyzaduje_text, "varování")
        return redirect(url_for("hra"))

    _uloz_session(hrdina, mapa, cil_id)

    # Spustit souboj pokud lokace má nepřítele
    if cil.nepratel:
        nepritel_data = data["nepratele"].get(cil.nepratel)
        if nepritel_data:
            session["nepritel"] = Nepritel(nepritel_data).do_dict()
            session.modified = True
            return redirect(url_for("souboj_stranka"))

    return redirect(url_for("hra"))


@app.route("/sebrat/<predmet_id>")
def sebrat(predmet_id: str):
    """Sebrání předmětu z lokace."""
    hrdina = _hrdina_ze_session()
    if not hrdina:
        return redirect(url_for("index"))

    data, mapa = _nacti_svet_a_mapu()
    lokace_id = session["lokace_id"]
    lokace = mapa.get(lokace_id)
    inv = Inventar(data["predmety"])
    predmet = inv.predmet(predmet_id)

    if not predmet or predmet_id not in lokace.predmety:
        flash("Předmět zde není.", "chyba")
    elif not hrdina.pridej_predmet(predmet_id):
        flash("Inventář je plný! (max 8 předmětů)", "varování")
    else:
        lokace.sebrat_predmet(predmet_id)
        flash(f"Sebral jsi: {predmet.ikona} {predmet.nazev}", "uspech")

    _uloz_session(hrdina, mapa, lokace_id)
    return redirect(url_for("hra"))


@app.route("/pouzit/<predmet_id>")
def pouzit(predmet_id: str):
    """Použití předmětu z inventáře."""
    hrdina = _hrdina_ze_session()
    if not hrdina:
        return redirect(url_for("index"))

    data, mapa = _nacti_svet_a_mapu()
    inv = Inventar(data["predmety"])
    predmet = inv.predmet(predmet_id)

    if not predmet or not hrdina.ma_predmet(predmet_id):
        flash("Předmět nemáš.", "chyba")
    else:
        zprava = predmet.pouzij(hrdina)
        flash(zprava, "uspech")

    _uloz_session(hrdina, mapa, session["lokace_id"])
    return redirect(url_for("inventar_stranka"))


@app.route("/vyhodit/<predmet_id>")
def vyhodit(predmet_id: str):
    """Vyhození předmětu."""
    hrdina = _hrdina_ze_session()
    if not hrdina:
        return redirect(url_for("index"))

    data, mapa = _nacti_svet_a_mapu()
    inv = Inventar(data["predmety"])
    predmet = inv.predmet(predmet_id)

    if predmet and hrdina.odeber_predmet(predmet_id):
        flash(f"Zahodil jsi {predmet.nazev}.", "info")
    else:
        flash("Předmět nemáš.", "chyba")

    _uloz_session(hrdina, mapa, session["lokace_id"])
    return redirect(url_for("inventar_stranka"))


@app.route("/inventar")
def inventar_stranka():
    """Zobrazení inventáře."""
    hrdina = _hrdina_ze_session()
    if not hrdina:
        return redirect(url_for("index"))

    data, _ = _nacti_svet_a_mapu()
    inv = Inventar(data["predmety"])
    predmety = inv.seznam_hrdiny(hrdina)

    return render_template("inventar.html", hrdina=hrdina, predmety=predmety)


@app.route("/souboj", methods=["GET", "POST"])
def souboj_stranka():
    """Obrazovka souboje."""
    hrdina = _hrdina_ze_session()
    if not hrdina or "nepritel" not in session:
        return redirect(url_for("hra"))

    data, mapa = _nacti_svet_a_mapu()
    nepritel = Nepritel.z_dict(session["nepritel"])
    inv = Inventar(data["predmety"])

    vysledek = None
    zprava_hrdiny = None
    zprava_nepritele = None

    if request.method == "POST":
        akce = request.form.get("akce", "utok")

        # Použití předmětu v souboji
        if akce.startswith("pouzit_"):
            pid = akce[7:]
            predmet = inv.predmet(pid)
            if predmet and hrdina.ma_predmet(pid):
                zprava = predmet.pouzij(hrdina)
                flash(zprava, "uspech")
                # Nepřítel také zaútočí
                _, n_skutecne = nepritel.utoci(hrdina)
                zprava_nepritele = f"{nepritel.nazev} útočí a zasáhne za {n_skutecne} poškození."
                if not hrdina.je_nazivu():
                    session.pop("nepritel", None)
                    _uloz_session(hrdina, mapa, session["lokace_id"])
                    return redirect(url_for("konec_stranka", vysledek="prohra"))
            session["nepritel"] = nepritel.do_dict()
            _uloz_session(hrdina, mapa, session["lokace_id"])
        else:
            # Útok nebo útěk
            kolo = kolo_souboje(akce, hrdina, nepritel)
            zprava_hrdiny = kolo["zprava_hrdiny"]
            zprava_nepritele = kolo["zprava_nepritele"]

            if kolo["utekl"]:
                session.pop("nepritel", None)
                _uloz_session(hrdina, mapa, session["lokace_id"])
                flash("Utekl jsi z boje!", "info")
                return redirect(url_for("hra"))

            if kolo["skoncil"]:
                if kolo["vitez"]:
                    # Odměna
                    if nepritel.odmena_predmet:
                        if hrdina.pridej_predmet(nepritel.odmena_predmet):
                            odmena = inv.predmet(nepritel.odmena_predmet)
                            flash(f"Získal jsi: {odmena.ikona} {odmena.nazev}", "uspech")

                    # Zkontrolovat win condition
                    lokace = mapa.get(session["lokace_id"])
                    session.pop("nepritel", None)
                    _uloz_session(hrdina, mapa, session["lokace_id"])

                    if lokace and lokace.win_condition:
                        return redirect(url_for("konec_stranka", vysledek="vyhral"))
                    flash(f"Porazil jsi {nepritel.nazev}!", "uspech")
                    return redirect(url_for("hra"))
                else:
                    session.pop("nepritel", None)
                    _uloz_session(hrdina, mapa, session["lokace_id"])
                    return redirect(url_for("konec_stranka", vysledek="prohra"))

            session["nepritel"] = nepritel.do_dict()
            _uloz_session(hrdina, mapa, session["lokace_id"])

    predmety_hrdiny = inv.seznam_hrdiny(hrdina)
    return render_template(
        "souboj.html",
        hrdina=hrdina,
        nepritel=nepritel,
        predmety=predmety_hrdiny,
        zprava_hrdiny=zprava_hrdiny,
        zprava_nepritele=zprava_nepritele,
    )


@app.route("/konec/<vysledek>")
def konec_stranka(vysledek: str):
    """Obrazovka výhry nebo prohry."""
    hrdina = _hrdina_ze_session()
    vyhral = vysledek == "vyhral"
    return render_template("konec.html", hrdina=hrdina, vyhral=vyhral)


@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
