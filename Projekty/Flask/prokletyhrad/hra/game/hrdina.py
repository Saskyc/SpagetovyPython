"""
game/hrdina.py
Třída Hrdina – uchovává stav hráče.
"""

MAX_ZIVOTY = 100
LIMIT_INVENTARE = 8  # maximální počet předmětů v inventáři


class Hrdina:
    def __init__(self, jmeno: str):
        self.jmeno = jmeno
        self.zivoty = MAX_ZIVOTY
        self.max_zivoty = MAX_ZIVOTY
        self.zaklad_utok = 10    # základní útok bez zbraně
        self.zaklad_obrana = 5  # základní obrana bez brnění
        self.bonus_utok = 0     # bonus ze zbraně
        self.bonus_obrana = 0   # bonus z brnění
        self.inventar: list[str] = []  # seznam ID předmětů

    # ── Statistiky ─────────────────────────────────────────────

    @property
    def utok(self) -> int:
        return self.zaklad_utok + self.bonus_utok

    @property
    def obrana(self) -> int:
        return self.zaklad_obrana + self.bonus_obrana

    def je_nazivu(self) -> bool:
        return self.zivoty > 0

    # ── Životy ─────────────────────────────────────────────────

    def utrap(self, poskozeni: int):
        """Sníží životy o čisté poškození (po odečtení obrany)."""
        skut = max(1, poskozeni - self.obrana)
        self.zivoty = max(0, self.zivoty - skut)
        return skut

    def vylec(self, mnozstvi: int):
        """Obnoví životy, nepřekročí maximum."""
        self.zivoty = min(self.max_zivoty, self.zivoty + mnozstvi)

    # ── Vybavení ───────────────────────────────────────────────

    def vybav_zbran(self, bonus: int):
        self.bonus_utok = bonus

    def vybav_brneni(self, bonus: int):
        self.bonus_obrana = bonus

    # ── Inventář ───────────────────────────────────────────────

    def ma_predmet(self, predmet_id: str) -> bool:
        return predmet_id in self.inventar

    def pridej_predmet(self, predmet_id: str) -> bool:
        """Přidá předmět do inventáře. Vrátí False pokud je plný."""
        if len(self.inventar) >= LIMIT_INVENTARE:
            return False
        self.inventar.append(predmet_id)
        return True

    def odeber_predmet(self, predmet_id: str) -> bool:
        """Odebere předmět z inventáře. Vrátí False pokud tam není."""
        if predmet_id in self.inventar:
            self.inventar.remove(predmet_id)
            return True
        return False

    # ── Serializace (pro Flask session) ────────────────────────

    def do_dict(self) -> dict:
        return {
            "jmeno": self.jmeno,
            "zivoty": self.zivoty,
            "max_zivoty": self.max_zivoty,
            "zaklad_utok": self.zaklad_utok,
            "zaklad_obrana": self.zaklad_obrana,
            "bonus_utok": self.bonus_utok,
            "bonus_obrana": self.bonus_obrana,
            "inventar": self.inventar,
        }

    @classmethod
    def z_dict(cls, data: dict) -> "Hrdina":
        h = cls(data["jmeno"])
        h.zivoty = data["zivoty"]
        h.max_zivoty = data["max_zivoty"]
        h.zaklad_utok = data["zaklad_utok"]
        h.zaklad_obrana = data["zaklad_obrana"]
        h.bonus_utok = data["bonus_utok"]
        h.bonus_obrana = data["bonus_obrana"]
        h.inventar = data["inventar"]
        return h
