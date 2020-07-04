from unittest import mock

from twitter.common.event.twit import TwitCreated
from twitter.timeline.handler.twit_created import TwitCreatedHandler
from twitter.timeline.service.add_twit import AddTwitService


class TestTwitCreatedHandler:
    def test_run(self):
        add_twit_service_spy = mock.MagicMock(spec=AddTwitService)
        handler = TwitCreatedHandler(TwitCreated, add_twit_service_spy)
        twit_id = 22
        user_id = 99

        # when
        handler.run(TwitCreated(twit_id, user_id))

        # then
        add_twit_service_spy.append_new_twit_to_followers.assert_called_once_with(twit_id, user_id)
