from flask import Flask

import config


def make_app():
    env = config.get_env()
    if env == config.ENV_PROD:
        static_url_path = ""
        static_folder = "/app/markov-web/dist"
        template_folder = "/app/markov-web/dist"
    else:
        static_url_path = ""
        static_folder = "../markov-web/dist"
        template_folder = "../markov-web/dist"

    app = Flask(__name__,
                static_url_path=static_url_path,
                static_folder=static_folder,
                template_folder=template_folder)

    return app
