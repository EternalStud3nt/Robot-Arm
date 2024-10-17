class Event:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, callback):
        if callback not in self._subscribers:
            self._subscribers.append(callback)

    def unsubscribe(self, callback):
        if callback in self._subscribers:
            self._subscribers.remove(callback)

    def invoke(self, *args, **kwargs):
        for callback in self._subscribers:
            callback(*args, **kwargs)

# Example usage
def on_event_fired(message):
    print(f"Event received with message: {message}")

event = Event()
event.subscribe(on_event_fired)
event.invoke("Hello, World!")