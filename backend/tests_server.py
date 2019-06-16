import json

from unittest import TestCase
from unittest.mock import patch

import config
import server


class CommonMixin:
    def setUp(self):
        server.app.testing = True
        self.app = server.app.test_client()


class GoodRequests(CommonMixin, TestCase):
    @patch('server.render_template')
    @patch('config.get_env')
    def test_get_index(self, get_env_mock, render_template_mock):
        get_env_mock.return_value = config.ENV_PROD
        render_template_mock.return_value = ''

        self.app.get('/')

        get_env_mock.assert_called_once_with()
        render_template_mock.assert_called_once_with('index.html')

    @patch('server.markov')
    def test_post_plain_text(self, markov_mock):
        input_text = 'This is the text for input'
        output_size = 100
        markov_mock.return_value = input_text

        ret = self.app.post('/plain_text',
                            data=json.dumps({'text': input_text, 'output_size': output_size}),
                            content_type='application/json')

        self.assertEqual(ret.status_code, 200)
        self.assertEqual(str(ret.data, 'utf-8'), input_text)
        markov_mock.assert_called_once_with(input_text, words_num=output_size)

    @patch('server.reddit.get_comments_text')
    @patch('server.markov')
    def test_post_reddit(self, markov_mock, reddit_mock):
        username = 'user'
        output_size = 100
        reddit_output = 'reddit_output'
        markov_output = 'markov_output'
        reddit_mock.return_value = reddit_output
        markov_mock.return_value = markov_output

        ret = self.app.post('/reddit',
                            data=json.dumps({'username': username, 'output_size': output_size}),
                            content_type='application/json')

        self.assertEqual(ret.status_code, 200)
        self.assertEqual(str(ret.data, 'utf-8'), markov_output)
        reddit_mock.assert_called_once_with(username)
        markov_mock.assert_called_once_with(reddit_output, words_num=output_size)


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

    def _post_missing_input(self, endpoint):
        ret = self.app.post(endpoint,
                            data=json.dumps({'output_size': 100}),
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

    def test_post_plain_text_no_input(self):
        input_text = ''
        ret = self.app.post('/plain_text',
                            data=json.dumps({'text': input_text}),
                            content_type='application/json')
        self.assertEqual(ret.status_code, 400)

    def test_post_plain_text_too_long(self):
        input_text = 'a' * 10001
        ret = self.app.post('/plain_text',
                            data=json.dumps({'text': input_text}),
                            content_type='application/json')
        self.assertEqual(ret.status_code, 400)

    def test_post_reddit_no_input(self):
        input_text = ''
        ret = self.app.post('/reddit',
                            data=json.dumps({'username': input_text}),
                            content_type='application/json')
        self.assertEqual(ret.status_code, 400)

    def test_post_reddit_too_long(self):
        input_text = 'a' * 20
        ret = self.app.post('/reddit',
                            data=json.dumps({'username': input_text}),
                            content_type='application/json')
        self.assertEqual(ret.status_code, 400)

    def test_post_plain_text_missing_output_size(self):
        input_text = 'This is the text for input'
        ret = self.app.post('/plain_text',
                            data=json.dumps({'text': input_text}),
                            content_type='application/json')
        self.assertEqual(ret.status_code, 400)

    def test_post_reddit_missing_output_size(self):
        username = 'user'
        ret = self.app.post('/plain_text',
                            data=json.dumps({'username': username}),
                            content_type='application/json')
        self.assertEqual(ret.status_code, 400)
