import engine, tkinter as tk, math
from . import display

class handler:
    def __init__(self, engine: engine, dis: display):
        self.engine = engine
        self.pixels: list = []
        self.setup = False
        self.dis = dis

    def createScreen(self):
        width = math.floor(self.dis.width / self.dis.res)
        height = math.floor(self.dis.height / self.dis.res)

        for x in range(width):
            for y in range(height):
                frame = tk.Frame(self.dis.root, width=width, height=height)
                frame.grid(column=y, row=x)

                self.pixels.append(frame)

        self.width = width
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