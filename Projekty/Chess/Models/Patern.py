from .Attributes import *
from .Position import *
from .Piece import Piece
from .Board import Board

@BehaviorClass
class Patern:
    @Initialization
    def __init__(self : "Patern", agressive : bool, repeat : bool, jump : bool, relative : "Position") -> None:
        self.agressive : bool = agressive
        self.repeat : bool = repeat
        self.relative : Position = relative
        self.jump : bool = jump

    def Usable(self : "Patern", piece : "Piece", board : "Board") -> bool:
        position : Position = piece.position + self.relative
        foundPiece : Piece = board.findPiece(position)
        
        if position.OutOfBounds:
            return False
        
        if foundPiece.isWhite == piece.isWhite:
            return False
        
        if foundPiece != None and not self.agressive:
            return False
        
        return True