from . import windHandler

def RGBToHEX(rgb: tuple) -> str:
    return '#%02x%02x%02x' % rgb

class Rect:
    def __init__(self, x: int, y: int, width: int, height: int, colorHEX: str = None, colorRGB: tuple = None):
        #Convert the RGB to Hex if there is no hex value
        if colorHEX == None:
            if colorRGB == None:
                raise Exception("No color for rect. Please input either hex or rgb.")

            colorHEX = RGBToHEX(colorRGB)

        # Stores pixel information [[x, y], [x, y]]
        # Offset from origin
        self.pixels = []

        # Origin of rect
        self.x = x
        self.y = y


        # Color of rect
        self.color = colorHEX

        # set pixel offsets
        for ix in range(width):
            for iy in range(height):
                self.pixels.append([ix, iy])

    def draw(self, handler: windHandler.handler):
        for i in self.pixels:
            xOff = i[0]
            yOff = i[1]

            # Rect is now off the screen
            # Do not draw it
            if self.x + xOff >= handler.width:
                continue
            if self.x + xOff < 0:
                continue

            handler.setPixel(self.x + xOff, self.y + yOff, self.color)


