class Command:
    def __init__(self : "Command"):
        pass
    
    def input(self : "Command", message : str) -> str:
        self.userinput = input(message + " ")
        self.process()
        return self.input
    
    def process(self : "Command") -> None:
        if not " " in self.userinput:
            return
        self.args = self.userinput.split(" ")
    def arg(self : "Command", index : int) -> str | None:
        if (len(self.args) -1) < index:
            return None
        return self.args[index]

"""
Test of command.
"""

command = Command()
command.input("Test")
print(f"1: {command.arg(0)}")
print(f"2: {command.arg(1)}")
print(f"3: {command.arg(2)}")
print(f"4: {command.arg(3)}")
print(f"5: {command.arg(4)}")