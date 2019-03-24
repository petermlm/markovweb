#!/bin/bash

docker build -t markov-web-vue-dev .

docker run \
    --rm \
    -it \
    -p 8080:8080 \
    -v $(pwd):/app \
    --name markov-web-vue-dev-run \
    markov-web-vue-dev
