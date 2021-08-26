#!/usr/bin/env python3

from flask import request, abort, render_template, Response
from flask_cors import CORS
from markov import markov

from app import make_app
import config
import reddit

app = make_app()

if config.get_env() == config.ENV_DEV:
    app.config['CORS_HEADERS'] = 'Content-Type'
    CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=['GET'])
def index():
    return render_template('plain_text.html')


@app.route('/plain_text', methods=['POST'])
def plain_text_post():
    if not request.json or 'text' not in request.json or 'output_size' not in request.json:
        abort(400)

    try:
        text = request.json['text']
        output_size = request.json['output_size']
    except KeyError:
        abort(400)

    input_size = len(text)

    if input_size_valid(input_size, config.PlainTextMaxInput) or \
            output_size_valid(output_size):
        abort(400)

    return markov(text, words_num=output_size)


@app.route('/reddit', methods=['GET'])
def reddit_get():
    return render_template('reddit.html')


@app.route('/reddit', methods=['POST'])
def reddit_post():
    if not request.json or 'username' not in request.json or 'output_size' not in request.json:
        abort(400)

    try:
        username = request.json['username']
        output_size = request.json['output_size']
    except KeyError:
        abort(400)

    input_size = len(username)

    if input_size_valid(input_size, config.RedditMaxInput) or \
            output_size_valid(output_size):
        abort(400)

    comments_text = reddit.get_comments_text(username)
    return markov(comments_text, words_num=output_size)


def input_size_valid(input_size, max):
    return 0 > input_size >= max


def output_size_valid(output_size):
    return 0 > output_size >= config.OutputSizeMax


if __name__ == '__main__':
    app.run(host='0.0.0.0')
