from random import Random
clear = lambda : print("\n"*100)

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

"""
=============================Locations=============================
"""

class Location:
    def __init__(self : "Location"):
        self.name : str = "Location"
        self.locations : list = []
        self.npcs : list = []
        self.enemies : list = []

    @staticmethod
    def remove(self : "Location", npc : "Npc") -> None:
        try:
            self.npcs.remove(npc)
            self.enemies.remove(npc)
        except:
            pass

class Tavern(Location):
    def __init__(self : "Location"):
        super().__init__()
        self.name : str = "Tavern"

class Blacksmith(Location):
    def __init__(self : "Location"):
        super().__init__()
        self.name : str = "Blacksmith"

"""
=============================DATA (Structs)=============================
"""

"""
=============================Entity=============================
"""

class Npc:
    def __init__(self : "Npc", name : str, health : int):
        self.name : str = name
        self.health : int = health

"""
=============================Enemies=============================
"""

class Hostile(Npc):
    def __init__(self : "Npc", reward : int, minDamage : int, maxDamage : int) -> None:
        super().__init__("Enemy", 100)
        self.reward : int = reward
        self.minDamage : int = minDamage
        self.maxDamage : int = maxDamage

    @staticmethod
    def stats(self : "Hostile") -> None:
        print(f"{Color.Regular.Red}Enemy overview:\n- HP: {self.health}")

    @staticmethod
    def printAction() -> None:
        print(f"{Color.Regular.Purple}Akce:\n- Attack\n- Leave\n- Nothing")

    @staticmethod
    def attack(self : "Hostile") -> None:
        if self.health <= 0:
            return
        Player.Hp = Player.Hp - Random.randint(Random(), self.minDamage, self.maxDamage)

    class Evaluator:
        @staticmethod
        def Evaluate(self : "Hostile") -> bool:
            actionResult = Hostile.Evaluator.EvaluateAction(self)
            myselfResult = Hostile.Evaluator.EvaluateMyself(self)
            playerResult = Hostile.Evaluator.EvaluatePlayer(self)

            if actionResult or myselfResult or playerResult:
                return True
            return False

        @staticmethod
        def EvaluateAction(self : "Hostile") -> bool:
            akce = input("Akce: ").lower()
            match akce:
                case "attack":
                    Player.attack(self)
                case "nothing":
                    pass
                case "leave":
                    return True
            return False

        @staticmethod
        def EvaluateMyself(self : "Hostile") -> bool:
            if self.health > 0:
                return False
            
            Player.Coin = Player.Coin + self.reward
            Player.Status.Location.enemies.remove(self)
            return True

        @staticmethod
        def EvaluatePlayer(self : "Hostile") -> bool:
            if Player.Hp > 0:
                return False
            
            Player.removeCoin(self.reward * 2)
            return True

    @staticmethod
    def print(self : "Hostile") -> None:
        clear()
        Player.stats()
        Hostile.stats(self)
        Hostile.printAction()

    @staticmethod
    def fight(self : "Hostile") -> None:
        Player.Status.FightingWith = self
        while True:
            Hostile.print(self)

            if Hostile.Evaluator.Evaluate(self):
                Player.Status.FightingWith = None
                break

            Hostile.attack(self)

class Spider(Hostile):
    def __init__(self : "Hostile"):
        super().__init__(40, 1, 3)
        self.name : str = "Spider"
        self.health : int = 5

"""
=============================Class option=============================
"""

class Option:
    def __init__(self : "Option"):
        self.text : str = "Text"
        self.answer : str = "Dialogue class here, leave"
    def action(self : "Option"):
        pass

"""
=============================Class dialogue=============================
"""

class Dialogue:
    def __init__(self : "Dialogue"):
        self.mainText : str = "Main Text"
        self.options : list[Option] = []

"""
=============================Items=============================
"""

class Item:
    def __init__(self, name : str):
        self.name = name

class Weapon(Item):
    def __init__(self, name : str, damage : int, penetration : int):
        super().__init__(name)
        self.damage = damage
        self.penetration = penetration

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


class Friendly(Npc):
    def __init__(self):
        super().__init__("NPC", 100)
        self.dialogues = []
    def talk(self):
        Player.Status.TalkingWith = self
        for dialogue in self.dialogues:
            clear()
            shouldLeave = False
            print(f"{Color.Regular.Purple}{dialogue.mainText}")

            while True:
                index = 0
                for option in dialogue.options:
                    print(f" {Color.Regular.Red}{index}", f"{Color.Regular.Yellow}{option.text}")
                    index += 1
                user = input(f"{Color.Reset}Odpověď? ")
                if not user.isdigit():
                    continue
                digit = int(user)

                if digit >= len(dialogue.options):
                    continue
                
                option = dialogue.options[digit]
                answer = option.answer

                option.action()

                if answer.lower() == "leave":
                    shouldLeave = True
                break

            if shouldLeave:
                Player.Status.TalkingWith = None
                break

class FullNpc(Friendly, Hostile):
    def __init__(self, name : str, health : int, minDamage : int, maxDamage : int, reward : int):
        self.name = name
        self.health = health
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.reward = reward
        self.dialogues = []

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
=============================Static player class=============================
because this is singleplayer
"""


class Player:
    Hp : int = 100
    Coin : int = 0
    class Status:
        Location : "Location" = None
        TalkingWith : "Friendly" = None
        FightingWith : "Hostile" = None

    class Inventory:
        Items : list[Item] = []
        Armor : list = []
        EquippedWeapon : "Weapon" = None

    @staticmethod
    def removeCoin(number : int) -> None:
        Player.Coin = Player.Coin - number
        if Player.Coin < 0:
            Player.Coin = 0

    def attack(entity : "Npc"):
        entity.health = entity.health - Player.Inventory.EquippedWeapon.damage

    @staticmethod
    def stats() -> None:
        print(f"{Color.Reset}Player overview:\n HP: {Player.Hp}\n Coin: {Player.Coin}\n Location: {Player.Status.Location.name}")


"""
=============================Game class=============================
"""

class Game:
    status = None
    locations = []

    def start() -> None:
        Player.Inventory.EquippedWeapon = Stick()

        location = Tavern()
        Game.locations.append(location)
        Player.Status.Location = location

        location = Blacksmith()
        location.locations.append(Game.locations[0])
        location.npcs.append(John())
        location.npcs.append(JohnDog())
        location.npcs.append(JohnWife())
        

        location.enemies.append(Spider())
        Game.locations.append(location)
        Player.Status.Location.locations.append(location)
        

        Game.status = ""
        Game.loop()

    def loop() -> None:
        while True:
            clear()
            Player.stats()
            print(f"{Color.Regular.Green}Command overviews:\n go location\n talk npc\n fight enemy{Color.Reset}")

            if len(Player.Status.Location.locations) == 0:
                print(f"{Color.Regular.Red}No location to go to")
            else:
                print(f"{Color.Regular.Blue}Locations to go to:")
                index = 0
                for location in Player.Status.Location.locations:
                    print(f" {Color.Bold.Blue}({index}) {location.name}")
                    index += 1

            if len(Player.Status.Location.npcs) == 0:
                print(f"{Color.Regular.Red}No Npcs to talk with")
            else:
                print(f"{Color.Regular.Purple}Npcs to talk with:")
                index = 0
                for npc in Player.Status.Location.npcs:
                    print(f" {Color.Bold.Purple}({index}) {npc.name}")
                    index += 1

            if len(Player.Status.Location.enemies) == 0:
                print(f"{Color.Regular.Red}No Enmies to fight with")
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