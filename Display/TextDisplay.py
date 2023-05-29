from .Display import Display


class TextDisplay(Display):
    def drawTriangle(self, a1: int, a2: int, b1: int, b2: int):
        print(f"Drawing a triangle from vectors ({a1}, {a2}), ({b1}, {b2})")

    def drawCircle(self, r: int):
        print(f"Drawing a circle with radius {r}")

    def drawParallelogram(self, a1: int, a2: int, b1: int, b2: int):
        print(f"Drawing a parallelogram from vectors ({a1}, {a2}), ({b1}, {b2})")
