from .Display import Display

class TextDisplay(Display):
    def drawTriangle(self, a1, a2, b1, b2):
        print(f"Drawing a triangle from vectors ({a1}, {a2}), ({b1}, {b2})")

    def drawCircle(self, r):
        print(f"Drawing a circle with radius {r}")

    def drawParallelogramm(self, a1, a2, b1, b2):
        print(f"Drawing a parallelogram from vectors ({a1}, {a2}), ({b1}, {b2})")