import json

from unittest import TestCase
from unittest.mock import patch

import server


class CommonMixin:
    def setUp(self):
        server.app.testing = True
        self.app = server.app.test_client()


class GoodRequests(CommonMixin, TestCase):
    def test_get_index(self):
        ret = self.app.get('/')
        self.assertEqual(ret.status_code, 200)
        self.assertEqual(ret.content_type, 'text/html; charset=utf-8')

    @patch('server.markov')
    def test_post_plain_text(self, markov_mock):
        input_text = 'This is the text for input'
        markov_mock.return_value = input_text

        ret = self.app.post('/plain_text',
                            data=json.dumps({'text': input_text}),
                            content_type='application/json')

        self.assertEqual(ret.status_code, 200)
        self.assertEqual(str(ret.data, 'utf-8'), input_text)
        markov_mock.assert_called_once_with(input_text)

    @patch('server.reddit.get_comments_text')
    @patch('server.markov')
    def test_post_reddit(self, markov_mock, reddit_mock):
        username = 'user'
        reddit_output = 'reddit_output'
        markov_output = 'markov_output'
        reddit_mock.return_value = reddit_output
        markov_mock.return_value = markov_output

        ret = self.app.post('/reddit',
                            data=json.dumps({'username': username}),
                            content_type='application/json')

        self.assertEqual(ret.status_code, 200)
        self.assertEqual(str(ret.data, 'utf-8'), markov_output)
        reddit_mock.assert_called_once_with(username)
        markov_mock.assert_called_once_with(reddit_output)


class BadRequests(CommonMixin, TestCase):
    def _post_get(self, endpoint):
        ret = self.app.get(endpoint)
        self.assertEqual(ret.status_code, 404)

    def _post_not_json(self, endpoint):
        ret = self.app.post(endpoint, data='not a json')
        self.assertEqual(ret.status_code, 400)

    def _post_bad_json(self, endpoint):
        ret = self.app.post(endpoint,
                            data=json.dumps({'bad': 'json'}),
                            content_type='application/json')
        self.assertEqual(ret.status_code, 400)

    def test_post_plain_text_get(self):
        self._post_get('/plain_text')

    def test_post_plain_text_not_json(self):
        self._post_not_json('/plain_text')

    def test_post_plain_text_bad_json(self):
        self._post_bad_json('/plain_text')

    def test_post_reddit_get(self):
        self._post_get('/reddit')

    def test_post_reddit_not_json(self):
        self._post_not_json('/reddit')

    def test_post_reddit_bad_json(self):
        self._post_bad_json('/reddit')
