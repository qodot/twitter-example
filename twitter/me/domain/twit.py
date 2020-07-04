from __future__ import annotations

from twitter.common.entity import Aggregate
from twitter.common.event.twit import TwitCreated


class Twit(Aggregate):
    def __init__(
        self,
        id_: int,
        content: str,
        user_id: int,
    ) -> None:
        super().__init__()

        self.id: int = id_
        self.content: str = content
        self.user_id: int = user_id

    @classmethod
    def factory(
        cls,
        id_: int,
        content: str,
        user_id: int,
    ) -> Twit:
        twit = cls(id_=id_, content=content, user_id=user_id)

        event = TwitCreated(twit_id=id_, user_id=user_id)
        twit.add_event(event)

        return twit
