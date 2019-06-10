#!/bin/bash

export UID=$(id -u)
export GID=$(id -g)
docker-compose -f docker-compose-dev.yaml up --build
