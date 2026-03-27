from ..Attributes import *
from ..Piece import *

@BehaviorClass
class King(Piece):
    @Initialization
    def __init__(self : "King", position : "Position", isWhite : bool) -> None:
        super().__init__(position, "King", "♚", isWhite)
        self.patterns = [
            Patern(True, False, False, Position(1, 1)),
            Patern(True, False, False, Position(0, 1)),
            Patern(True, False, False, Position(-1, 1)),
            
            Patern(True, False, False, Position(1, 0)),
            Patern(True, False, False, Position(-1, 0)),
            
            Patern(True, False, False, Position(1, -1)),
            Patern(True, False, False, Position(0, -1)),
            Patern(True, False, False, Position(-1, -1)),
            ]