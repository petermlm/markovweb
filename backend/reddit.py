import requests

count = 25


def make_url(username, step):
    query_string = '?count={}&after={}'.format(count * (step + 1), count * step)
    return 'https://www.reddit.com/user/{}/comments/.json{}'.format(username, query_string)


def get_comments_text(username):
    comments_text = ''

    for i in range(4):
        url = make_url(username, i)
        ret = requests.get(url, headers={'User-agent': 'your bot 0.1'})
        ret = ret.json()

        for comment in ret['data']['children']:
            comment_text = comment['data']['body']
            comments_text += ' ' + comment_text

    return comments_text
