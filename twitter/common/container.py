from abc import abstractmethod
from typing import Type
from typing import TypeVar

from twitter.common.event.dispatcher import EventDispatcher
from twitter.common.event.event import Event
from twitter.common.event.twit import TwitCreated

from twitter.me.service.twit import TwitService
from twitter.timeline.handler.twit_created import TwitCreatedHandler
from twitter.timeline.service.add_twit import AddTwitService


T = TypeVar("T")


class DIContainer:
    """dependency injection container
    """

    def __init__(self) -> None:
        self._container = {}

    @abstractmethod
    def compose(self) -> None:
        pass

    def _compose(self) -> None:
        # common context
        self.register(EventDispatcher())

        # me context
        self.register(TwitService())

        # timeline context
        self.register(AddTwitService())
        self.register(
            TwitCreatedHandler(
                TwitCreated,
                self.get(AddTwitService)
            )
        )

        # event dispatch map
        Event.inject_dispatcher(self.get(EventDispatcher))
        event_dispatcher = self.get(EventDispatcher)
        event_dispatcher.register(
            TwitCreated,
            self.get(TwitCreatedHandler)
        )

    def register(self, obj: T) -> None:
        type_ = type(obj)
        self._container[type_] = obj

    def get(self, type_: Type[T]) -> T:
        try:
            obj = self._container[type_]
        except KeyError:
            raise NotContainedTypeError(f"type: {type_}")

        return obj


class NotContainedTypeError(Exception):
    pass


class ProductionDIContainer(DIContainer):
    def compose(self) -> None:
        self._compose()


class StageDIContainer(DIContainer):
    def compose(self) -> None:
        self._compose()


class DevelopmentDIContainer(DIContainer):
    def compose(self) -> None:
        self._compose()


class TestDIContainer(DIContainer):
    def compose(self) -> None:
        self._compose()


class DIContainerFactory:
    @classmethod
    def factory(cls, env: str) -> DIContainer:
        if env == "production":
            container = ProductionDIContainer()
        elif env == "stage":
            container = StageDIContainer()
        elif env == "development":
            container = DevelopmentDIContainer()
        elif env == "test":
            container = TestDIContainer()
        else:
            raise WrongEnvironmentError(f"env: {env}")

        container.compose()
        return container


class WrongEnvironmentError(Exception):
    pass
