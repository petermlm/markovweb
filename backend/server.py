#!/usr/bin/env python3

from flask import Flask, request, abort, render_template, Response
from flask_cors import CORS

import config
import reddit
from markov import markov

app = Flask(__name__,
            static_url_path="",
            static_folder="../markov-web/dist",
            template_folder="../markov-web/dist")

if config.get_env() == config.ENV_DEV:
    app.config['CORS_HEADERS'] = 'Content-Type'
    CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=['GET'])
def index():
    env = config.get_env()
    if env == config.ENV_PROD:
        return render_template("index.html")
    else:
        res = Response("In development, port is 8080")
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res


@app.route('/plain_text', methods=['POST'])
def request_plain_text():
    if not request.json or 'text' not in request.json:
        abort(400)

    try:
        text = request.json['text']
    except KeyError:
        abort(400)

    input_size = len(text)

    if input_size == 0 or input_size >= config.PlainTextMaxInput:
        abort(400)

    return markov(text)


@app.route('/reddit', methods=['POST'])
def request_reddit():
    if not request.json or 'username' not in request.json:
        abort(400)

    try:
        username = request.json['username']
    except KeyError:
        abort(400)

    input_size = len(username)

    if input_size == 0 or input_size >= config.RedditMaxInput:
        abort(400)

    comments_text = reddit.get_comments_text(username)
    return markov(comments_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
