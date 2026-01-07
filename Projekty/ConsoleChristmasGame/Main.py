from MyObjects.Location import Location
from MyObjects.Npc import Npc
from MyObjects.Text import Color
from MyObjects.Text import Text
from MyObjects.Option import Option
from MyObjects.Dialogue import Dialogue

from MyObjects.Item import Item
from MyObjects.Weapon import Weapon

from random import Random




"""
=============================Locations=============================
"""

class Tavern(Location):
    def __init__(self : "Location"):
        super().__init__()
        self.name : str = "Tavern"

class Blacksmith(Location):
    def __init__(self : "Location"):
        super().__init__()
        self.name : str = "Blacksmith"

class Cesta(Location):
    def __init__(self : "Location"):
        super().__init__()
        self.name : str = "Cesta"

class Cave(Location):
    def __init__(self : "Location"):
        super().__init__()
        self.name : str = "Cave"

"""
=============================Enemies=============================
"""

class Spider(Hostile):
    def __init__(self : "Hostile"):
        super().__init__(40, 1, 3)
        self.name : str = "Spider"
        self.health : int = 5

class Zombie(Hostile):
    def __init__(self : "Hostile"):
        super().__init__(60, 5, 15)
        self.name : str = "Zombie"
        self.health : int = 20

"""
=============================Items=============================
"""



class Stick(Weapon):
    def __init__(self):
        super().__init__("Stick", 1, 0)

class ShortWoodenSword(Weapon):
    def __init__(self):
        super().__init__("Wooden Short Sword", 1, 1)

class ShortWoodenSword(Weapon):
    def __init__(self):
        super().__init__("Wooden Long Sword", 3, 2)

class ShortStoneSword(Weapon):
    def __init__(self):
        super().__init__("Stone Short Sword", 5, 3)

class LongStoneSword(Weapon):
    def __init__(self):
        super().__init__("Stone Long Sword", 7, 6)

class ShortIronSword(Weapon):
    def __init__(self):
        super().__init__("Stone Short Sword", 6, 5)

class LongIronSword(Weapon):
    def __init__(self):
        super().__init__("Stone Long Sword", 9, 7)

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

class Game:
    status = None
    locations = []
    language = Text.lang.English

    @staticmethod
    def start() -> None:
        Player.Inventory.EquippedWeapon = Stick()

        location = Tavern()
        Game.locations.append(location)
        Player.Status.Location = location

        location = Blacksmith()
        Game.locations.append(location)

        location.locations.append(Game.locations[0])
        Game.locations[0].locations.append(location)
        location.npcs.append(John())
        location.npcs.append(JohnDog())
        location.npcs.append(JohnWife())

        location = Cesta()
        Game.locations.append(location)
        location.locations.append(Game.locations[0])
        Game.locations[0].locations.append(location)
        location.enemies.append(Spider())
        location.enemies.append(Spider())
        location.enemies.append(Zombie())
        location.enemies.append(Spider())
        location.enemies.append(Spider())
        

        Game.status = ""
        Game.loop()

    @staticmethod
    def loop() -> None:
        while True:
            clear()
            Player.stats()
            Text.print("ComOver", Game.language)

            if len(Player.Status.Location.locations) == 0:
                print(f"{Color.Regular.Red}No location to go to")
            else:
                print(f"{Color.Regular.Blue}Locations to go to:")
                index = 0
                for location in Player.Status.Location.locations:
                    print(f" {Color.Bold.Blue}({index}) {location.name}")
                    index += 1

            if len(Player.Status.Location.npcs) == 0:
                Text.print("NoNpcs", Game.language)
            else:
                Text.print("SomeNpcs", Game.language)
                index = 0
                for npc in Player.Status.Location.npcs:
                    print(f" {Color.Bold.Purple}({index}) {npc.name}")
                    index += 1

            if len(Player.Status.Location.enemies) == 0:
                print(f"{Color.Regular.Red}No Enemies to fight with")
            else:
                print(f"{Color.Regular.Red}Enemies to fight with:")
                index = 0
                for enemy in Player.Status.Location.enemies:
                    print(f" {Color.Bold.Red}({index}) {enemy.name}")
                    index += 1

            user = input(f"{Color.Regular.Blue}Your action: ")
            if not " " in user:
                continue
            args = user.split(" ")

            index = 0
            match args[0]:
                case "go":
                    for loc in Player.Status.Location.locations:
                        if loc.name == args[1] or str(index) == args[1]:
                            Player.Status.Location = loc
                            break
                        index += 1
                case "talk":
                    for npc in Player.Status.Location.npcs:
                        if npc.name == args[1] or str(index) == args[1]:
                            Friendly.talk(npc)
                            break
                        index += 1
                case "fight":
                    for enemy in Player.Status.Location.enemies:
                        if enemy.name == args[1] or str(index) == args[1]:
                            Hostile.fight(enemy)
                            break
                        index += 1


Game.start()