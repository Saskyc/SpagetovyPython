from pathlib import Path
from datetime import datetime
from datetime import time
import random

"""
cesta = Path("data") / "osoby" / "seznam.txt"
print(f"Sestavená cesta: {cesta}")

#r čtení (soubor musí existovat)
#w zápis (vytvoří nový nebo smaže a přepíše existující)
#a přidání na konec (Vytvoří pokud neexistuje)
#vytvoří nový (pokud existuje = chyba)

#Vytvoření a zápis textového souboru
with open("pozdrav.txt", "w", encoding="utf-8") as f:
    f.write("Ahoj, Franto Nováku\n")
print("Soubor pozdrav.txt byl vytvořen a zapsán")

# Čtení celého souboru najednou
with open("pozdrav.txt", "r", encoding="utf-8") as f:
    obsah = f.read()
print(f"Obsah: {obsah}")

#Přidání dalšího řádku
with open("pozdrav.txt", "a", encoding="utf-8") as f:
    f.write("Zdraví tvoje python aplikace.")
print("Do souboru bylo přidáno")

from pathlib import Path

cesta = Path("data") / "osoby" / "seznam.txt"
print(f"Sestavená cesta: {cesta}")

"""
#---------------------------------------------------

_DAYNAMES = [None, "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

datum = datetime.now().date()


hodina = time.hour


cisloDne = datum.toordinal() % 7 or 7
nazev = _DAYNAMES[cisloDne]

print(nazev)

cesta = Path("logy") / "mojepc" / f"{nazev}.txt"

print(cesta.absolute())

exists = cesta.exists()
print(exists)

if not exists:
    cesta.parent.mkdir(parents=True, exist_ok=True)  # ensure folders exist

with open(cesta, "a", encoding="utf-8") as f:
    f.write(f"Time: {datum.ctime()} | {random.randint(3, 20)} \n")
