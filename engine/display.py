import engine, tkinter as tk
from . import windHandler, Event

class Display:
    def __init__(self, engine: engine):
        self.engine = engine

    def __bindEvents(self):
        self.root.bind("<KeyPress>", self.events.addEvent)
        self.root.bind("<KeyRelease>", self.events.addEvent)

    def joinEvents(self, event: Event.event):
        self.events: Event.event = event

    def joinWindhandler(self, windHandler: windHandler):
        self.windHandler: windHandler.handler = windHandler

    def set_mode(self, width: int, height: int, resizable: bool, res: int):
        self.width = width
        self.height = height
        self.res = res

        self.root = tk.Tk()
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(resizable, resizable)

        self.root.protocol("WM_DELETE_WINDOW", self.__onClosing)
        self.__bindEvents()

        self.running = True
        self.engine.windHandler.createScreen()

    def fill(self, color: str):
        if not self.windHandler.setup:
            return

        for pixel in self.windHandler.pixels:
            pixel['bg'] = color

    def drawRect(self, rect):
        rect.draw(self.windHandler)

    def update(self):
        self.root.update_idletasks()
        self.root.update()

        #self.events.get()

    def __onClosing(self):
        self.running = False