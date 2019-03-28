#!/bin/bash

cd /app/backend
gunicorn -w 4 -b 0.0.0.0:8100 server:app
