from flask import render_template

import config


def render(template):
    env = config.get_env()
    if env == config.ENV_PROD:
        base_url = "/markov"
    else:
        base_url = ""

    return render_template(template, env=env, base_url=base_url)
