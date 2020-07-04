from abc import ABC, abstractmethod
from typing import Type

from .event import Event


class EventHandler(ABC):
    """should implement this interface
    to listen specific Event and call EventHandler.run method
    """

    @abstractmethod
    def __init__(
        self,
        trigger: Type[Event],
        *services: dict,
    ) -> None:
        pass

    def handle(self, event: Event) -> None:
        if type(event) != self.trigger:
            raise TypeError(
                f"{type(event).__name__} is not valid event type "
                f"for handler {type(self).__name__}"
            )

        self.run(event)

    @abstractmethod
    def run(self, event: Event) -> None:
        pass
