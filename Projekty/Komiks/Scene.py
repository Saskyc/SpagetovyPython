from Resolution import Resolution
from Object import Object

class Scene:
    def __init__(self, resolution : Resolution):
        self.width : float = resolution.width
        self.height : float = resolution.height
        self.objects : list[Object] = []

    def add(self, obj : Object):
        self.objects.append(obj)
    
    def clean(self):
        self.objects : list[Object] = []

    def draw(self):
        objects_html = "".join(obj.draw() for obj in self.objects)
        return f"""
        <div class="scene"
            style="
                width: {self.width}px;
                height: {self.height}px;
            ">
            {objects_html}
        </div>
        """
