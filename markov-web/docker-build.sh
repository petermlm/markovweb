#!/bin/bash

docker build -t markov-web-vue-dev .

docker run \
    --rm \
    -it \
    -p 8080:8080 \
    -v $(pwd):/app \
    -u $(id -u):$(id -g) \
    --name markov-web-vue-dev-run \
    --entrypoint "/app/entrypoint-build.sh" \
    markov-web-vue-dev
