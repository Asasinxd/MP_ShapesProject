from .Shape import Shape


class ComplexShape(Shape):
    def __init__(self, w: object):
        super().__init__(w)
        self.queue = list()

    def add(self, o: object) -> bool:
        if len(self.queue) < 5:
            if self.queue.append(o):
                return True

        return False

    def draw(self):
        for obj in self.queue:
            obj.draw()