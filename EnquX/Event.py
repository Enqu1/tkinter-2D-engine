import copy
from . import display

class event:
    def __init__(self, dis: display):
        self.dis: display = dis
        self.events = []

    def addEvent(self, event):
        self.events.append(event)

    def get(self):
        temp = copy.copy(self.events)
        self.events = []

        return temp