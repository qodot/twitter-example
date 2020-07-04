from __future__ import annotations

from abc import ABC
from typing import Generator, List

from twitter.common.event.event import Event
from twitter.common.event.dispatcher import NoEventHandlerError


class Aggregate(ABC):
    def __init__(self) -> None:
        self._domain_events: List[Event] = []

    def add_event(self, event: Event) -> None:
        self._domain_events.append(event)

    def __del__(self) -> None:
        self._dispatch()

    def _dispatch(self) -> None:
        for event in self._consume_event():
            try:
                event.dispatcher.dispatch(event)
            except NoEventHandlerError:
                # TODO: how do i know there's no
                # registered handler with specific event?
                pass
            except Exception:
                # TODO: log events fail to dispatch
                pass

    def _consume_event(self) -> Generator[Event]:
        while self._domain_events:
            yield self._domain_events.pop(0)
