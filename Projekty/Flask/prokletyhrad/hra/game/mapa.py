"""
game/mapa.py
Načítání světa a práce s lokacemi.
"""
from __future__ import annotations
import json
import os


DATA_SOUBOR = os.path.join(os.path.dirname(__file__), "..", "data", "svet.json")


def nacti_svet() -> dict:
    """Načte a vrátí celý slovník světa ze svet.json."""
    with open(DATA_SOUBOR, encoding="utf-8") as f:
        return json.load(f)


class Lokace:
    """Reprezentuje jednu lokaci světa."""

    def __init__(self, data: dict):
        self.id: str = data["id"]
        self.nazev: str = data["nazev"]
        self.popis: str = data["popis"]
        self.sousede: dict[str, str | None] = data["sousede"]
        self.predmety: list[str] = list(data.get("predmety", []))
        self.nepratel: str | None = data.get("nepratel")
        self.vyzaduje_predmet: str | None = data.get("vyzaduje_predmet")
        self.vyzaduje_text: str = data.get("vyzaduje_text", "Vstup je zablokován.")
        self.win_condition: bool = data.get("win_condition", False)

    def dostupne_smery(self) -> dict[str, str]:
        """Vrátí jen smery kde existuje cíl (ne None)."""
        return {smer: cil for smer, cil in self.sousede.items() if cil}

    def sebrat_predmet(self, predmet_id: str) -> bool:
        """Odebere předmět z lokace (po sebrání). Vrátí False pokud tam není."""
        if predmet_id in self.predmety:
            self.predmety.remove(predmet_id)
            return True
        return False
    def sousedni_lokace(self, mapa) -> dict[str, Lokace]:
        return {
            smer: mapa.get(cil)
            for smer, cil in self.sousede.items()
            if cil
        }


class Mapa:
    """Spravuje všechny lokace světa."""

    SMER_NAZVY = {
        "sever": "Sever ↑",
        "jih": "Jih ↓",
        "vychod": "Východ →",
        "zapad": "Západ ←",
    }

    def __init__(self, data: dict):
        self._lokace = {lid: Lokace(ldata) for lid, ldata in data["lokace"].items()}

    def get(self, lokace_id: str) -> Lokace | None:
        return self._lokace.get(lokace_id)

    def vsechny(self) -> dict[str, Lokace]:
        return self._lokace

    # ── Serializace stavu mapy (sebrané předměty) ───────────────

    def stav_predmetu(self) -> dict[str, list[str]]:
        """Vrátí {lokace_id: [predmety]} – pro uložení do session."""
        return {lid: list(lok.predmety) for lid, lok in self._lokace.items()}

    def nacti_stav_predmetu(self, stav: dict[str, list[str]]):
        """Obnoví stav předmětů v lokacích ze session."""
        for lid, predmety in stav.items():
            if lid in self._lokace:
                self._lokace[lid].predmety = predmety
