class Color:
    Reset = "\x1b[0m"
    class Regular:
        Black = "\x1b[0;30m"
        Red = "\x1b[0;31m"
        Green = "\x1b[0;32m"
        Yellow = "\x1b[0;33m"
        Blue = "\x1b[0;34m"
        Purple = "\x1b[0;35m"
        Cyan = "\x1b[0;36m"
        White = "\x1b[0;37m"
    class Bold:
        Black = "\x1b[1;30m"
        Red = "\x1b[1;31m"
        Green = "\x1b[1;32m"
        Yellow = "\x1b[1;33m"
        Blue = "\x1b[1;34m"
        Purple = "\x1b[1;35m"
        Cyan = "\x1b[1;36m"
        White = "\x1b[1;37m"
    class Underline:
        Black = "\x1b[4;30m"
        Red = "\x1b[4;31m"
        Green = "\x1b[4;32m"
        Yellow = "\x1b[4;33m"
        Blue = "\x1b[4;34m"
        Purple = "\x1b[4;35m"
        Cyan = "\x1b[4;36m"
        White = "\x1b[4;37m"
    class Background:
        Black = "\x1b[40m"
        Red = "\x1b[4;41m"
        Green = "\x1b[4;42m"
        Yellow = "\x1b[4;43m"
        Blue = "\x1b[4;44m"
        Purple = "\x1b[4;45m"
        Cyan = "\x1b[4;46m"
        White = "\x1b[4;47m"

    class Intensity:
        class High:
            Black = "\x1b[0;90m"
            Red = "\x1b[0;91m"
            Green = "\x1b[0;92m"
            Yellow = "\x1b[0;93m"
            Blue = "\x1b[0;94m"
            Purple = "\x1b[0;95m"
            Cyan = "\x1b[0;96m"
            White = "\x1b[0;97m"

            class Bold:
                Black = "\x1b[1;90"
                Red = "\x1b[1;91m"
                Green = "\x1b[1;92m"
                Yellow = "\x1b[1;93m"
                Blue = "\x1b[1;94m"
                Purple = "\x1b[1;95m"
                Cyan = "\x1b[1;96m"
                White = "\x1b[1;97m"

            class Background:
                Black = "\x1b[1;100m"
                Red = "\x1b[1;101m"
                Green = "\x1b[1;102m"
                Yellow = "\x1b[1;103m"
                Blue = "\x1b[1;104m"
                Purple = "\x1b[1;105m"
                Cyan = "\x1b[1;106m"
                White = "\x1b[1;107m"
class Text:
    class Hlavni:
        KategorieVyber = f"{Color.Intensity.High.Cyan}Jakou kategorii chceš navštívit?{Color.Reset}"
        VypisInfo = f"{Color.Intensity.High.Cyan}Zadej {Color.Regular.Red}'vypis' {Color.Intensity.High.Cyan}pro výpis všech produktů{Color.Reset}"
        UzivatelskyInput = f"{Color.Underline.Red}Uživatelský input:{Color.Reset} "
        HlavniVyberMoznost = f"- {Color.Intensity.High.Yellow}%option%{Color.Reset}"
    class Side:
        WriteReturn = f"{Color.Regular.Purple}Napiš {Color.Regular.Red}'return' {Color.Regular.Purple}pro vrácení.{Color.Reset}"
        SelectOption = f"{Color.Regular.Purple}Výběrová možnost: {Color.Intensity.High.Purple}%option%{Color.Reset}"
        WrongSelection = f"{Color.Regular.Red}Minulý výběr byl chybný{Color.Reset}"
        ItemWrite = f" {Color.Regular.Blue}%item%{Color.Reset}"
        UserInput = f"{Color.Underline.Red}Napiš ID pro vybrání itemu do košíku:{Color.Reset} "
    class Kosik:
        Line = f"{Color.Bold.Purple}=============================={Color.Reset}"
        Overview = f"{Color.Underline.Blue}Kosik overview{Color.Reset}{Color.Intensity.High.Green} (%price%) {Color.Reset}"
        Category = f"{Color.Reset}- {Color.Intensity.High.Cyan}Kategorie: %type%{Color.Reset}, {Color.Intensity.High.Yellow}Název: %name%{Color.Reset}, {Color.Intensity.High.Green}Cena: %price%{Color.Reset}"
