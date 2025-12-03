"""
=================1=================
"""

def detektivka(seznam : list[int]) -> int | None:
    y : tuple[int | None, int | None] = (None, None)
    for cislo in seznam:
        if y[0] is None:
            y = (cislo, y[1])
            continue
        if y[0] == cislo:
            continue
        if y[0] < cislo:
            temp = y[0]
            y = (cislo, temp)
            continue
        if y[1] is None:
            y = (y[0], cislo)
            continue
        if y[1] < cislo:
            y = (y[0], cislo)
            continue
    return y[1]

sez : list[int] = [13, 7, 22, 22, 6, 18, 9, 22, 14, 3]
print(detektivka(sez))

"""
=================2=================
"""

class HashList:
    def __init__(self : "HashList") -> None:
        self.navstevnici : list[str] = []
        self.duplicity : int = 0
    def pridat(self : "HashList", navstevnik : str) -> None:
        for jmeno in self.navstevnici:
            if navstevnik == jmeno:
                self.duplicity += 1
                return
        self.navstevnici.append(navstevnik)

def koncert(seznam : list[str]) -> "HashList":
    konc = HashList()
    for navstevnik in seznam:
        konc.pridat(navstevnik)
    
    return konc

sez : list[str] = ["Franta Novák", "Eva Malá", "Franta Novák", "Petr Dlouhý", "Eva Malá"]
info = koncert(sez)
print(f"Duplicit: {info.duplicity}, Návštěnvící: {info.navstevnici}")

"""
=================3=================
"""

def autobusrotace(seznam : list[object], k : int) -> list[object]:
    unsorted : list[tuple[object, int]] = []
    index = 0
    for thing in seznam:
        unsorted.append((thing, (index + k) % len(seznam)))
        index += 1
    sorted : list[object] = [1] * len(seznam)
    for i in unsorted:
        del sorted[i[1]]
        sorted.insert(i[1], i[0])
    return sorted

a = [1, 2, 3, 4, 5, 6, 7]
print([1, 2, 3, 4, 5, 6, 7], autobusrotace(a, 3))

"""
=================4=================
"""

def vesnicetrziste(prvni : list[str], druhy : list[str]) -> list[str]:
    hash = HashList()
    for i in prvni:
        hash.pridat(i)
    for i in druhy:
        hash.pridat(i)
    return hash.navstevnici

vesnice_a = ["med", "sýr", "chléb", "vejce"]
vesnice_b = ["sýr", "máslo", "vejce", "slivovice"]
print(vesnicetrziste(vesnice_a, vesnice_b))

"""
=================6=================
"""

def reverselist(seznam : list[object]) -> list[object]:
    sorted : list[object] = []
    for i in seznam:
        sorted.insert(0, i)
    return sorted
    
data = ["A", "B", "C", "D", "E"]
print(reverselist(data))

"""
=================7=================
"""

def insertsortedlist(seznam : list[int], insert : int) -> list[int]:
    inserted = False
    sorted : list[int] = []
    for i in seznam:
        if inserted:
            sorted.append(i)
            continue
        if insert > i:
            sorted.append(i)
            continue
        sorted.append(insert)
        inserted = True
    if not inserted:
        sorted.append(insert)
    return sorted

data : list[int] = [12, 18, 18, 23, 27, 31]
print(insertsortedlist(data, 25))

"""
=================8=================
"""

class Posloupnoust:
    def __init__(self : "Posloupnoust") -> None:
        self.prvky : list[object] = []
        self.maraton : tuple[object, int]
        self.vysledek : int = []
    def process(self : "Posloupnoust") -> "Posloupnoust":
        self.maraton = []
        curobj : object = None
        rotace : int = 0
        prvni : bool = True
        for i in self.prvky:
            if prvni:
                prvni : bool = False
                curobj : object = i
                rotace : int = 1
                continue
            if i != curobj:
                self.maraton.append((i, rotace))
                rotace = 1
                continue
            if i == curobj:
                rotace += 1
        
        mar : tuple[object, int] | None = None
        for i in self.maraton:
            if mar is None:
                mar = i
                continue
            if i[1] > mar[1]:
                mar = i
        self.vysledek = mar
        return self
    @staticmethod
    def staticprocess(prvky : list[object]) -> tuple[object, int]:
        posloupnoust : "Posloupnoust" = Posloupnoust()
        posloupnoust.prvky = prvky
        return posloupnoust.process().vysledek

tempo : list[int] = [5, 5, 6, 6, 6, 7, 7, 5, 5, 5, 5]
print(Posloupnoust.staticprocess(tempo))