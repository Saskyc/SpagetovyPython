import math
from typing import Any, Iterator


class number:
    len : int = property(lambda self : len(self))
    def __init__(self):
        number : int = 0
    
    def __init__(self, value : object):
        number : int = int(value)
    
    def __len__(self) -> int:
        return len(str(self))
    def range(self) -> list[int]:
        return range(self.len)
    
    def __iter__(self):
        for u in str(self.number):
            yield int(u)
    
    def __add__(self, val2):
        return number(self.number + val2.number)
    
    
    def __eq__(self : "number", __value: object) -> bool: #Defines behavior for the equality operator, ==.
        return self.number == int(__value)
    def __ne__(self : "number", other : object): #Defines behavior for the inequality operator, !=.
        return self.number != int(other)
    def __lt__(self : "number", other : object): #Defines behavior for the less-than operator, <.
        return self.number < int(other)
    def __gt__(self : "number", other : object): #Defines behavior for the greater-than operator, >.
        return self.number > int(other)
    def __le__(self : "number", other : object): #Defines behavior for the less-than-or-equal-to operator, <=.
        return self.number <= int(other)
    def __ge__(self : "number", other : object): #Defines behavior for the greater-than-or-equal-to operator, >=.
        return self.number >= int(other)
    
    def __abs__(self : "number"): #Implements behavior for the built in abs() function.
        return abs(self.number)
    def __invert__(self : "number") -> int:
        return ~self.number
    def __round__(self : "number", n : int) -> int:
        return round(self.number, n)
    def __floor__(self : "number") -> int:
        return math.floor(self.number)
    def __ceil__(self : "number") -> int:
        return math.ceil(self.number)
    def __trunc__(self : "number") -> int:
        return math.trunc(self.number)
    
    def __sizeof__(self) -> int:
        return len(self)
    
    def __call__(self) -> int:
        return self.number
    
    def __int__(self):
        return self.number
    def __bool__(self):
        return bool(self.number)
    def __float__(self):
        return float(self.number)
    
    def __repr__(self):
        return str(self.number)
    def __str__(self):
        return str(self.number)
    
    def __getitem__(self, key) -> int:
        text = str(self)
        return int(text[key])
    def __setitem__(self, key, value) -> None:
        text = str(self)
        text[key] = value
    def __delitem__(self, key) -> None:
        text = str(self)
        for i in range()
        
        text[key]
        
    def __del__(self):
        del self