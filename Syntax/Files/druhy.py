import os

# Spočti počet řádků a slov v souboru
with open('pozdrav.txt', 'r') as file:
    print(os.path.abspath(file.name))

radky = 0
slova = 0
with open("pozdrav.txt", "r", encoding="utf-8") as f:
    for radek in f:
        radky += 1
        slova += len(radek.split())
print(f"Řádků: {radky} Slova: {slova}")

#read(n) vs. readline()
with open("pozdrav.txt", "r", encoding="utf-8") as f:
    prvnich_5 = f.read(5)
    dalsi_radek = f.readline().strip()
print(f"Prvních 5 znaků: {prvnich_5}")
print(f"Další řádek: {dalsi_radek}")

#velke soubory: iterace je pametove usporna
pocet = 0
with open("velk_log.txt", "r", encoding="utf-8") as f:
    for _ in f:
        pocet += 1
print(f"Počet řádků ve velkém souboru: {pocet}")