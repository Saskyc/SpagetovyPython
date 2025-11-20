from random import Random

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



clear = lambda : print("\n"*100)

"""
=============================Locations=============================
"""

class Location:
    def __init__(self):
        self.locations = []
        self.name = "Location"
        self.npcs = []
        self.enemies = []

class Tavern(Location):
    def __init__(self):
        super().__init__()
        self.name = "Tavern"

class Blacksmith(Location):
    def __init__(self):
        super().__init__()
        self.name = "Blacksmith"

"""
=============================DATA (Structs)=============================
"""

"""
=============================Enemies=============================
"""

class Enemy:
    def __init__(self, name : str, hp : int, reward : int, minDamage : int, maxDamage : int):
        self.name = name
        self.hp = hp
        self.reward = reward
        self.minDamage = minDamage
        self.maxDamage = maxDamage

    @staticmethod
    def stats(self) -> None:
        print(f"{Color.Regular.Red}Enemy overview:\n- HP: {self.hp}")

    def attack(self) -> None:
        Player.Hp = Player.Hp - Random.randint(Random(), self.minDamage, self.maxDamage)

    def fight(self) -> None:
        while True:
            leaveFight = False
            clear()
            Player.stats()
            Enemy.stats(self)
            print(f"{Color.Regular.Purple}Akce:\n- Attack\n- Leave\n- Nothing")

            akce = input("Akce: ").lower()
            match akce:
                case "attack":
                    self.hp = self.hp - Player.Inventory.EquippedWeapon.damage
                case "nothing":
                    pass
                case "leave":
                    leaveFight = True
            
            if self.hp <= 0:
                Player.Coin = Player.Coin + self.reward
                Player.Location.enemies.remove(self)
                leaveFight = True
            
            if self.hp > 0:
                Enemy.attack(self)

            if Player.Hp <= 0:
                Player.Hp = 100
                leaveFight = True
                Player.removeCoin(self.reward * 2)
            
           

            if leaveFight:
                break

class Spider(Enemy):
    def __init__(self):
        super().__init__("Spider", 5, 40, 1, 3)

"""
=============================Class option=============================
"""

class Option:
    def __init__(self):
        self.text = "Text"
        self.answer = "Dialogue class here, leave"
    def action(self):
        pass

"""
=============================Class dialogue=============================
"""

class Dialogue:
    def __init__(self):
        self.mainText = "Main Text"
        self.options = []

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

class Npc:
    def __init__(self):
        self.name = "NPC"
        self.health = 100
        self.dialogues = []
    def talk(self):
        for dialogue in self.dialogues:
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
                break

class John(Npc):
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

class JohnWife(Npc):
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

"""
=============================Static player class=============================
because this is singleplayer
"""


class Player:
    Location = None
    Hp = 100
    Coin = 0
    class Inventory:
        Items = []
        Armor = []
        EquippedWeapon = None

    @staticmethod
    def removeCoin(number : int) -> None:
        Player.Coin = Player.Coin - number
        if Player.Coin < 0:
            Player.Coin = 0

    @staticmethod
    def stats() -> None:
        print(f"{Color.Reset}Player overview:\n HP: {Player.Hp}\n Coin: {Player.Coin}\n Location: {Player.Location.name}")


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
        Player.Location = location

        location = Blacksmith()
        location.locations.append(Game.locations[0])
        location.npcs.append(John())
        location.npcs.append(JohnWife())
        location.enemies.append(Spider())
        Game.locations.append(location)
        Player.Location.locations.append(location)
        

        Game.status = ""
        Game.loop()

    def loop():
        while True:
            clear()
            Player.stats()
            print(f"{Color.Regular.Green}Command overviews:\n go location\n talk npc\n fight enemy{Color.Reset}")

            if len(Player.Location.locations) == 0:
                print(f"{Color.Regular.Red}No location to go to")
            else:
                print(f"{Color.Regular.Blue}Locations to go to:")
                index = 0
                for location in Player.Location.locations:
                    print(f" {Color.Bold.Blue}({index}) {location.name}")
                    index += 1

            if len(Player.Location.npcs) == 0:
                print(f"{Color.Regular.Red}No Npcs to talk with")
            else:
                print(f"{Color.Regular.Purple}Npcs to talk with:")
                index = 0
                for npc in Player.Location.npcs:
                    print(f" {Color.Bold.Purple}({index}) {npc.name}")
                    index += 1

            if len(Player.Location.enemies) == 0:
                print(f"{Color.Regular.Red}No Enmies to fight with")
            else:
                print(f"{Color.Regular.Red}Enemies to fight with:")
                index = 0
                for enemy in Player.Location.enemies:
                    print(f" {Color.Bold.Red}({index}) {enemy.name}")
                    index += 1

            user = input(f"{Color.Regular.Blue}Your action: ")
            if not " " in user:
                continue
            args = user.split(" ")

            index = 0
            match args[0]:
                case "go":
                    for loc in Player.Location.locations:
                        if loc.name == args[1] or str(index) == args[1]:
                            Player.Location = loc
                            break
                        index += 1
                case "talk":
                    for npc in Player.Location.npcs:
                        if npc.name == args[1] or str(index) == args[1]:
                            npc.talk()
                            break
                        index += 1
                case "fight":
                    for enemy in Player.Location.enemies:
                        if enemy.name == args[1] or str(index) == args[1]:
                            enemy.fight()
                            break
                        index += 1


Game.start()