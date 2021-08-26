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
