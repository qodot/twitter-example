from datetime import datetime
from typing import Type
from unittest import mock

from pytest import raises

from twitter.common.event.event import Event
from twitter.common.event.dispatcher import (
    EventDispatcher,
    NoEventHandlerError,
)
from twitter.common.event.handler import EventHandler


class TestEventDispater:
    def test_register(self):
        class MyEvent(Event):
            pass

        class MyHandler(EventHandler):
            def __init__(self, trigger: Type[MyEvent]):
                self.trigger = trigger

            def run(self, event: MyEvent):
                pass

        handler = MyHandler(MyEvent)
        event_dispatcher = EventDispatcher()

        # when
        event_dispatcher.register(MyEvent, handler)

        # then
        assert MyEvent in event_dispatcher.dispatch_map
        assert event_dispatcher.dispatch_map[MyEvent] == [handler]

    def test_dispatch(self):
        class MyEvent(Event):
            pass

        class MyHandler1(EventHandler):
            def __init__(self, trigger: Type[MyEvent]):
                self.trigger = trigger

            def run(self, event: MyEvent):
                pass

        handler1_spy = mock.MagicMock(spec=MyHandler1)

        class MyHandler2(EventHandler):
            def __init__(self, trigger: Type[MyEvent]):
                self.trigger = trigger

            def run(self, event: MyEvent):
                pass

        handler2_spy = mock.MagicMock(spec=MyHandler2)

        event_dispatcher = EventDispatcher()
        event_dispatcher.register(MyEvent, handler1_spy)
        event_dispatcher.register(MyEvent, handler2_spy)

        event = MyEvent(datetime.now())

        # when
        # import pdb; pdb.set_trace()
        event_dispatcher.dispatch(event)

        # then
        handler1_spy.handle.assert_called_once_with(event)
        handler2_spy.handle.assert_called_once_with(event)

    def test_dispatch_raise_no_handler_errors(self):
        class MyEvent(Event):
            pass

        event_dispatcher = EventDispatcher()

        event = MyEvent(datetime.now())

        # when
        with raises(NoEventHandlerError):
            event_dispatcher.dispatch(event)
