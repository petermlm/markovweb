#!/usr/bin/env python3

from flask import Flask, request, abort, render_template

import reddit
from markov import markov

app = Flask(__name__,
            static_url_path="",
            static_folder="../markov-web/dist",
            template_folder="../markov-web/dist")


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/plain_text', methods=['POST'])
def request_plain_text():
    if not request.json or 'text' not in request.json:
        abort(400)

    try:
        text = request.json['text']
    except KeyError:
        return "Bad Request"

    return markov(text)


@app.route('/reddit', methods=['POST'])
def request_reddit():
    if not request.json or 'username' not in request.json:
        abort(400)

    try:
        username = request.json['username']
    except KeyError:
        return "Bad Request"

    comments_text = reddit.get_comments_text(username)
    return markov(comments_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
