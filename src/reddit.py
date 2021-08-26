import requests

count = 25
pages = 4
user_agent = 'pedromelgueira.com Markov 1.0'


def make_url(username, step):
    query_string = '?count={}&after={}'.format(count * (step + 1), count * step)
    return 'https://www.reddit.com/user/{}/comments/.json{}'.format(username, query_string)


def get_comments_text(username):
    comments_text = ''

    for i in range(pages):
        url = make_url(username, i)
        ret = requests.get(url, headers={'User-agent': user_agent})
        ret = ret.json()

        for comment in ret['data']['children']:
            comment_text = comment['data']['body']
            comments_text += ' ' + comment_text

    return comments_text
