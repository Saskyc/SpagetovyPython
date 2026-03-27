from ..Attributes import *
from ..Piece import *

@BehaviorClass
class Rook(Piece):
    @Initialization
    def __init__(self : "Rook", position : "Position", isWhite : bool) -> None:
        super().__init__(position, "Rook", "♜", isWhite)
        self.patterns = [
            Patern(True, True, False, Position(0, 1)),
            Patern(True, True, False, Position(0, -1)),
            Patern(True, True, False, Position(1, 0)),
            Patern(True, True, False, Position(-1, 0)),
            ]