from Place import place

class Entity():
    def __init__(self) -> None:
        self.x : float = 0
        self.y : float = 0
        self.height : float = 0
        self.width : float = 0
        self.asset : str = ""
    
    def Show(self) -> str:
        return place(self.asset, self.x, self.y, self.width, self.height)

class EditableEntity(Entity):
    def __init__(self, x : float, y : float, height : float, width : float, asset : str) -> None:
        super().__init__()
        self.x : float = x
        self.y : float = y
        self.height : float = height
        self.width : float = width
        self.asset : str = asset