#!/bin/bash

cd markov-web
source docker-dist.sh
cd ..

docker build -f backend/docker/Dockerfile -t markovweb-prod .

docker run \
    --rm \
    -d \
    -p 8100:5000 \
    -e ENV=PROD \
    -v $(pwd)/backend:/app/backend \
    -v $(pwd)/markov-web/dist:/app/markov-web/dist \
    --entrypoint "/app/backend/docker/entrypoint-prod.sh" \
    --name markovweb-run \
    markovweb-prod
