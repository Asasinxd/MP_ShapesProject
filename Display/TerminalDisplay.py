from .Display import Display
from Exceptions.MyExceptions import MyExceptions

class TerminalDisplay(Display):

    def is_point_in_triangle(self, x: int, y: int, x1: int, y1: int, a1: int, a2: int, b1: int, b2: int) -> bool:
        '''
        Function checks if point is included in triangle
        :param x: x value of current point
        :param y: y value of current point
        :param x1: x-coordinate of triangle
        :param y1: y-coordinate of triangle
        :param a1: positive integer higher then 0, x value of 'a' vector
        :param a2: positive integer higher then 0, y value of 'a' vector
        :param b1: positive integer higher then 0, x value of 'b' vector
        :param b2: negative integer lover then 0, y value of 'b' vector
        :return: bool
        '''

        area_triangle = abs((x1 * (a2 - b2) + a1 * (b2 - y1) + b1 * (y1 - a2)) / 2.0)
        area_sub_triangle1 = abs((x * (y1 - a2) + x1 * (a2 - y) + a1 * (y - y1)) / 2.0)
        area_sub_triangle2 = abs((x * (a2 - b2) + a1 * (b2 - y) + b1 * (y - a2)) / 2.0)
        area_sub_triangle3 = abs((x * (b2 - y1) + b1 * (y1 - y) + x1 * (y - b2)) / 2.0)

        return area_triangle == area_sub_triangle1 + area_sub_triangle2 + area_sub_triangle3

    def drawTriangle(self, a1: int, a2: int, b1: int, b2: int):
        '''
        Function draw triangle in command line using 't' character
        :param a1: positive integer higher then 0, x value of 'a' vector
        :param a2: positive integer higher then 0, y value of 'a' vector
        :param b1: positive integer higher then 0, x value of 'b' vector
        :param b2: negative integer lover then 0, y value of 'b' vector
        :return: None
        '''

        MyExceptions.validInput(a1, a2, b1, b2)
        min_x = min(0, a1, b1)
        max_x = max(0, a1, b1)
        min_y = min(0, a2, b2)
        max_y = max(0, a2, b2)

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if self.is_point_in_triangle(x, y, 0, 0, a1, a2, b1, b2):
                    print("t", end='')
                else:
                    print(' ', end='')
            print()

    def drawCircle(self, r: int):
        '''
        Function draw circle in command line using 'c' character
        :param r: positive integer higher then, circle radius
        :return: None
        '''

        MyExceptions.validInputCircle(r)

        diameter = int(r*2)

        radius = diameter / 2 - .5
        r = (radius + .25) ** 2 + 1

        result = ''

        for i in range(diameter):
            y = (i - radius) ** 2
            for j in range(diameter):
                x = (j - radius) ** 2
                if x + y <= r:
                    result = result + 'c  '
                else:
                    result = result + '   '
            result = result + '\n'

        print(result)

    def is_point_in_parallelogram(self, x, y, a1, a2, b1, b2):
        '''
        Function checks if point is included in parallelogram
        :param x: x value of current point
        :param y: y value of current point
        :param a1: positive integer higher then 0, x value of 'a' vector
        :param a2: positive integer higher then 0, y value of 'a' vector
        :param b1: positive integer higher then 0, x value of 'b' vector
        :param b2: negative integer lover then 0, y value of 'b' vector
        :return: bool
        '''
        p1 = (0, 0)
        p2 = (a1, a2)
        p3 = (a1 + b1, a2 + b2)
        p4 = (b1, b2)

        area_triangle1 = abs((x * (p2[1] - p1[1]) + p1[0] * (y - p2[1]) + p2[0] * (p1[1] - y)) / 2.0)
        area_triangle2 = abs((x * (p3[1] - p2[1]) + p2[0] * (y - p3[1]) + p3[0] * (p2[1] - y)) / 2.0)
        area_triangle3 = abs((x * (p4[1] - p3[1]) + p3[0] * (y - p4[1]) + p4[0] * (p3[1] - y)) / 2.0)
        area_triangle4 = abs((x * (p1[1] - p4[1]) + p4[0] * (y - p1[1]) + p1[0] * (p4[1] - y)) / 2.0)

        area_parallelogram = area_triangle1 + area_triangle2 + area_triangle3 + area_triangle4

        return area_parallelogram == abs(a1 * b2 - a2 * b1)

    def drawParallelogram(self, a1: int, a2: int, b1: int, b2: int):
        '''
        Function draw parallelogram in command line using 'p' character
        :param a1: positive integer higher then 0, x value of 'a' vector
        :param a2: positive integer higher then 0, y value of 'a' vector
        :param b1: positive integer higher then 0, x value of 'b' vector
        :param b2: negative integer lover then 0, y value of 'b' vector
        :return:
        '''

        MyExceptions.validInput(a1, a2, b1, b2)

        max_x = max(a1, a1 + b1)
        min_x = min(0, b1)
        max_y = max(a2, a2 + b2)
        min_y = min(0, b2)

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if self.is_point_in_parallelogram(x, y, a1, a2, b1, b2):
                    print("p", end="")
                else:
                    print(" ", end="")
            print()
