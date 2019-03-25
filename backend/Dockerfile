FROM ubuntu:18.04

# System Packages
RUN apt update --fix-missing && \
    apt -qq -y install python3 python3-pip git vim

# Python packages
RUN mkdir /pip_packages
ADD backend/requirements.txt /pip_packages/requirements.txt
RUN cd /pip_packages && pip3 install -r requirements.txt

# Prepare frontend
RUN mkdir -p /app/markov-web
ADD markov-web/dist /app/markov-web/dist

# Prepare directory for development
ADD backend /app/backend
WORKDIR /app/backend

# Run
ENTRYPOINT /app/backend/entrypoint.sh
