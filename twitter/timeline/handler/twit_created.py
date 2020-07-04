from __future__ import annotations

from typing import TYPE_CHECKING, Type

from twitter.common.event.handler import EventHandler
from twitter.common.event.twit import TwitCreated


if TYPE_CHECKING:
    from twitter.timeline.service.add_twit import AddTwitService


class TwitCreatedHandler(EventHandler):
    def __init__(
        self,
        trigger: Type[TwitCreated],
        add_twit_service: AddTwitService,
    ) -> None:
        self.trigger = trigger
        self.add_twit_service = add_twit_service

    def run(self, event: TwitCreated) -> None:
        user_id = event.user_id
        twit_id = event.twit_id

        self.add_twit_service.append_new_twit_to_followers(twit_id, user_id)
