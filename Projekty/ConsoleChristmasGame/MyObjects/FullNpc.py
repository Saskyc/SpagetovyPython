

class FullNpc(Friendly, Hostile):
    def __init__(self, name : str, health : int, minDamage : int, maxDamage : int, reward : int) -> None:
        self.name = name
        self.health = health
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.reward = reward
        self.dialogues = []