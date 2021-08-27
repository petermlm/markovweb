This is a simple web application that enables the usage of [my Markov library](https://github.com/petermlm/markov)
via a web interface. There are two ways of using it, either by pasting a big
block of text or by inputting a reddit username.

Text is then generated using a Markov chain from the given text or from the
comments of the reddit username.

# Development

Create a virtual environment

    cd src
    python3 -m venv env
    source env/bin/activate
    pip install wheel
    pip install -r requirements.txt

Then to run do:

    FLASK_ENV=development python server.py

To run tests do:

    python -m unittest

# Deploy

In the `deploy` directory there are two helper scripts. To deploy use the
`deploy.sh` script with a single argument for the port of the server. To kill
the deployment, use `kill.sh`.

# Frontend

The frontend used to be a Vue application, but I don't have time to maintain it
and deal with npm package issues. I've decided to reimplement the frontend
using Jinja, Boostrap, and vanilla JavaScript.
