from .Entity import Entity

class Hrdina(Entity):
    def __init__(self, jmeno):
        super().__init__(0, 0)
        self.jmeno = jmeno