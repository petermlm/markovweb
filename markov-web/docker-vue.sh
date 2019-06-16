#!/bin/bash

docker exec \
    -it \
    markovweb_frontend_1 \
    /app/node_modules/vue-cli/bin/vue $@
