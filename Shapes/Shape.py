class Shape:
    def __init__(self, w: object):
        self.w = w

    def draw(self):
        pass

    def changeDisplay(self, newDisplay: object):
        self.w = newDisplay
