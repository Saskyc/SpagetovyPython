from Models.hrac import Hrac
from Models.definovaneakce import DefinedAction
from random import Random

class Hra:
    def __init__(self):
        jmeno = input("Jaké je tvé jméno? ")
        self.random = Random()
        self.plr = Hrac(jmeno)
        self.ai = Hrac("AI")
        self.kolo = 0
    def loop(self):
        while True:
            self.kolo += 1
            print(f"KOLO: {self.kolo}")
            self.plr.zacatek()
            if self.plr.prohral == True:
                print(f"Vyhral: {self.ai.nazev}")
                break
            
            print("======")
            print("-", self.plr.info())
            print("-", self.ai.info())
            print("======")
            
            while True:
                if self.plr.nabity > 0:
                    akce = input("Vyber si akci\nBranit, Utocit, Nabit: ").lower()
                else:
                    akce = input("Vyber si akci\nBranit, Nabit: ").lower()
                
                vybrana = 0
                
                if akce == "branit" or akce == "bránit" or akce == "b":
                    vybrana = 1
                elif akce == "utocit" or akce == "útočit" or akce == "u":
                    vybrana = 2
                elif akce == "nabit" or akce == "nabít" or akce == "n":
                    vybrana = 3
                
                print(f"Jo {vybrana}")
                
                if vybrana == 1:
                    self.plr.akce(DefinedAction.Branit, self.ai)
                    break
                elif vybrana == 2:
                    self.plr.akce(DefinedAction.Utocit, self.ai)
                    break
                elif vybrana == 3:
                    self.plr.akce(DefinedAction.Nabit, self.ai)
                    break
                else:
                    print("ŠPATNĚ HRÁČ")
            
            self.ai.zacatek()
            if self.ai.prohral == True:
                print(f"Vyhral: {self.plr.nazev}")
                break
            
            while True:
                if self.ai.nabity > 0:
                    rnd = self.random.randint(1, 3)
                    if rnd == 1:
                        self.ai.akce(DefinedAction.Branit, self.plr)
                    elif rnd == 2:
                        self.ai.akce(DefinedAction.Utocit, self.plr)
                    elif rnd == 3:
                        self.ai.akce(DefinedAction.Nabit, self.plr)
                    else:
                        print("AI spatna akce")
                    break
                else:
                    rnd = self.random.randint(1, 2)
                    if rnd == 1:
                        self.ai.akce(DefinedAction.Branit, self.plr)
                    elif rnd == 2:
                        self.ai.akce(DefinedAction.Nabit, self.plr)
                    else:
                        print("AI spatna akce")
                    break

hra = Hra()
hra.loop()