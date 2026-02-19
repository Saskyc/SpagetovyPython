from hrac import Hrac
from definovaneakce import DefinedAction
from random import Random

class Hra:
    def __init__(self):
        jmeno = input("Jaké je tvé jméno? ")
        self.plr = Hrac(jmeno)
        self.ai = Hrac("AI")
    def loop(self):
        while True:
            self.plr.zacatek()
            
            if self.plr.prohral == True:
                print(f"Vyhral: {self.ai.nazev}")
                break
            
            self.plr.info()
            self.ai.info()
            
            while True:
                if self.plr.nabity > 0:
                    akce = input("Vyber si akci:\nBranit, Utocit, Nabit").lower()
                else:
                    akce = input("Vyber si akci:\nBranit, Nabit").lower()
                if akce == "branit" or akce == "bránit" or "b":
                    self.plr.akce(DefinedAction.Branit, self.ai)
                    break
                if akce == "utocit" or akce == "útočit" or "u" and self.plr.nabity > 0:
                    self.plr.akce(DefinedAction.Utocit, self.ai)
                    break
                if akce == "nabit" or akce == "nabít" or "a":
                    self.plr.akce(DefinedAction.Nabit, self.ai)
                    break
                print("Špatná akce vyber si ještě jednou")
            
            self.ai.zacatek()
            if self.ai.prohral == True:
                print(f"Vyhral: {self.plr.nazev}")
                break
            
            while True:
                if self.plr.nabity > 0:
                    rnd = Random.randint(1, 3)
                    if rnd == 1:
                        self.ai.akce(DefinedAction.Branit, self.plr)
                    if rnd == 2:
                        self.ai.akce(DefinedAction.Utocit, self.plr)
                    if rnd == 3:
                        self.ai.akce(DefinedAction.Nabit, self.plr)
                else:
                    rnd = Random.randint(1, 2)
                    if rnd == 1:
                        self.ai.akce(DefinedAction.Branit, self.plr)
                    if rnd == 2:
                        self.ai.akce(DefinedAction.Nabit, self.plr)