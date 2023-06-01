from .Shape import Shape


class ComplexShape(Shape):
    def __init__(self, w: object, a1: int, a2: int, b1: int, b2: int):
        super().__init__(w)
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2
        self.queue = list()

    def add(self, o: object):
        if len(self.queue) < 5:
            if self.queue.append(o):
                return True

        return False

    def draw(self):
        obj = self.queue[0]
        self.queue.pop(0)
        obj.draw()
