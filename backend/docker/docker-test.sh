#!/bin/bash

docker run \
    --rm \
    -it \
    -v $(pwd)/..:/app/backend \
    --entrypoint "/app/backend/docker/entrypoint-test.sh" \
    --name markov-web-testing \
    markov-web $1
