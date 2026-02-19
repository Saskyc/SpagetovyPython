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
    f.write("Zdraví tvoje python aplikace.\nNegři")
print("Do souboru bylo přidáno")

from pathlib import Path

cesta = Path("data") / "osoby" / "seznam.txt"
print(f"Sestavená cesta: {cesta}")