from .Position import Position
from .Patern import Patern
from .Attributes import *
from .Board import Board

@BehaviorClass
class Piece:
    @Initialization
    def __init__(self : "Piece", position : "Position", name : str = "", character : str = "X", isWhite : bool = True) -> None:
        self.name : str = name
        self.character : str = character
        self.position : "Position" = position
        self.side : bool = isWhite
        self.isSelected : bool = False
        self.patterns : list[Patern] = []

    @InstanceMethod
    def IsPossibleMove(self : "Piece") -> bool:
        return False

    @InstanceMethod
    def Select(self : "Piece", board : "Board"):
        while True:
            move = input("Pole kam se pohne: ")