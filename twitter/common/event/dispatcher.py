from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING, Type


if TYPE_CHECKING:
    from twitter.common.event.event import Event
    from twitter.common.event.handler import EventHandler


class EventDispatcher:
    """map Event to EventHandler and call EventHandler.handle method
    """

    def __init__(self):
        self.dispatch_map = defaultdict(list)

    def register(self, event: Type[Event], handler: EventHandler) -> None:
        self.dispatch_map[event].append(handler)

    def dispatch(self, event: Event) -> None:
        handlers = self.dispatch_map.get(type(event))
        if not handlers:
            raise NoEventHandlerError

        for handler in handlers:
            handler.handle(event)


class NoEventHandlerError(Exception):
    pass
