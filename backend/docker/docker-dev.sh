#!/bin/bash

docker run \
    --rm \
    -it \
    -p 5000:5000 \
    -v $(pwd)/..:/app/backend \
    --entrypoint "/app/backend/docker/entrypoint-dev.sh" \
    --name markov-web-run \
    markov-web
