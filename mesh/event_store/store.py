class EventStore:
    def __init__(self):
        self.events = []
    def add(self, e):
        self.events.append(e)
    def log(self, *args, **kwargs):
        self.events.append((args, kwargs))
