from . import windHandler, display, Event, rect

class engine:
    def __init__(self):
        self.width: int = None
        self.height: int = None
        self.res: int = None
        self.running = False
        self.display: display.Display = display.Display(self)
        self.events: Event.event = Event.event(self.display)
        self.windHandler: windHandler.handler = windHandler.handler(self, self.display)
        self.rect = rect

        self.display.joinWindhandler(self.windHandler)
        self.display.joinEvents(self.events)