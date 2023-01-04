import EnquX, tkinter as tk, math
from . import display

class handler:
    def __init__(self, engine: EnquX, dis: display):
        self.engine = engine
        self.pixels: list = []
        self.setup = False
        self.dis: display = dis

    def createScreen(self):
        width = round(self.dis.width / self.dis.res)
        height = round(self.dis.height / self.dis.res)

        lenX = round(self.dis.width / width)
        lenY = round(self.dis.height / height)

        for x in range(lenX):
            for y in range(lenY):
                frame = tk.Frame(self.dis.root, width=width, height=height)
                frame.grid(column=y, row=x)

                self.pixels.append(frame)

        self.width = lenX
        self.setup = True

    def setPixel(self, x: int, y: int, color: str):
        if not self.setup:
            return

        if x + y * self.width >= len(self.pixels):
            return
        
        if x < 0 or y < 0: 
            return

        index = x + y * self.width

        self.pixels[index]['bg'] = color