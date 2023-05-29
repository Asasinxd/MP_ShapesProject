from Shapes.Shape import Shape


class Circle(Shape):
    def __init__(self, w: object, r: int):
        super().__init__(w)
        self.r = r

    def draw(self):
        self.w.drawCircle(self.r)
