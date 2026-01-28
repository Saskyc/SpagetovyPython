from MyObjects.Location import Location
from MyObjects.Player import Player

from MyObjects.Option import Option
from MyObjects.Dialogue import Dialogue

from MyObjects.Item import Item
from MyObjects.Weapon import Weapon

from MyObjects.Text import Color
from MyObjects.Text import Text
from MyObjects.Text import clear

from MyObjects.Friendly import Friendly
from MyObjects.Hostile import Hostile
from MyObjects.FullNpc import FullNpc

class Game:
    def __init__(self : "Game"):
        self.player : "Player" = Player()
        status = None
        locations = []
        language = Text.lang.English

    def start(self : "Game") -> None:
        self.player.inventory.EquippedWeapon = Stick()

        location = Tavern()
        self.locations.append(location)
        self.player.status.Location = location

        location = Blacksmith()
        self.locations.append(location)

        location.locations.append(Game.locations[0])
        self.locations[0].locations.append(location)
        location.npcs.append(John())
        location.npcs.append(JohnDog())
        location.npcs.append(JohnWife())

        location = Cesta()
        self.locations.append(location)
        location.locations.append(Game.locations[0])
        self.locations[0].locations.append(location)
        location.enemies.append(Spider())
        location.enemies.append(Spider())
        location.enemies.append(Zombie())
        location.enemies.append(Spider())
        location.enemies.append(Spider())
        

        self.status = ""
        self.loop()

    def loop(self : "Game") -> None:
        while True:
            user = input(f"{Color.Regular.Blue}Your action: ")
            if not " " in user:
                continue
            args = user.split(" ")

            index = 0
            match args[0]:
                case "go":
                    for loc in self.player.status.Location.locations:
                        if loc.name == args[1] or str(index) == args[1]:
                            self.player.status.Location = loc
                            break
                        index += 1
                case "talk":
                    for npc in self.player.status.Location.npcs:
                        if npc.name == args[1] or str(index) == args[1]:
                            Friendly.talk(npc, self.player)
                            break
                        index += 1
                case "fight":
                    for enemy in self.player.status.Location.enemies:
                        if enemy.name == args[1] or str(index) == args[1]:
                            Hostile.fight(enemy, self.player)
                            break
                        index += 1
