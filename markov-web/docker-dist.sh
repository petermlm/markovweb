#!/bin/bash

docker build -f docker/Dockerfile -t markovweb-frontend-dist .

docker run \
    --rm \
    -it \
    -v $(pwd):/app \
    -u $(id -u):$(id -g) \
    --name markovweb-frontend-dist-run \
    --entrypoint "/app/docker/entrypoint-dist.sh" \
    markovweb-frontend-dist
