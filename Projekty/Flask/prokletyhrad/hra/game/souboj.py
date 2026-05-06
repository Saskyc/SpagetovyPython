"""
game/souboj.py
Logika souboje hrdiny s nepřítelem.
"""
from __future__ import annotations
import random
from game.hrdina import Hrdina


class Nepritel:
    """Reprezentuje nepřítele v souboji (stav kopírovaný ze session)."""

    def __init__(self, data: dict):
        self.id: str = data["id"]
        self.nazev: str = data["nazev"]
        self.zivoty: int = data["zivoty"]
        self.max_zivoty: int = data["zivoty"]
        self.utok: int = data["utok"]
        self.obrana: int = data["obrana"]
        self.odmena_predmet: str | None = data.get("odmena_predmet")
        self.ikona: str = data.get("ikona", "👾")

    def je_nazivu(self) -> bool:
        return self.zivoty > 0

    def utoci(self, hrdina: Hrdina) -> tuple[int, int]:
        """
        Nepřítel zaútočí na hrdinu.
        Vrátí (hruby_utok, skutecne_poskozeni).
        """
        hruby = self.utok + random.randint(-3, 3)
        skutecne = hrdina.utrap(hruby)
        return hruby, skutecne

    def do_dict(self) -> dict:
        return {
            "id": self.id,
            "nazev": self.nazev,
            "zivoty": self.zivoty,
            "max_zivoty": self.max_zivoty,
            "utok": self.utok,
            "obrana": self.obrana,
            "odmena_predmet": self.odmena_predmet,
            "ikona": self.ikona,
        }

    @classmethod
    def z_dict(cls, d: dict) -> "Nepritel":
        n = cls(d)
        n.zivoty = d["zivoty"]         # obnovíme aktuální životy (mohou být snížené)
        n.max_zivoty = d["max_zivoty"]
        return n


# ── Výpočty souboje ───────────────────────────────────────────────────────────

def vypocti_poskozeni_hrdiny(hrdina: Hrdina, nepritel: Nepritel) -> tuple[int, int]:
    """
    Vypočítá útok hrdiny.
    Vrátí (hruby_utok, skutecne_poskozeni_nepritelovi).
    """
    hruby = hrdina.utok + random.randint(-3, 5)
    skutecne = max(1, hruby - nepritel.obrana)
    nepritel.zivoty = max(0, nepritel.zivoty - skutecne)
    return hruby, skutecne


def utec_uspesne() -> bool:
    """50% šance na útěk."""
    return random.random() < 0.5


def kolo_souboje(akce: str, hrdina: Hrdina, nepritel: Nepritel) -> dict:
    """
    Provede jedno kolo souboje podle akce hráče.
    akce: 'utok' | 'utec'
    Vrátí slovník s výsledky kola.
    """
    zprava_hrdiny = ""
    zprava_nepritele = ""
    utekl = False
    skoncil = False
    vitez = False

    if akce == "utok":
        h_hruby, h_skutecne = vypocti_poskozeni_hrdiny(hrdina, nepritel)
        zprava_hrdiny = f"Útočíš za {h_hruby} – nepřítel blokuje {nepritel.obrana}, dostane {h_skutecne} poškození."

        if not nepritel.je_nazivu():
            skoncil = True
            vitez = True
        else:
            n_hruby, n_skutecne = nepritel.utoci(hrdina)
            zprava_nepritele = f"{nepritel.nazev} útočí za {n_hruby} – tvá obrana {hrdina.obrana}, dostaneš {n_skutecne} poškození."
            if not hrdina.je_nazivu():
                skoncil = True
                vitez = False

    elif akce == "utec":
        if utec_uspesne():
            utekl = True
            zprava_hrdiny = "Podařilo se ti uprchnout!"
        else:
            zprava_hrdiny = "Útěk se nezdařil!"
            n_hruby, n_skutecne = nepritel.utoci(hrdina)
            zprava_nepritele = f"{nepritel.nazev} tě dostihuje a zasáhne za {n_skutecne} poškození."
            if not hrdina.je_nazivu():
                skoncil = True
                vitez = False

    return {
        "zprava_hrdiny": zprava_hrdiny,
        "zprava_nepritele": zprava_nepritele,
        "utekl": utekl,
        "skoncil": skoncil,
        "vitez": vitez,
        "zivoty_hrdiny": hrdina.zivoty,
        "zivoty_nepritele": nepritel.zivoty,
    }
