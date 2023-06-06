from .Shape import Shape


class Triangle(Shape):
    def __init__(self, w: object, a1: int, a2: int, b1: int, b2: int):
        super().__init__(w)
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2

    def draw(self):
        self.w.drawTriangle(a1=self.a1, a2=self.a2, b1=self.b1, b2=self.b2)
