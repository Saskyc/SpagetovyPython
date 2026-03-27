from ..Attributes import *
from ..Piece import *

@BehaviorClass
class Bishop(Piece):
    @Initialization
    def __init__(self : "Bishop", position : "Position", isWhite : bool) -> None:
        super().__init__(position, "Bishop", "♝", isWhite)
        self.patterns = [
            Patern(True, True, False, Position(1, 1)),
            Patern(True, True, False, Position(-1, 1)),
            Patern(True, True, False, Position(1, -1)),
            Patern(True, True, False, Position(-1, -1)),
            ]