class Zarizeni:
    def __init__(self, name, type, price, id):
        self.Name = name
        self.Type = type
        self.Price = price
        self.Id = id

    def __str__(self):
        return f'{self.Id} / Jméno: {self.Name} / Cena: {self.Price}'

from enum import Enum
Stav = Enum("Stav", ["HLAVNI", "SIDE", "KONEC"])
Options = Enum('Option', ["NONE", 'CPU', 'RAM', 'Motherboard', 'GPU', 
        'Zdroj', "HDD", "SSD", "Cooling", "SoundCard", "Case", "Monitor", "Reproduktor", "Sluchátka",
        "Myš", "Klávesnice", "Kamera", "Volant"])

def removeOptionPrefix(option):
    return str(option).removeprefix("Option.")

def ZiskatReference(typ, list):

    returnList = []

    for x in list:
        if x.Type != typ:
            continue
        returnList.append(x)

    return returnList

def kosikPrice(list):
    cena = 0
    for x in list:
        cena += x.Price
    return cena

def prehledKosiku(list):
    cena = kosikPrice(list)
    print(Text.Kosik.Line)
    print(Text.Kosik.Overview.replace("%price%", str(cena)))
    for x in list:
        text = Text.Kosik.Category.replace("%type%", removeOptionPrefix(str(x.Type)))
        text = text.replace("%name%", str(x.Name))
        text = text.replace("%price%", str(x.Price))
        print(text) #Dodělat
    print(Text.Kosik.Line)

def napsatHlavniVyber():
    validOptions.clear()
    for i in Options:
        validOptions.append((removeOptionPrefix(i), i))
        print(Text.Hlavni.HlavniVyberMoznost.replace("%option%", str(removeOptionPrefix(i))))

clear = lambda : print("\n"*100)

"""
Domácí úkol: Konfigurace PC soustavy

    CPU, RAM, MB, GPU, ZDROJ, HDD, SSD, 
    CHLAZENÍ, ZVUKOVÁ KARTA, PC CASE, MONITOR, 
    REPRÁK, SLUCHÁTKA, MYŠ, KLÁVESNICE, KAMERA, VOLANT

Použít MATCH.
5 od každého produktu.
"""

