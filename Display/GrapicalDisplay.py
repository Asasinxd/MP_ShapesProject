from .Display import Display
from Exceptions.MyExceptions import MyExceptions
import matplotlib.pyplot as plt
import numpy as np

class GrapicalDisplay(Display):

    def drawTriangle(self, a1: int, a2: int, b1: int, b2: int):
        MyExceptions.validInput(a1, a2, b1, b2)

        vertices = np.array([[0, 0], [a1, a2], [b1, b2], [0, 0]])

        x = vertices[:, 0]
        y = vertices[:, 1]

        plt.plot(x, y, 'r')
        plt.fill(x, y, 'r', alpha=0.3)

        plt.xlim(min(x) - 1, max(x) + 1)
        plt.ylim(min(y) - 1, max(y) + 1)

        plt.show()

    def drawCircle(self, r: int):
        MyExceptions.validInputCircle(r)

        theta = np.linspace(0, 2 * np.pi, 100)
        x = r * np.cos(theta)
        y = r * np.sin(theta)

        plt.plot(x, y, 'r')
        plt.fill(x, y, 'r', alpha=0.3)

        plt.xlim(-r - 1, r + 1)
        plt.ylim(-r - 1, r + 1)

        plt.show()


    def drawParallelogram(self, a1: int, a2: int, b1: int, b2: int):
        MyExceptions.validInput(a1, a2, b1, b2)

        vertices = np.array([[0, 0], [a1, a2], [a1 + b1, a2 + b2], [b1, b2], [0, 0]])

        x = vertices[:, 0]
        y = vertices[:, 1]

        plt.plot(x, y, 'r')
        plt.fill(x, y, 'r', alpha=0.3)

        plt.xlim(min(x) - 1, max(x) + 1)
        plt.ylim(min(y) - 1, max(y) + 1)

        for i, txt in enumerate(vertices):
            plt.annotate(f'({txt[0]}, {txt[1]})', (txt[0], txt[1]), textcoords="offset points", xytext=(-10, 5),
                         ha='center')

        plt.show()
