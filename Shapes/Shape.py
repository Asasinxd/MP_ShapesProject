class Shape:
    def __init__(self, w: object):
        '''
        Initialize object to display shape
        :param w: object, type of display
        '''
        self.w = w

    def draw(self):
        pass

    def changeDisplay(self, newDisplay: object):
        '''
        Function chages object that displays shape
        :param newDisplay: object, new object to display shape
        :return: None
        '''

        self.w = newDisplay
