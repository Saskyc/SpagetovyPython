class Karta:
    def __init__(self, nazev, hodnota):
        self.nazev = nazev
        self.hodnota = hodnota
mujObjekt = Karta("K", 10)
print(mujObjekt.nazev)
print(mujObjekt.hodnota)

list = [Karta("Jedna", 1), Karta("Dva", 2), Karta("Tri", 3)]