Sklad = [
    Zarizeni("Intel® Core™ i5-4590, 3.70GHz,Tray", Options.CPU, 490, 1),
    Zarizeni("AMD Ryzen 7 9800X3D", Options.CPU, 11690, 2),
    Zarizeni("AMD Ryzen 7 9700X", Options.CPU, 7390, 3),
    Zarizeni("Intel Core Ultra 5 225", Options.CPU, 4299, 4),
    Zarizeni("Intel Core Ultra 5 225F", Options.CPU, 3599, 5),

    Zarizeni("Kingston FURY 32GB KIT DDR4 3200MHz CL16 Beast Black 1Gx8", Options.RAM, 1100, 6),
    Zarizeni("Apacer 8GB DDR3 1600 MT/s CL11", Options.RAM, 2477, 7),
    Zarizeni("G.SKILL 32GB KIT DDR5 6000MHz CL30 Trident Z5 NEO RGB for AMD", Options.RAM, 3644, 8),
    Zarizeni("Patriot 32GB DDR4 3200MT/s CL22 Signature Premium", Options.RAM, 8879, 9),
    Zarizeni("Kingston FURY 32GB KIT DDR5 6000MT/s CL30 Beast Black EXPO", Options.RAM, 1000, 10),

    Zarizeni("ASUS TUF GAMING A520M-PLUS II", Options.Motherboard, 1700, 11),
    Zarizeni("Základní deska Bitmain (Control board)", Options.Motherboard, 3990, 12),
    Zarizeni("GIGABYTE b650 eagle ax/AM5/ATX", Options.Motherboard, 3369, 13),
    Zarizeni("ASUS PRIME A520M-K AM4 mATX", Options.Motherboard, 1249, 14),
    Zarizeni("MSI MAG B650 TOMAHAWK WIFI", Options.Motherboard, 3600, 15),

    Zarizeni("ASUS PRIME Radeon RX 9070 XT O16G", Options.GPU, 15590, 16),
    Zarizeni("XFX Quicksilver AMD Radeon RX 9070 XT 16G", Options.GPU, 15599, 17),
    Zarizeni("GIGABYTE GeForce RTX 5080 GAMING OC 16G", Options.GPU, 28589, 18),
    Zarizeni("XFX Mercury AMD Radeon RX 9060 XT OC Gaming Edition 16GB", Options.GPU, 9999, 19),
    Zarizeni("PALIT GeForce RTX 5050 Dual 8GB", Options.GPU, 5999, 20),

    Zarizeni("MSI MAG A850GL PCIE5 II", Options.Zdroj, 2399, 21),
    Zarizeni("Seasonic Core GX-750 ATX 3.1", Options.Zdroj, 2399, 22),
    Zarizeni("MSI MAG A750BN PCIE5", Options.Zdroj, 1399, 23),
    Zarizeni("ADATA XPG PYLON 550W", Options.Zdroj, 999, 24),
    Zarizeni("FSP Fortron VITA GM 1000W", Options.Zdroj, 2849, 25),

    Zarizeni("Seagate 3,5'' IronWolf 4TB", Options.HDD, 2555, 26),
    Zarizeni("Synology 3,5'' HAT3300 6TB", Options.HDD, 4999, 27),
    Zarizeni("Seagate 3,5'' IronWolf 8TB", Options.HDD, 4649, 28),
    Zarizeni("Western Elements 2,5'' 1,5TB", Options.HDD, 1899, 29),
    Zarizeni("Western WD80PUZX 1,8'' 8TB", Options.HDD, 10895, 30),

    Zarizeni("Samsung 990 PRO NVMe 2 TB", Options.SSD, 15000, 31),
    Zarizeni("Western Blue SN5000 1TB", Options.SSD, 10000, 32),
    Zarizeni("Digital Gold MM7111 .5TB", Options.SSD, 5000, 33),
    Zarizeni("Kingston DC600M 7,68TB", Options.SSD, 22690, 34),
    Zarizeni("ADATA Micron 5400 3.84 TB", Options.SSD, 22721, 35),

    Zarizeni("Cooler Master MASTERLIQUID 360 ATMOS", Options.Cooling, 5200, 36),
    Zarizeni("ARCTIC Freezer 36 A-RGB Black", Options.Cooling, 969, 37),
    Zarizeni("Corsair NAUTILUS 360 ARGB Black", Options.Cooling, 2790, 38),
    Zarizeni("ARCTIC P8 PWM PST", Options.Cooling, 139, 39),
    Zarizeni("XILENCE Vodní chlazení", Options.Cooling, 3310, 40),

    Zarizeni("AlzaPower External Sound Card X250 matná černá", Options.SoundCard, 249, 41),
    Zarizeni("Creative Sound Blaster AE-9", Options.SoundCard, 7379, 42),
    Zarizeni("M-Audio M-Track DUO", Options.SoundCard, 1269, 43),
    Zarizeni("Tascam US-2x2HR", Options.SoundCard, 3599, 44),
    Zarizeni("Vention 1-port USB External Sound Card 0.15M Black(OMTP-CTIA)", Options.SoundCard, 199, 45),

    Zarizeni("24'' MISURA MM24DFA", Options.Monitor, 2999, 46),
    Zarizeni("23.6'' MSI MAG 244C", Options.Monitor, 1990, 47),
    Zarizeni("Herní monitor AOC 27G42E", Options.Monitor, 2490, 48),
    Zarizeni("Monitor MSI Pro MP252L", Options.Monitor, 1490, 49),
    Zarizeni("Monitor Xiaomi A27i", Options.Monitor, 1999, 50),

    Zarizeni("", Options.Reproduktor, 0, 51),
    Zarizeni("", Options.Reproduktor, 0, 52),
    Zarizeni("", Options.Reproduktor, 0, 53),
    Zarizeni("", Options.Reproduktor, 0, 54),
    Zarizeni("", Options.Reproduktor, 0, 55),

    Zarizeni("", Options.Sluchátka, 0, 56),
    Zarizeni("", Options.Sluchátka, 0, 57),
    Zarizeni("", Options.Sluchátka, 0, 58),
    Zarizeni("", Options.Sluchátka, 0, 59),
    Zarizeni("", Options.Sluchátka, 0, 60),

    Zarizeni("", Options.Myš, 0, 61),
    Zarizeni("", Options.Myš, 0, 62),
    Zarizeni("", Options.Myš, 0, 63),
    Zarizeni("", Options.Myš, 0, 64),
    Zarizeni("", Options.Myš, 0, 65),

    Zarizeni("", Options.Klávesnice, 0, 66),
    Zarizeni("", Options.Klávesnice, 0, 67),
    Zarizeni("", Options.Klávesnice, 0, 68),
    Zarizeni("", Options.Klávesnice, 0, 69),
    Zarizeni("", Options.Klávesnice, 0, 70),

    Zarizeni("", Options.Kamera, 0, 71),
    Zarizeni("", Options.Kamera, 0, 72),
    Zarizeni("", Options.Kamera, 0, 73),
    Zarizeni("", Options.Kamera, 0, 74),
    Zarizeni("", Options.Kamera, 0, 75),

    Zarizeni("", Options.Volant, 0, 76),
    Zarizeni("", Options.Volant, 0, 77),
    Zarizeni("", Options.Volant, 0, 78),
    Zarizeni("", Options.Volant, 0, 79),
    Zarizeni("", Options.Volant, 0, 80),

    Zarizeni("", Options.Case, 0, 81),
    Zarizeni("", Options.Case, 0, 82),
    Zarizeni("", Options.Case, 0, 83),
    Zarizeni("", Options.Case, 0, 84),
    Zarizeni("", Options.Case, 0, 85),
]

