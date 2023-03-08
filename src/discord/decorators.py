from typing import Any
from ..gateway.config import Event


class EventOn:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(args, kwds)

    def event(self, event: str) -> Any:
        print(event)


app = EventOn()


@app.event(event=Event.MESSAGE_CREATE)
def foo(a, b):
    print(a, b)

