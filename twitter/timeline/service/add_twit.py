from __future__ import annotations

from typing import List

from twitter.timeline.domain.user import Follower
from twitter.timeline.domain.twit import Timeline


class AddTwitService:
    def append_new_twit_to_followers(
        self,
        twit_id: int,
        user_id: int,
    ) -> None:
        followers = self._get_followers(user_id)
        for follower in followers:
            timeline = self._get_timeline(follower.id)
            timeline.append(twit_id)
            self._persist_timeline(timeline)

    def _get_followers(self, user_id: int) -> List[Follower]:
        pass

    def _get_timeline(self, user_id: int) -> Timeline:
        pass

    def _persist_timeline(self, timeline: Timeline) -> None:
        pass
