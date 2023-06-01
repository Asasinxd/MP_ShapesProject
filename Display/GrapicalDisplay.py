from .Display import Display


class GrapicalDisplay(Display):

    def is_point_in_triangle(self, x: int, y: int, x1: int, y1: int, a1: int, a2: int, b1: int, b2: int) -> bool:
        area_triangle = abs((x1 * (a2 - b2) + a1 * (b2 - y1) + b1 * (y1 - a2)) / 2.0)
        area_sub_triangle1 = abs((x * (y1 - a2) + x1 * (a2 - y) + a1 * (y - y1)) / 2.0)
        area_sub_triangle2 = abs((x * (a2 - b2) + a1 * (b2 - y) + b1 * (y - a2)) / 2.0)
        area_sub_triangle3 = abs((x * (b2 - y1) + b1 * (y1 - y) + x1 * (y - b2)) / 2.0)

        return area_triangle == area_sub_triangle1 + area_sub_triangle2 + area_sub_triangle3

    def drawTriangle(self, a1: int, a2: int, b1: int, b2: int):
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


    def drawParallelogram(self, a1: int, a2: int, b1: int, b2: int):
        pass
