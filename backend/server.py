#!/usr/bin/env python3

from flask import Flask, request, abort, render_template

from markov import markov

app = Flask(__name__,
            static_url_path="",
            static_folder="../markov-web/dist",
            template_folder="../markov-web/dist")


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def index2():
    if not request.json or 'text' not in request.json:
        print(request.json)
        abort(400)

    try:
        text = request.json['text']
    except KeyError:
        return "Bad Request"

    return markov(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
