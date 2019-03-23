#!/usr/bin/env python3

from flask import Flask, request, abort, render_template

app = Flask(__name__,
            static_url_path="",
            static_folder="./markov/dist",
            template_folder="./markov/dist")


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def index2():
    if not request.json or 'text' not in request.json:
        print(request.json)
        abort(400)

    text = request.json['text']
    # Call Markov here
    return text


if __name__ == '__main__':
    app.run(host='0.0.0.0')
