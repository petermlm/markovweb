from flask import render_template

import config


def render(template):
    if config.get_env() == config.ENV_PROD:
        base_url = "/markov"
    else:
        base_url = ""

    return render_template(template, base_url=base_url)
