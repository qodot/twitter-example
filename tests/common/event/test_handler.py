from typing import Type

from twitter.common.event.event import Event
from twitter.common.event.handler import EventHandler


class TestEventHandler:
    def test_init(self):
        class MyEvent(Event):
            pass

        class MyHandler(EventHandler):
            def __init__(self, trigger: Type[MyEvent]):
                self.trigger = trigger

            def run(self, event: MyEvent):
                pass

        # when
        handler = MyHandler(MyEvent)

        # then
        assert handler.trigger is MyEvent
