from MyObjects.Location import Location
from MyObjects.Player import Player

from MyObjects.Option import Option
from MyObjects.Dialogue import Dialogue

from MyObjects.Item import Item
from MyObjects.Weapon import Weapon

from MyObjects.Text import *

from MyObjects.Friendly import Friendly
from MyObjects.Hostile import Hostile
from MyObjects.FullNpc import FullNpc

"""
=============================Npcs=============================
"""

class John(Friendly):
    class BlackSmithShop:
        Items = [ShortIronSword, LongIronSword]

    class DoNot(Option):
        def __init__(self):
            super().__init__()
            self.text = "Rozmyslel jsem si to"
            self.answer = "leave"

    class GoToTheShop(Option):
        def __init__(self):
            super().__init__()
            self.text = "Co je k nabídce?"
            self.answer = ""
        
        def action(self):
            while True:
                clear()
                
                pass

    class JDialogue(Dialogue):
        def __init__(self):
            super().__init__()
            self.mainText = "Yo dobrodruhu! Chceš si něco koupit?"
            self.options = [
                John.GoToTheShop(),
                John.DoNot(), 
                ]

    def __init__(self):
        super().__init__()
        self.name = "John"
        self.dialogues = [
            John.JDialogue(), 
            ]

class JohnWife(Friendly):
    class First(Dialogue):
        class Why(Option):
            def __init__(self):
                super().__init__()
                self.text = "Z jakého důvodu?"
                self.answer = "Continue"
        class Leave(Option):
            def __init__(self):
                super().__init__()
                self.text = "Ty jsi ale pizda"
                self.answer = "leave"

        def __init__(self):
            super().__init__()
            self.mainText = "Vítej dobrodruhu, John mě tak sere"
            self.options = [
                JohnWife.First.Why, 
                JohnWife.First.Leave
            ]

    def __init__(self):
        super().__init__()
        self.name = "Johnova žena"
        self.dialogues = [
            JohnWife.First(),
            ]

class JohnDog(FullNpc):
    class OnlyDialogue(Dialogue):
        class Pet(Option):
            def __init__(self):
                super().__init__()
                self.text = "Pohladit"
                self.answer = "leave"
            def action(self):
                while True:
                    print(f"{Color.Regular.Green}Rafran šťastně vrtí ocasem")
                    input("...: ")
                    break
        class Boom(Option):
            def __init__(self):
                super().__init__()
                self.text = "Bouchnout Rafana"
                self.answer = "leave"
            def action(self):
                Player.Status.TalkingWith.fight()
        class Leave(Option):
            def __init__(self):
                super().__init__()
                self.text = "Nechat Rafana šťastně spát"
                self.answer = "leave"
        def __init__(self):
            super().__init__()
            self.mainText = "Rafan šťastně spí v rohu"
            self.options = [
                JohnDog.OnlyDialogue.Pet(),
                JohnDog.OnlyDialogue.Boom(),
                JohnDog.OnlyDialogue.Leave(),
            ]

    def __init__(self):
        super().__init__("Rafan", 99999999999, 99999999999, 999999999999, 0)
        self.dialogues = [JohnDog.OnlyDialogue()]

class Vaclav(Friendly):
    class Predstaveni(Dialogue):
        pass
    
    def __init__(self):
        super().__init__()
        self.name = "Sír Lajky"
        self.health = 300
        self.dialogues = []

"""
=============================Game class=============================
"""



game = Game()
game.start()