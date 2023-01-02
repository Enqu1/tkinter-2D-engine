from . import windHandler

class Rect:
    def __init__(self, x: int, y: int, width: int, height: int, color: str):
        # Stores pixel information [[x, y], [x, y]]
        # Offset from origin
        self.pixels = []

        # Origin of rect
        self.x = x
        self.y = y

        # Color of rect
        self.color = color

        # set pixel offsets
        for ix in range(width):
            for iy in range(height):
                self.pixels.append([ix, iy])

    def draw(self, handler: windHandler.handler):
        for i in self.pixels:
            xOff = i[0]
            yOff = i[1]

            handler.setPixel(self.x + xOff, self.y + yOff, self.color)


