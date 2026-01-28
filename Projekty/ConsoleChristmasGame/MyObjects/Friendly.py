from .Npc import Npc
from .Player import Player
from .Text import clear
from .Text import Color

class Friendly(Npc):
    def __init__(self):
        super().__init__("NPC", 100)
        self.dialogues = []
    def talk(self, player : "Player"):
        player.status.TalkingWith = self
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
                player.status.TalkingWith = None
                break