from .Display import Display
from Exceptions.MyExceptions import MyExceptions

class TextDisplay(Display):
    def drawTriangle(self, a1: int, a2: int, b1: int, b2: int):
        '''
        Function prints info about drawing triangle
        :param a1: positive integer higher then 0, x value of 'a' vector
        :param a2: positive integer higher then 0, y value of 'a' vector
        :param b1: positive integer higher then 0, x value of 'b' vector
        :param b2: negative integer lover then 0, y value of 'b' vector
        :return: None
        '''

        MyExceptions.validInput(a1=a1, a2=a2, b1=b1, b2=b2)
        print(f"Drawing a triangle from vectors ({a1}, {a2}), ({b1}, {b2})")

    def drawCircle(self, r: int):
        '''
        Function prints info about drawing circle
        :param r: positive integer higher then, circle radius
        :return: None
        '''

        MyExceptions.validInputCircle(r=r)
        print(f"Drawing a circle with radius {r}")

    def drawParallelogram(self, a1: int, a2: int, b1: int, b2: int):
        '''
        Function prints info about drawing parallelogram
        :param a1: positive integer higher then 0, x value of 'a' vector
        :param a2: positive integer higher then 0, y value of 'a' vector
        :param b1: positive integer higher then 0, x value of 'b' vector
        :param b2: negative integer lover then 0, y value of 'b' vector
        :return: None
        '''

        MyExceptions.validInput(a1=a1, a2=a2, b1=b1, b2=b2)
        print(f"Drawing a parallelogram from vectors ({a1}, {a2}), ({b1}, {b2})")
