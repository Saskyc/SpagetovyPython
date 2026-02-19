from ObjectBase import ObjectBase
from Vector2 import Vector2
from Resolution import Resolution

class Object(ObjectBase):
    def __init__(self, position : Vector2, resolution : Resolution, image : str) -> None:
        super().__init__()
        self.x : float = position.x
        self.y : float = position.y
        self.width : float = resolution.width
        self.height : float = resolution.height
        self.image : str = image

obj = Object(Vector2(100, 100), Resolution(50, 100), "Cerna")
print(obj.draw())