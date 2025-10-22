import random
import time

class Osoba:
    def __init__(self, name, hours, minutes, entered):
        self.name = name
        self.hours = int(hours)
        self.minutes = int(minutes)
        if entered == "T":
            self.entered = True
        elif entered == "F":
            self.entered = False
        else:
            self.entered = bool(entered)

    @property
    def message(self):
        ent = "přišel"
        if not self.entered:
            ent = "odešel"
        if self.minutes < 10:
            self.minutes = str(self.minutes) + "0"
        return f"{self.name} {ent} v {self.hours}:{self.minutes}"

lidi = []

while True:
    h = input("Chceš opustit definování osob? y/n ")
    if h.lower() == "y":
        break

    lidi.insert(len(lidi), Osoba(input("Jméno: "), input("Hodiny: "), input("Minuty: "), input("Přišel (T)/odešel (F)")))


cas = (time.localtime().tm_hour, time.localtime().tm_min)

jmena=["Ondřej", "Borec3", "František", "Zloděj", "Omg"]

for i in range(5):
    cas = ((cas[0] + random.randrange(1,5)) % 24, (cas[1] + random.randrange(0,60)) % 60)

    osoba = Osoba(jmena.pop(0), cas[0], cas[1], bool(random.randrange(0, 2)))

    lidi.insert(len(lidi), osoba)


while True:
    try:
        getter = input("Najdi osobu dle jména ")

        found = False

        for clovek in lidi:
            if clovek.name == getter:
                print(clovek.message)
                found = True
                break
        if not found:
            print("Nenašel jsem osobu")
            continue
        break
    except:
        print("Špatně")

print(f"Osob v budově {len(lidi)}")