from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional


if TYPE_CHECKING:
    from .dispatcher import EventDispatcher


class Event:
    """Event itself
    """

    handled_started_at: Optional[datetime] = None
    handle_ended_at: Optional[datetime] = None

    def __init__(
        self,
        emitted_at: datetime = None,
    ) -> None:
        if emitted_at is None:
            emitted_at = datetime.now()

        self.emitted_at: datetime = emitted_at

    @classmethod
    def inject_dispatcher(
        cls,
        dispatcher: EventDispatcher,
    ) -> None:
        cls.dispatcher = dispatcher
