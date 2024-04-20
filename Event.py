class Event:
    def __init__(self):
        self.handlers = set()

    def subscribe(self, handler):
        self.handlers.add(handler)

    def unsubscribe(self, handler):
        self.handlers.remove(handler)

    def invoke(self, *args, **kwargs):
        for handler in self.handlers:
            handler(*args, **kwargs)
