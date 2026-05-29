class BlockedConfiguration:
    def __init__(self, up : bool = False, left : bool = False, down : bool = False, right : bool = False) -> None:
        self.isBlockedUp = up
        self.isBlockedLeft = left
        self.isBlockedDown = down
        self.isBlockedRight = right
    def to_dict(self) -> dict:
        return {
            "up": self.isBlockedUp,
            "left": self.isBlockedLeft,
            "down": self.isBlockedDown,
            "right": self.isBlockedRight,
        }
    @staticmethod
    def from_dict(information : dict) -> "BlockedConfiguration":
        up = information["up"]
        left = information["left"]
        down = information["down"]
        right = information["right"]
        return BlockedConfiguration(up, left, down, right)