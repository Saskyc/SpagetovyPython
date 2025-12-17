import random
from typing import Tuple

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


class WordleGame():
    def __init__(self, words : list[str]):
        self.guessed : list[tuple[str, str]] = []
        self.words : list[str] = words
        self.wronglyGuessed : str = ""
        self.contains : str = ""
        self.correct : str = ""
        self.word = ""
        pass
    def selectword(self):
        theCh = random.choice(self.words)
        print("The choise of word", theCh)
        self.word = theCh.upper()
    def tryguess(self) -> str:
        inp : str = input("Slovo které hádáš: ").upper().replace(" ", "")

        if len(inp) != 5:
            return ""

        answer : str = ""

        for i in range(len(inp)):
            if inp[i] == self.word[i]:
                if inp[i] not in self.correct:
                    self.correct += inp[i]
                    self.contains.replace(inp[i], "")
                answer += f"{Color.Regular.Green}{inp[i]}{Color.Reset}"
            elif inp[i] in self.word:
                if inp[i] not in self.contains or inp[i] not in self.correct:
                    self.contains += inp[i]
                answer += f"{Color.Regular.Yellow}{inp[i]}{Color.Reset}"
            else:
                if inp[i] not in self.wronglyGuessed:
                    self.wronglyGuessed += inp[i]
                answer += f"{Color.Intensity.High.Black}{inp[i]}{Color.Reset}"
        self.guessed.append((inp, answer))
        return inp
    def line(j : str) -> str:
        return f"{Color.Reset} | {j} {Color.Reset}| \n"
    def print(self):
        clear()
        printed = ""
        self.keyboard()

        for i in self.guessed:
            printed += f"| {i[1]} | \n"
        for i in range(6 - len(self.guessed)):
            printed += "| _____ | \n"
        print(printed)
    def start(self):
        self.selectword()
        self.loop()
    def end(self) -> Tuple[bool, bool]:
        self.print()
        theGuess = self.tryguess()
        if len(self.guessed) == 6:
            return (True, False)
        if theGuess == "":
            return (False, False)
        if theGuess == self.word.upper():
            return (True, True)
        return (False, False)
    def loop(self):
        status : Tuple[bool, bool] = (False, False)
        while True:
            status = self.end()
            if status[0]:
                break
        self.print()
        if status[1] == False:
            print(f"{Color.Regular.Cyan}Slovo bylo: {Color.Regular.Green}{self.word}{Color.Reset}")
    def color(self, letter : str) -> str:
        if letter in self.correct:
            return f"{Color.Regular.Green}{letter}{Color.Reset}"
        elif letter in self.contains:
            return f"{Color.Regular.Yellow}{letter}{Color.Reset}"
        elif letter in self.wronglyGuessed:
            return f"{Color.Intensity.High.Black}{letter}{Color.Reset}"

        return f"{Color.Reset}{letter}{Color.Reset}"
    def keyboard(self) -> None:
        letters = "QWERTZUIOP\nASDFGHJKL \n YXCVBNM  "
        colored = ""
        for i in range(len(letters)):
            colored += self.color(letters[i])
        print(colored + "\n")

theWords : list[str] = [
  "Santa", "Angel", "Merry", "Carol", "Holly", "Jolly", "Snowy", "Frost",
  "Chill", "Feast", "Tinsel", "Wreath", "Gifts", "Cocoa", "Sugar", "Spice",
  "Elves", "Sleigh", "Bells", "Trees", "Pines", "Icily", "Peace", "Joyful",
  "Cheer", "Faith", "Glory", "Birth", "Crate", "Stock", "Socks", "Candy",
  "Treat", "Proud", "Starry", "Shine", "Light", "Snowy", "White", "North",
  "Polar", "Bliss", "Happy", "Fuzzy", "Warmth", "Coals", "Loggy", "Flame",
  "Mitts", "Scarf", "Coats", "Boots", "Crack", "Nippy", "Fires", "Cedar",
  "Chime", "Tunes", "Songs", "Voices", "Peace", "Prays", "Faith", "Cross",
  "Bible", "Birth", "Mange", "Sheep", "Wise", "Kings", "Frank", "Myrrh",
  "Golds", "Stars", "Night", "Silent", "Heard", "Bless", "Grace", "Hope",
  "Noels", "Glads", "Feliz", "Navid", "Jesus", "Christ", "Decor", "Ornam",
  "Glass", "Shiny", "Tonic", "Sweet", "Baked", "Ovens", "Bread", "Pecan",
  "Apple", "Spuds", "Gravy", "Plums", "Raisn", "Dates", "Cream", "Spork",
  "Plates", "Cups", "Napks", "Serve", "Share", "Smile", "Laugh", "Gather",
  "Homes", "Family", "Visit", "Cards", "Notes", "Stamp", "Boxes", "Paper",
  "Taped", "Wraps", "Ribbons", "Bows", "Parcel", "Piled", "Under", "Trees",
  "Await", "Magic", "Dream", "Wishes", "Spark", "Glow", "Fable", "Legnd"
]

while True:
    WordleGame(theWords).start()
    input("Pokračovat")