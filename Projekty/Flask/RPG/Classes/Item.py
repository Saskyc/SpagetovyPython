from .Location import Location

class Item:
    def __init__(self, name : str, location : Location):
        self.name : str = name
        self.location : Location = location