import datetime
import os
from typing import Any

import yaml

from .World import World
from .Hrdina import Hrdina

class SaveManager:
    def saveInFile(folderName : str, fileName : str, contents : Any) -> None:
        base_directory = os.path.dirname(os.path.dirname(__file__))
        saves_directory = os.path.join(base_directory, 'Saves', folderName)

        os.makedirs(saves_directory, exist_ok=True)

        file_path = os.path.join(saves_directory, fileName + '.yaml')

        with open(file_path, 'w') as file:
            yaml.dump(contents, file)

    @staticmethod
    def saveWorld(world : World) -> None:
        information = {
            "locations": [i.to_dict() for i in world.locations],
        }
        folder_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        SaveManager.saveInFile(folder_name, "WorldData", information)

    def savePlayer(player: Hrdina) -> None:
        folder_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        SaveManager.saveInFile(folder_name, "PlayerData", player.to_dict())

    @staticmethod
    def loadWorld(information : dict) -> World:
        pass

    @staticmethod
    def loadPlayer(information : dict) -> Hrdina:
        pass