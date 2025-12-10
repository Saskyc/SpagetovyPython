#Literal
osoba : dict[str, object] = {
    "jmeno" : "Franta",
    "vek" : 18,
}

print("osoba typ", type(osoba), osoba)

#Konstruktor dict - z dvojic (iteratovatelný)
pary : list[tuple[str, object]] = [
    ("jmeno", "Franta"),
    ("vek", 18)
]
print("pary typ", type(pary), pary)
osoba : dict[str, object] = dict(osoba)
print("osoba typ", type(osoba), osoba)

#Z klíčových arghumentů (když jsou identifikátory)
osoba : dict[str, object] = dict(
    jmeno = "Franta",
    vek = 18
)

print("osoba typ", type(osoba), osoba)

#Z klíče se stejnou hodnotou
klice : list[str] = ["A", "B", "C"]
vse_na_zero : dict[str, int] = dict.fromkeys(klice, 0)

print("klice typ", type(klice), klice)
print("vse_na_zero typ", type(vse_na_zero), vse_na_zero)

"""
Pristup k hodnotam
"""

osoba = {
    "jmeno": "Franta",
    "vek": 18,
}

osoba["jmeno"] #-> "Franta" (KeyError, pokud klíč neexistuje)
osoba.get("trida") #-> None (nevyhodnotí výjimku)
osoba.get("trida", "nezadano") #-> Místo None vrátí string "nezadano".

"""
Přídání, změna, smazání
"""

osoba["skola"] = "SPŠ"
osoba["vek"] = 19 #změna hodnoty
del osoba["skola"] #smazání klíče (KeyError, pokud neexistuje)
osoba.pop("vek", None) #smaže a vrátí hodnotu, jinak vráti výchozí hodnotu.

"""
Důležité metody
"""

osoba = {
    "jmeno": "Franta",
    "vek": 18,
}

osoba.keys() #dict_leys - "živý" pohled na klíče
osoba.values() #dict_values - hodnoty
osoba.items() #dict_items - (klíč, hodnota) tuple páry

a = {
    "jmeno" : "Franta",
    "vek" : 19,
}

b = {
    "vek" : 19,
    "trida" : "2.B"
}

a.update(b) #a se změní na: jmeno Franta, vek 19, trida 2.B

#Python 3.9+ operátor sjednocení
c = a | {
    "prumer" : 1.75 #nový slovník a starý zůástane
}

"""
Iterace přes slovníky
"""

znamky = {
    "Matematika" : 1,
    "Python" : 2,
    "Fyzika" : 1,
}

#přes klíče
for predmet in znamky:
    print(predmet, znamky[predmet])

#přes páry
for predmet, znamka in znamky.items():
    print(predmet, znamka)

#filtrujeme nebo transformujeme
vyborne = {
    p: z
    for p, z in znamky.items()
        if z == 1
}

"""
Dict comprehension (skládání slovníku)
"""

#mapování předmetů na kreditový koeficient
predmety = [
    "Matematika",
    "Python",
    "Fyzika"
]