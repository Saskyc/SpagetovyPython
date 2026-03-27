from ..Attributes import *
from ..Piece import *

@BehaviorClass
class Queen(Piece):
    @Initialization
    def __init__(self : "Queen", position : "Position", isWhite : bool) -> None:
        super().__init__(position, "Queen", "♛", isWhite)
        self.patterns = [
            Patern(True, True, False, Position(0, 1)),
            Patern(True, True, False, Position(0, -1)),
            Patern(True, True, False, Position(1, 0)),
            Patern(True, True, False, Position(-1, 0)),
            
            Patern(True, True, False, Position(1, 1)),
            Patern(True, True, False, Position(-1, 1)),
            Patern(True, True, False, Position(1, -1)),
            Patern(True, True, False, Position(-1, -1)),
            ]