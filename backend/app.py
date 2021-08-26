from flask import Flask


def make_app():
    return Flask(__name__,
                 static_url_path="/static",
                 static_folder="static",
                 template_folder="templates")
