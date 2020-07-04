from .event import Event


class TwitCreated(Event):
    def __init__(
        self,
        twit_id: int,
        user_id: int,
    ) -> None:
        self.twit_id: int = twit_id
        self.user_id: int = user_id
