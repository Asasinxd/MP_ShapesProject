from Shapes.Shape import Shape

class Circle(Shape):
    def __init__(self, w: object, r: int):
        '''
        Initialize object to display circle with given radius
        :param w: object, type of display
        :param r: positive integer higher then, circle radius
        '''

        super().__init__(w)
        self.r = r

    def draw(self):
        '''
        Function calls function to draw circle
        :return: None
        '''

        self.w.drawCircle(self.r)
