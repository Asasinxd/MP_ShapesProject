from .Shape import Shape


class Parallelogram(Shape):
    def __init__(self, w: object, a1: int, a2: int, b1: int, b2: int):
        '''
        Initialize object to diaplsay parallelogram with given parameters
        :param w: object, type of display
        :param a1: positive integer higher then 0, x value of 'a' vector
        :param a2: positive integer higher then 0, y value of 'a' vector
        :param b1: positive integer higher then 0, x value of 'b' vector
        :param b2: negative integer lover then 0, y value of 'b' vector
        '''

        super().__init__(w)
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2

    def draw(self):
        '''
        Function calls functio to draw parallelogram
        :return: None
        '''

        self.w.drawParallelogram(a1=self.a1, a2=self.a2, b1=self.b1, b2=self.b2)
