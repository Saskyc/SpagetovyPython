from .Player import Player
from .Text import Text
from .Text import Color
from .Text import clear

from ..Main import Game

class InfoEachRound:
    
    def pr(player : "Player"):
        clear()
        player.stats()
        Text.print("ComOver", Game.language)

        if len(player.status.Location.locations) == 0:
            print(f"{Color.Regular.Red}No location to go to")
        else:
            print(f"{Color.Regular.Blue}Locations to go to:")
            index = 0
            for location in player.status.Location.locations:
                print(f" {Color.Bold.Blue}({index}) {location.name}")
                index += 1

        if len(player.status.Location.npcs) == 0:
            Text.print("NoNpcs", Game.language)
        else:
            Text.print("SomeNpcs", Game.language)
            index = 0
            for npc in player.status.Location.npcs:
                print(f" {Color.Bold.Purple}({index}) {npc.name}")
                index += 1

        if len(player.status.Location.enemies) == 0:
            print(f"{Color.Regular.Red}No Enemies to fight with")
        else:
            print(f"{Color.Regular.Red}Enemies to fight with:")
            index = 0
            for enemy in player.status.Location.enemies:
                print(f" {Color.Bold.Red}({index}) {enemy.name}")
                index += 1