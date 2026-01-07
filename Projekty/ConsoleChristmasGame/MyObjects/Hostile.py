from .Npc import Npc
from .Player import Player
from .Text import Color
from random import Random

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