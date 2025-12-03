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

import sys

clear = lambda : print("\n"*100)

class Debug:
    def __init__(self : "Debug", message : str):
        print("=======DEBUG/=======")
        print(message)
        print("=======/DEBUG=======")
        input("Leave: ")

        for i in range(4):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")

def DataClass(obj: object) -> object:
    return obj

def StaticClass(obj : object) -> object:
    return obj

def BehaviorClass(obj : object) -> object:
    return obj

def Initialization(obj : object) -> object:
    return obj

def InstanceMethod(obj : object) -> object:
    return obj

@DataClass
class Position:
    @Initialization
    def __init__(self : "Position", x : int | str, y : int) -> None:
        if isinstance(x, str):
            x : int = int(x)
        if isinstance(y, str):
            y : int = int(y)
        self.x : int = x
        self.y : int = y

    @InstanceMethod
    def __eq__(self : "Position", other : "Position") -> bool:
        #Debug(f"Equal position\nSelf: {self}\nOther: {other}\nCond: {self.x == other.x and self.y == other.y}")
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"[{self.x}, {self.y}]"
    
    @InstanceMethod
    def __add__(self : "Position", other : "Position") -> "Position":
        x = self.x + other.x
        y = self.y + other.y
        return Position(x, y)

    @InstanceMethod
    def __sub__(self : "Position", other : "Position") -> "Position":
        x = self.x - other.x
        y = self.y - other.y
        return Position(x, y)

    @InstanceMethod
    def __mul__(self : "Position", other : "Position") -> "Position":
        x = self.x * other.x
        y = self.y * other.y
        return Position(x, y)
    
    @InstanceMethod
    def __truediv__(self : "Position", other : "Position") -> "Position":
        x = self.x / other.x
        y = self.y / other.y
        return Position(x, y)
    
    @InstanceMethod
    def __floordiv__(self : "Position", other : "Position") -> "Position":
        x = self.x // other.x
        y = self.y // other.y
        return Position(x,y)
    
    @InstanceMethod
    def __mod__(self : "Position", other : "Position") -> "Position":
        x = self.x % other.x
        y = self.y % other.y
        return Position(x, y)
    
    @InstanceMethod
    def __str__(self : "Position") -> str:
        return f"[{self.x}, {self.y}]"

    @InstanceMethod
    def OutOfBounds(self : "Position") -> bool:
        Debug(f"Pos: {self}\n1st: {self.x < 1 or self.x > 8}\n2nd: {self.y < 1 or self.y > 8}")
        if self.x < 1 or self.x > 8:
            return False
        if self.y < 1 or self.y > 8:
            return False
        return True

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

@BehaviorClass
class Knight(Piece):
    @Initialization
    def __init__(self : "Pawn", position : "Position", isWhite : bool) -> None:
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

@BehaviorClass
class Rook(Piece):
    @Initialization
    def __init__(self : "Pawn", position : "Position", isWhite : bool) -> None:
        super().__init__(position, "Rook", "♜", isWhite)
        self.patterns = [
            Patern(True, True, False, Position(0, 1)),
            Patern(True, True, False, Position(0, -1)),
            Patern(True, True, False, Position(1, 0)),
            Patern(True, True, False, Position(-1, 0)),
            ]

@BehaviorClass
class Bishop(Piece):
    @Initialization
    def __init__(self : "Pawn", position : "Position", isWhite : bool) -> None:
        super().__init__(position, "Bishop", "♝", isWhite)
        self.patterns = [
            Patern(True, True, False, Position(1, 1)),
            Patern(True, True, False, Position(-1, 1)),
            Patern(True, True, False, Position(1, -1)),
            Patern(True, True, False, Position(-1, -1)),
            ]

@BehaviorClass
class Queen(Piece):
    @Initialization
    def __init__(self : "Pawn", position : "Position", isWhite : bool) -> None:
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

@BehaviorClass
class King(Piece):
    @Initialization
    def __init__(self : "Pawn", position : "Position", isWhite : bool) -> None:
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

@DataClass
class Command:
    @Initialization
    def __init__(self : "Command", inp : str) -> None:
        self.origin = inp
        self.form : list[str] = Command.format(inp)
        self.valid : bool = Command.isValid(inp)
        try:
            self.pos : Position = Command.position(inp)
        except:
            self.pos : Position = Position(0, 0)
        
        try:
            self.x : int = Board.get.Number(self.form[0] + " ")
            try:
                self.y : int = int(self.form[1])
            except:
                self.y : int = -1
        except:
            self.x = -1
            self.y = -1
    @InstanceMethod
    def piece(self : "Command", board : "Board") -> None | Piece:
        mes = "\nPieces\n"
        for p in board.pieces:
            mes += f"- {p.position} | {p.name}\n"
        #Debug(f"Position {self.pos}\n{mes}")
        return board.findPiece(self.pos)
    
    @staticmethod
    def format(inputted : str | list[str]) -> list[str]:
        if isinstance(inputted, list):
            return inputted
        return list(inputted)
    
    @staticmethod
    def isValid(inputted : str | list[str]) -> bool:
        if len(inputted) > 2 or len(inputted) < 1:
            return False
        
        if isinstance(inputted, str):
            inputted = format(inputted)
        try:
            int(inputted[0])
            return False
        except:
            pass
        
        try:
            int(inputted[1])
        except:
            return False
        
        pos : Position = Command.position(inputted)
        Debug(f"Checking position rn: {pos}")
        if not pos.OutOfBounds():
            return False
        return True
    
    @staticmethod
    def position(listed : str | list[str]) -> "Position":
        if isinstance(listed, str):
            listed = format(listed)
        
        x : str = Board.get.Number(listed[0] + " ")
        y : str = listed[1]
        
        x : int = int(x) - 1
        return Position(x, y)

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