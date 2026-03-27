from .Attributes import *
from .Debug import Debug

@DataClass
class Position:
    @Initialization
    def __init__(self : "Position", x : int | str, y : int) -> None:
        if isinstance(x, str):
            x : int = int(x)
        if isinstance(y, str):
            y : int = int(y)
        self.x : int = x
        self.y : int = y

    @InstanceMethod
    def __eq__(self : "Position", other : "Position") -> bool:
        #Debug(f"Equal position\nSelf: {self}\nOther: {other}\nCond: {self.x == other.x and self.y == other.y}")
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"[{self.x}, {self.y}]"
    
    @InstanceMethod
    def __add__(self : "Position", other : "Position") -> "Position":
        x = self.x + other.x
        y = self.y + other.y
        return Position(x, y)

    @InstanceMethod
    def __sub__(self : "Position", other : "Position") -> "Position":
        x = self.x - other.x
        y = self.y - other.y
        return Position(x, y)

    @InstanceMethod
    def __mul__(self : "Position", other : "Position") -> "Position":
        x = self.x * other.x
        y = self.y * other.y
        return Position(x, y)
    
    @InstanceMethod
    def __truediv__(self : "Position", other : "Position") -> "Position":
        x = self.x / other.x
        y = self.y / other.y
        return Position(x, y)
    
    @InstanceMethod
    def __floordiv__(self : "Position", other : "Position") -> "Position":
        x = self.x // other.x
        y = self.y // other.y
        return Position(x,y)
    
    @InstanceMethod
    def __mod__(self : "Position", other : "Position") -> "Position":
        x = self.x % other.x
        y = self.y % other.y
        return Position(x, y)
    
    @InstanceMethod
    def __str__(self : "Position") -> str:
        return f"[{self.x}, {self.y}]"

    @InstanceMethod
    def OutOfBounds(self : "Position") -> bool:
        Debug(f"Pos: {self}\n1st: {self.x < 1 or self.x > 8}\n2nd: {self.y < 1 or self.y > 8}")
        if self.x < 1 or self.x > 8:
            return False
        if self.y < 1 or self.y > 8:
            return False
        return True