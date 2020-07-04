from twitter.me.domain.twit import Twit


class TestPost:
    def test_factory(self):
        id_ = 1
        content = "content"
        user_id = 1

        # when
        twit = Twit.factory(id_=id_, content=content, user_id=user_id)

        # then
        assert isinstance(twit, Twit)
        assert twit.id == id_
        assert twit.content == content
        assert twit.user_id == user_id
