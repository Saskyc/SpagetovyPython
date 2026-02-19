#r čtení (soubor musí existovat)
#w zápis (vytvoří nový nebo smaže a přepíše existující)
#a přidání na konec (Vytvoří pokud neexistuje)
#x vytvoří nový (pokud existuje = chyba)

from pathlib import Path

cesta = Path("data") / "osoby" / "seznam.txt"
print(f"Sestavená cesta: {cesta}")
exists = cesta.exists()
print(exists)

if not exists:
    cesta.parent.mkdir(parents=True, exist_ok=True)  # ensure folders exist
    open(cesta, "x", encoding="utf-8")


    #Vytvoření a zápis textového souboru
    with open(cesta, "w", encoding="utf-8") as f:
        f.write("Ahoj, Franto Nováku\n")
    print("Soubor pozdrav.txt byl vytvořen a zapsán")

    # Čtení celého souboru najednou
    with open(cesta, "r", encoding="utf-8") as f:
        obsah = f.read()
    print(f"Obsah: {obsah}")

#Přidání dalšího řádku
with open(cesta, "a", encoding="utf-8") as f:
    f.write("Zdraví tvoje python aplikace.\n")
print("Do souboru bylo přidáno")

from datetime import datetime

while True:
    theThing = input("Koho zdravis? ")
    with open(cesta, "a", encoding="utf-8") as f:
        f.write(f"Pozdraven {theThing} ({str(datetime.now())})\n")

