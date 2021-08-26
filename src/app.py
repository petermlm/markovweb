from flask import Flask

import config


def make_app():
    # The are the same right now, but may be different in the future
    if config.get_env() == config.ENV_PROD:
        static_url_path = "/static"
    else:
        static_url_path = "/static"

    app = Flask(__name__,
                static_url_path=static_url_path,
                static_folder="static",
                template_folder="templates")

    return app
