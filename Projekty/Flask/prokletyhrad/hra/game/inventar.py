"""
game/inventar.py
Třídy Predmet a Inventar.
"""
from __future__ import annotations
from game.hrdina import Hrdina


class Predmet:
    """Reprezentuje jeden předmět načtený z dat světa."""

    def __init__(self, data: dict):
        self.id: str = data["id"]
        self.nazev: str = data["nazev"]
        self.typ: str = data["typ"]          # zbran | lektvar | brneni | klicovy
        self.popis: str = data["popis"]
        self.efekt_zivoty: int = data.get("efekt_zivoty", 0)
        self.efekt_utok: int = data.get("efekt_utok", 0)
        self.efekt_obrana: int = data.get("efekt_obrana", 0)
        self.ikona: str = data.get("ikona", "📦")

    def pouzij(self, hrdina: Hrdina) -> str:
        """
        Aplikuje efekt předmětu na hrdinu.
        Vrátí textový popis výsledku.
        Jednoúčelové předměty (lektvar) jsou odebrány z inventáře po použití.
        """
        if self.typ == "lektvar":
            if self.efekt_zivoty > 0:
                hrdina.vylec(self.efekt_zivoty)
                hrdina.odeber_predmet(self.id)
                return f"Vypil jsi {self.nazev} a obnovil sis {self.efekt_zivoty} životů. (životy: {hrdina.zivoty}/{hrdina.max_zivoty})"
            elif self.efekt_utok > 0:
                hrdina.bonus_utok += self.efekt_utok
                hrdina.odeber_predmet(self.id)
                return f"Vypil jsi {self.nazev}. Útok dočasně zvýšen o {self.efekt_utok}!"
            return "Lektvar nemá žádný efekt."

        elif self.typ == "zbran":
            hrdina.vybav_zbran(self.efekt_utok)
            return f"Vybavil sis {self.nazev}. Útok +{self.efekt_utok}."

        elif self.typ == "brneni":
            hrdina.vybav_brneni(self.efekt_obrana)
            return f"Oblékl sis {self.nazev}. Obrana +{self.efekt_obrana}."

        elif self.typ == "klicovy":
            return f"{self.nazev} je klíčový předmět – nelze použít přímo, ale otevírá určitá místa."

        return "Neznámý typ předmětu."


class Inventar:
    """Pomocná třída pro práci s inventářem hrdiny a daty předmětů."""

    def __init__(self, data_predmetu: dict):
        """
        data_predmetu: slovník {id -> dict} ze svet.json["predmety"]
        """
        self._data = data_predmetu

    def predmet(self, predmet_id: str) -> Predmet | None:
        """Vrátí instanci Predmet nebo None."""
        d = self._data.get(predmet_id)
        return Predmet(d) if d else None

    def seznam_hrdiny(self, hrdina: Hrdina) -> list[Predmet]:
        """Vrátí seznam předmětů v inventáři hrdiny jako Predmet objekty."""
        return [p for pid in hrdina.inventar if (p := self.predmet(pid))]
