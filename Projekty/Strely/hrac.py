from .akce import Akce

class Hrac:
    def __init__(self, nazev : str):
        self.zivoty : int = 3
        self.nabity : int = 0
        self.brani : bool = False
        self.prohral : bool = False
        self.nazev : str = nazev
    def zacatek(self) -> None:
        self.brani = False
    def odebratZivot(self) -> None:
        self.zivoty = self.zivoty - 1
        if self.zivoty == 0:
            self.prohral = True
    def zautocitNa(self, dalsi : "Hrac") -> None:
        if dalsi.brani == True:
            return
        dalsi.odebratZivot()
    def info(self):
        print(f"{self.nazev} má {self.zivoty}hp a {self.nabity} nábojů")
    def akce(self, akce : Akce, dalsi : "Hrac") -> None:
        if akce.nazev == "nabit":
            print(f"{self.nazev} nabíjí a má nábojů {self.nabity}")
            self.nabity += 1
        if akce.nazev == "branit":
            print(f"{self.nazev} se brání")
            self.brani = True
        if akce.nazev == "utocit" and self.nabity > 0:
            print(f"{self.nazev} zaútočil na {dalsi.nazev}")
            self.zautocitNa(dalsi)