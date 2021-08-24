#!/bin/bash

PORT=$1

# Run from main directory
cd ..

# Build frontend
cd markov-web
source build.sh
cd ..

# Build backend
docker build -f backend/Dockerfile -t markov-web-deploy .

docker run \
    --rm \
    -d \
    -p $PORT:5000 \
    -e ENV=PROD \
    -v $(pwd)/backend:/app/backend \
    -v $(pwd)/markov-web/dist:/app/markov-web/dist \
    --name markov-web-deploy-run \
    markov-web-deploy
