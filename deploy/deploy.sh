#!/bin/bash

PORT=$1

# Run from source directory
cd ../src

# Build the project
docker build -f Dockerfile -t markov-web-deploy .

# Run it
docker run \
    --rm \
    -d \
    -p $PORT:5000 \
    -e ENV=PROD \
    --name markov-web-deploy-run \
    markov-web-deploy
