# Development

## Backend

Create a virtual environment

    cd backend
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt

Then to run do:

    python3 server.py

To run tests do:

    python3 -m unittest

## Frontend

In the `markov-web` directory, the server may be run locally with:

    npm run serve

The frontend may be built with:

    npm run build

But using the docker image may be easier:

    ./build.sh

## Running Both Backend and Frontend

To run both, the frontend simply needs to be build first by running the
`build.sh` script in it's directory. Running the backend from the virtual
environment should then work.

# Deploy

In the `deploy` directory there are two helper scripts. To deploy use the
`deploy.sh` script with a single argument for the port of the server. To kill
the deployment, use `kill.sh`.
