#!/bin/bash

docker run \
    --rm \
    -d \
    -p 5000:5000 \
    -v $(pwd)/..:/app/backend \
    --entrypoint "/app/backend/docker/entrypoint-prod.sh" \
    --name markov-web-run \
    markov-web