Kosik = []
Nakup = (Stav.HLAVNI, Options.NONE)
validOptions = []
bylSpatne = False

while True:
    match Nakup[0]:
        case Stav.HLAVNI:
            clear()
            prehledKosiku(Kosik)
            print(Text.Hlavni.KategorieVyber)
            print(Text.Hlavni.VypisInfo)
            napsatHlavniVyber()

            uzivatel = input(Text.Hlavni.UzivatelskyInput)

            if uzivatel == "vypis":
                Nakup = (Stav.KONEC, Options.NONE)
                break
            
            for j in validOptions:
                if uzivatel.lower() == j[0].lower():
                    Nakup = (Stav.SIDE, j[1])
                    break
        case Stav.SIDE:
            clear()
            prehledKosiku(Kosik)
            print(Text.Side.SelectOption.replace("%option%", removeOptionPrefix(Nakup[1])))
            print(Text.Side.WriteReturn)

            if bylSpatne:
                print(Text.Side.WrongSelection)
                bylSpatne = False

            for i in ZiskatReference(Nakup[1], Sklad):
                print(Text.Side.ItemWrite.replace("%item%", str(i)))

            userInput = input(Text.Side.UserInput)

            if userInput.lower() == "return" or userInput == "":
                Nakup = (Stav.HLAVNI, Options.NONE)
                continue

            bylSpatne = True

            for i in ZiskatReference(Nakup[1], Sklad):
                if str(i.Id) == userInput:
                    Kosik.append(i)
                    bylSpatne = False
                    continue
        case Stav.KONEC:
            break
clear()
prehledKosiku(Kosik)