from ..Attributes import *
from ..Piece import *

@BehaviorClass
class Knight(Piece):
    @Initialization
    def __init__(self : "Knight", position : "Position", isWhite : bool) -> None:
        super().__init__(position, "Knight", "♞", isWhite)
        self.patterns = [
            Patern(True, False, True, Position(1, 2)),
            Patern(True, False, True, Position(-1, 2)),
            
            Patern(True, False, True, Position(1, -2)),
            Patern(True, False, True, Position(-1, -2)),
            
            Patern(True, False, True, Position(-2, 1)),
            Patern(True, False, True, Position(2, 1)),
            
            Patern(True, False, True, Position(-2, -1)),
            Patern(True, False, True, Position(2, -1)),
            ]