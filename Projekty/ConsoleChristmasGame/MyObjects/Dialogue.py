from .Option import Option
class Dialogue:
    def __init__(self : "Dialogue"):
        self.mainText : str = "Main Text"
        self.options : list[Option] = []

Dialogue()