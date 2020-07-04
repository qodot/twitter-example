from twitter import container
from twitter.me.service.twit import TwitService


class TestPostService:
    def test_create(self):
        # given
        content = "content"
        user_id = 123
        service = container.get(TwitService)

        # when
        new_id = service.create(content, user_id)

        assert new_id is not None
        assert isinstance(new_id, int)
