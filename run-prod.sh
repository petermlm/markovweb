#!/bin/bash

cd markov-web
source docker-dist.sh
cd ..

docker build -f backend/docker/Dockerfile -t markovweb-prod .

docker run \
    --rm \
    -d \
    -p 5000:5000 \
    -v $(pwd)/backend:/app/backend \
    -v $(pwd)/markov-web/dist:/app/frontend/dist \
    --entrypoint "/app/backend/docker/entrypoint-prod.sh" \
    --name markovweb-run \
    markovweb-prod
