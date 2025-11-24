class Color:
    Reset = "\x1b[0m"
    class Regular:
        Black = "\x1b[0;30m"
        Red = "\x1b[0;31m"
        Green = "\x1b[0;32m"
        Yellow = "\x1b[0;33m"
        Blue = "\x1b[0;34m"
        Purple = "\x1b[0;35m"
        Cyan = "\x1b[0;36m"
        White = "\x1b[0;37m"
    class Bold:
        Black = "\x1b[1;30m"
        Red = "\x1b[1;31m"
        Green = "\x1b[1;32m"
        Yellow = "\x1b[1;33m"
        Blue = "\x1b[1;34m"
        Purple = "\x1b[1;35m"
        Cyan = "\x1b[1;36m"
        White = "\x1b[1;37m"
    class Underline:
        Black = "\x1b[4;30m"
        Red = "\x1b[4;31m"
        Green = "\x1b[4;32m"
        Yellow = "\x1b[4;33m"
        Blue = "\x1b[4;34m"
        Purple = "\x1b[4;35m"
        Cyan = "\x1b[4;36m"
        White = "\x1b[4;37m"
    class Background:
        Black = "\x1b[40m"
        Red = "\x1b[4;41m"
        Green = "\x1b[4;42m"
        Yellow = "\x1b[4;43m"
        Blue = "\x1b[4;44m"
        Purple = "\x1b[4;45m"
        Cyan = "\x1b[4;46m"
        White = "\x1b[4;47m"

    class Intensity:
        class High:
            Black = "\x1b[0;90m"
            Red = "\x1b[0;91m"
            Green = "\x1b[0;92m"
            Yellow = "\x1b[0;93m"
            Blue = "\x1b[0;94m"
            Purple = "\x1b[0;95m"
            Cyan = "\x1b[0;96m"
            White = "\x1b[0;97m"

            class Bold:
                Black = "\x1b[1;90"
                Red = "\x1b[1;91m"
                Green = "\x1b[1;92m"
                Yellow = "\x1b[1;93m"
                Blue = "\x1b[1;94m"
                Purple = "\x1b[1;95m"
                Cyan = "\x1b[1;96m"
                White = "\x1b[1;97m"

            class Background:
                Black = "\x1b[1;100m"
                Red = "\x1b[1;101m"
                Green = "\x1b[1;102m"
                Yellow = "\x1b[1;103m"
                Blue = "\x1b[1;104m"
                Purple = "\x1b[1;105m"
                Cyan = "\x1b[1;106m"
                White = "\x1b[1;107m"

class Position:
    def __init__(self : "Position", x : int, y : int) -> None:
        self.x : int = x
        self.y : int = y
    def __eq__(self : "Position", other : "Position") -> bool:
        return self.x == other.x and self.y == other.y

class Piece:
    def __init__(self : "Piece", position : "Position", name : str = "", character : str = "X", isWhite : bool = True) -> None:
        self.name : str = name
        self.character : str = character
        self.position : "Position" = position
        self.side = isWhite

class Pawn(Piece):
    def __init__(self : "Pawn", position : "Position", isWhite : bool) -> None:
        super().__init__(position, "Pawn", "♟", isWhite)


class Board:
    def __init__(self : "Board") -> None:
        self.pieces : list[Piece] = []
        self.pieces.append(Pawn(Position(2, 4), True))
        self.pieces.append(Pawn(Position(3, 4), False))
        self.pieces.append(Pawn(Position(3, 5), True))

    def findPiece(self : "Board", position : "Position") -> "Piece":
        for piece in self.pieces:
            #print(f"[DEBUG] Name {piece.name}")
            if piece.position == position:
                return piece
    @staticmethod
    def getLetter(num : int) -> str:
        match num:
            case 0: return "0"
            case 1: return "A"
            case 2: return "B"
            case 3: return "C"
            case 4: return "D"
            case 5: return "E"
            case 6: return "F"
            case 7: return "G"
            case 8: return "H"
            case 9: return "I"

        return None
    def print(self : "Board") -> None:
        for y in range(9):
            
            line : str = ""

            for x in range(9):
                if x == 0:
                    if y == 0:
                        line += " "
                        continue
                    line += str(y)
                if y == 0:
                    letter : str = Board.getLetter(x)
                    line += letter
                    continue

                pos : Position = Position(x, y)
                piece : Piece = self.findPiece(pos)
                if piece == None:
                    line += " "
                else:
                    if piece.side:
                        line += f"{Color.Reset}{piece.character}{Color.Reset}"
                    else:
                        line += f"{Color.Regular.Black}{piece.character}{Color.Reset}"
                
                #print(f"[X: {relativeX}, Y: {relativeY}]")
            print(line)
            line = ""
        pass
        
board = Board()
board.print()