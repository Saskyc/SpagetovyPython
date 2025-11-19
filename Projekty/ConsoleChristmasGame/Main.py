clear = lambda : print("\n"*100)

"""
Locations
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
Enemies
"""

class Enemy:
    def __init__(self):
        pass

"""
Class option
"""

class Option:
    def __init__(self):
        self.text = "Text"
        self.answer = "Dialogue class here, leave"

"""
Class dialogue
"""

class Dialogue:
    def __init__(self):
        self.mainText = "Main Text"
        self.options = []

"""
Npcs
"""

class Npc:
    def __init__(self):
        self.name = "NPC"
        self.health = 100
        self.dialogues = []
    def talk(self):
        for dialogue in self.dialogues:
            shouldLeave = False
            print(dialogue.mainText)

            while True:
                index = 0
                for option in dialogue.options:
                    print(f" {index}", option.text)
                    index += 1
                user = input("Odpověď? ")
                if not user.isdigit():
                    continue
                digit = int(user)

                if digit >= len(dialogue.options):
                    continue
                answer = dialogue.options[digit].answer

                if answer.lower() == "leave":
                    shouldLeave = True
                break

            if shouldLeave:
                break



class JohnWelcomeNo(Option):
    def __init__(self):
        super().__init__()
        self.text = "Rozmyslel jsem si to"
        self.answer = "leave"

class JohnWelcomeYes(Option):
    def __init__(self):
        super().__init__()
        self.text = "Jasně!"
        self.answer = "mf"

class JohnWelcomeDialogue(Dialogue):
    def __init__(self):
        super().__init__()
        self.mainText = "Yo dobrodruhu! Chceš si něco koupit?"
        self.options = [JohnWelcomeNo(), JohnWelcomeYes()]

class JohnContinueDialogue(Dialogue):
    def __init__(self):
        super().__init__()
        self.mainText = "Tak to je skvělé! Chceš tento meč?"
        self.options = [JohnWelcomeYes(), JohnWelcomeNo()]

class John(Npc):
    def __init__(self):
        super().__init__()
        self.name = "John"
        self.dialogues = [JohnWelcomeDialogue(), JohnContinueDialogue()]


"""
Static player class, because this is singleplayer
"""


class Player:
    Location = None
    Hp = 100

    @staticmethod
    def stats() -> None:
        print(f"Player overview:\n HP: {Player.Hp}\n Location: {Player.Location.name}")


"""
Game class
"""

class Game:
    status = None
    locations = []

    def start(self):
        location = Tavern()
        Game.locations.append(location)
        Player.Location = location

        location = Blacksmith()
        location.locations.append(Game.locations[0])
        location.npcs.append(John())
        Game.locations.append(location)
        Player.Location.locations.append(location)


        Game.status = ""
        self.loop()

    def loop(self):
        while True:
            clear()
            Player.stats()
            print("Command overviews:\n go location\n talk npc\n fight enemy")

            if len(Player.Location.locations) == 0:
                print("No location to go to")
            else:
                print("Locations to go to:")
                for location in Player.Location.locations:
                    print(f" {location.name}")

            if len(Player.Location.npcs) == 0:
                print("No Npcs to talk with")
            else:
                print("Npcs to talk with:")
                for npc in Player.Location.npcs:
                    print(f" {npc.name}")

            user = input("Your action: ")
            if not " " in user:
                print("Invalid input")
                break
            args = user.split(" ")

            match args[0]:
                case "go":
                    for loc in Player.Location.locations:
                        if loc.name == args[1]:
                            Player.Location = loc
                case "talk":
                    for npc in Player.Location.npcs:
                        if npc.name == args[1]:
                            npc.talk()

            print(args[0], "&", args[1])

game = Game()
game.start()
John().talk()