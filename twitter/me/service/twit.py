from twitter.me.domain.twit import Twit


class TwitService:
    def create(self, content: str, user_id: int) -> int:
        new_id = self._generate_id()

        twit = Twit.factory(id_=new_id, content=content, user_id=user_id)
        self._persist(twit)

        return new_id

    def _generate_id(self) -> int:
        return 1

    def _persist(self, twit: Twit) -> None:
        pass
