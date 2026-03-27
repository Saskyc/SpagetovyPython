from ..Attributes import *
from ..Piece import *

@BehaviorClass
class Pawn(Piece):
    @Initialization
    def __init__(self : "Pawn", position : "Position", isWhite : bool) -> None:
        super().__init__(position, "Pawn", "♟", isWhite)
        self.patterns = [
            Patern(False, False, False, Position(0, 1)),
            Patern(True, False, False, Position(1, 1)),
            Patern(True, False, False, Position(-1, 1)),
            ]