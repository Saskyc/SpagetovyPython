class ObjectBase:
    def __init__(self) -> None:
        self.x : float = 0
        self.y : float = 0
        self.width : float = 100
        self.height : float = 100
        self.image : str = "Cerna"  # image file inside Images folder

    def draw(self) -> str:
        return f"""
        <div class="entity"
            style="
                transform: translate({self.x}px, {self.y}px);
                width: {self.width}px;
                height: {self.height}px;
            ">
            <img src="Images/{self.image}.png">
        </div>
        """
