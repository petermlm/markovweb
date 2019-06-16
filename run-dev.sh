#!/bin/bash

# Pass parameters like:
#
#     ./run-dev.sh --build

export UID=$(id -u)
export GID=$(id -g)
docker-compose -f docker-compose-dev.yaml up $*
