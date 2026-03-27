from Models.Position import Position
from Models.Attributes import *
from Models.Debug import *















    















@BehaviorClass
class Board:
    @Initialization
    def __init__(self : "Board") -> None:
        self.pieces : list[Piece] = []
        self.selected : Piece | None = None
        self.pieces.append(Knight(Position(2, 4), True))
        self.pieces.append(Pawn(Position(3, 4), False))
        self.pieces.append(Pawn(Position(3, 5), True))

    @InstanceMethod
    def findPiece(self : "Board", position : "Position") -> Piece | None:
        for piece in self.pieces:
            #print(f"[DEBUG] Name {piece.name}")
            if piece.position == position:
                return piece
        return None

    @staticmethod
    def OutOfBounds(position : "Position") -> bool:
        return position.OutOfBounds

    @StaticClass
    class get:
        tuples : list[(str, int)] = [
            ("A ", 1),
            ("B ", 2),
            ("C ", 3),
            ("D ", 4),
            ("E ", 5),
            ("F ", 6),
            ("G ", 7),
            ("H ", 8),
            ("I ", 9),
        ]

        @staticmethod
        def Letter(num : int) -> str | None:
            for tup in Board.get.tuples:
                if num == tup[1]:
                    return tup[0]
            return None

        @staticmethod
        def Number(letter : str) -> int | None:
            for tup in Board.get.tuples:
                if letter == tup[0]:
                    return tup[1]
            return None

    @InstanceMethod
    def print(self : "Board") -> None:
        for y in range(9):
            line : str = ""

            for x in range(9):
                if x == 0:
                    if y == 0:
                        line += "  "
                        continue
                    line += str(y)
                if y == 0:
                    letter : str = Board.get.Letter(x)
                    line += letter
                    continue

                pos : Position = Position(x, y)
                piece : Piece = self.findPiece(pos)
                if piece == None:
                    line += "  "
                else:
                    if piece.side:
                        line += f"{Color.Reset}{piece.character}{Color.Reset} "
                    else:
                        line += f"{Color.Regular.Black}{piece.character}{Color.Reset} "
                
                #print(f"[X: {relativeX}, Y: {relativeY}]")
            print(line)
            line = ""
        
board = Board()



while True:
    clear()
    board.print()
    select : str = input("What piece are you selecting: ")
    command : Command = Command(select)
    
    if not command.isValid:
        continue
    
    #print(command.x)
    #print(command.y)
    #print(command.pos)
    
    piece : Piece | None = command.piece(board)
    while True:
        if piece == None:
            break
        Debug(f"Piece is: {piece.character}")
        aCommand : Command = Command(input("Move: "))
        Debug(f"Moving piece\nV: {aCommand.isValid}\nP: {aCommand.pos}")
        if not aCommand.isValid:
            break
        
        
        piece.position = aCommand.pos
        break