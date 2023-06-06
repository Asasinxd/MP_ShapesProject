from Display.GrapicalDisplay import GrapicalDisplay
from Display.TerminalDisplay import TerminalDisplay
from Display.TextDisplay import TextDisplay
from Shapes.ComplexShape import ComplexShape
from Shapes.Triangle import Triangle
from Shapes.Circle import Circle
from Shapes.Parallelogram import Parallelogram

if __name__ == '__main__':
    w1 = TerminalDisplay()
    w2 = TextDisplay()
    w3 = GrapicalDisplay()

    o1 = Triangle(w=w1, a1=3, a2=2, b1=2, b2=-2)
    o2 = Parallelogram(w=w1, a1=3, a2=2, b1=2, b2=-2)
    o3 = Circle(w=w1, r=2)
    o4 = ComplexShape(w=w1)

    o4.add(o1)
    o4.add(o2)
    o4.add(o3)

    o4.draw()
    o1.draw()
    o2.draw()
    o3.draw()

    o1.changeDisplay(w2)
    o2.changeDisplay(w2)
    o3.changeDisplay(w2)
    o4.changeDisplay(w2)

    o4.draw()
    o1.draw()
    o2.draw()
    o3.draw()

    o1.changeDisplay(w3)
    o2.changeDisplay(w3)
    o3.changeDisplay(w3)
    o4.changeDisplay(w3)

    o1.draw()

    del o1
    del o2
    del o3
    del o4
    del w1
    del w2
