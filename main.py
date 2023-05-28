from MP_ShapesProject.Display.GrapicalDisplay import GrapicalDisplay
from MP_ShapesProject.Display.TextDisplay import TextDisplay
from MP_ShapesProject.Shapes.ComplexShape import ComplexShape
from MP_ShapesProject.Shapes.Triangle import Triangle
from MP_ShapesProject.Shapes.Circle import Circle
from MP_ShapesProject.Shapes.Parallelogram import Parallelogramm

if __name__ == '__main__':
    o1 = TextDisplay()
    o1.drawCircle(2)

    o2 = GrapicalDisplay()
    print("r = 3")
    o2.drawCircle(3)

    o2.drawTriangle(3, 2, 2, -2)
