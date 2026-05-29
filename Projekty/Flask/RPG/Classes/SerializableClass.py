class SerializableClass:
    def __init__(self, id : int):
        self.id = id
    def to_dict(self) -> dict:
        return {
            "id" : self.id,
        }