from .Display import Display
from Exceptions.MyExceptions import MyExceptions

class TextDisplay(Display):
    def drawTriangle(self, a1: int, a2: int, b1: int, b2: int):
        MyExceptions.validInput(a1=a1, a2=a2, b1=b1, b2=b2)
        print(f"Drawing a triangle from vectors ({a1}, {a2}), ({b1}, {b2})")

    def drawCircle(self, r: int):
        MyExceptions.validInputCircle(r=r)
        print(f"Drawing a circle with radius {r}")

    def drawParallelogram(self, a1: int, a2: int, b1: int, b2: int):
        MyExceptions.validInput(a1=a1, a2=a2, b1=b1, b2=b2)
        print(f"Drawing a parallelogram from vectors ({a1}, {a2}), ({b1}, {b2})")
