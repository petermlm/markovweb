#!/bin/bash

docker build -t markov-web -f Dockerfile ..

docker run \
    --rm \
    -it \
    -p 5000:5000 \
    -v $(pwd):/app/backend \
    --name markov-web-run \
    markov-web
