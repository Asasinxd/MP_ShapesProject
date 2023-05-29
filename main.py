from Display.GrapicalDisplay import GrapicalDisplay
from Display.TextDisplay import TextDisplay
from Shapes.ComplexShape import ComplexShape
from Shapes.Triangle import Triangle
from Shapes.Circle import Circle
from Shapes.Parallelogram import Parallelogram

if __name__ == '__main__':
    o1 = GrapicalDisplay()
    dupa = Circle(w=o1, r=3)
    dupa.draw()
