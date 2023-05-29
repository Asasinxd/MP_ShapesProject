from .Shape import Shape


class ComplexShape(Shape):
    def __init__(self, w: object, a1: int, a2: int, b1: int, b2: int):
        super().__init__(w)
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2

    def add(self):
        pass

    def draw(self):
        pass
