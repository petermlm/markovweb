from unittest import TestCase
from unittest.mock import MagicMock, patch, call

import reddit


class MakeUrlTests(TestCase):
    def test_make_url(self):
        username = 'user'
        step = 0
        exp = 'https://www.reddit.com/user/user/comments/.json?count=25&after=0'

        ret = reddit.make_url(username, step)
        self.assertEqual(ret, exp)

    def test_make_url_step_1(self):
        username = 'user'
        step = 1
        exp = 'https://www.reddit.com/user/user/comments/.json?count=50&after=25'

        ret = reddit.make_url(username, step)
        self.assertEqual(ret, exp)


@patch('reddit.requests.get')
class GetCommentsTextTests(TestCase):
    def test_call(self, requests_get_mock):
        username = 'user'

        children = []
        ret_mock = MagicMock()
        ret_mock.json.return_value = {'data': {'children': children}}

        requests_get_mock.get.return_value = ret_mock

        reddit.get_comments_text(username)

        calls = requests_get_mock.call_args_list
        for i in range(reddit.pages):
            url = reddit.make_url(username, i)
            self.assertEqual(calls[i], call(url, headers={'User-agent': reddit.user_agent}))
