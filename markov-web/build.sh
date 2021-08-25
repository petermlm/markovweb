#!/bin/bash

# This will be the directory containing the built frontend
mkdir -p dist

# Build the docker image
docker build -f docker/Dockerfile -t markov-web-frontend-build .

# Execute the build of the frontend
docker run \
    --rm \
    -it \
    -v $(pwd):/app \
    -u $(id -u):$(id -g) \
    --name markov-web-frontend-build-run \
    markov-web-frontend-build
