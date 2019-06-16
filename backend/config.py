import os

ENV_DEV = 'DEV'
ENV_TEST = 'TEST'
ENV_PROD = 'PROD'


def get_env():
    return os.environ.get('ENV', ENV_DEV)


PlainTextMaxInput = 10000
RedditMaxInput = 20

OutputSizeMax = 500
