from .Attributes import *
from .Position import Position
from .Piece import Piece
from .Debug import Debug
from .Board import Board

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