#!/bin/bash

docker exec \
    -it \
    markov-web-vue-dev-run \
    /app/node_modules/vue-cli/bin/vue $@
