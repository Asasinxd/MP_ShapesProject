from .Shape import Shape


class ComplexShape(Shape):
    def __init__(self, w: object):
        '''
        Initialize object to display various shapes added to queue
        :param w: object, type of display
        '''

        super().__init__(w)
        self.queue = list()

    def add(self, o: object) -> bool:
        '''
        Function adds object to queue and returns True if was added correctly and max capacity of queue is 5
        :param o: object, shape to draw
        :return: bool
        '''
        if len(self.queue) < 5:
            if self.queue.append(o):
                return True

        return False

    def draw(self):
        '''
        Function calss function for every obj in queue
        :return: None
        '''
        for obj in self.queue:
            obj.draw()
