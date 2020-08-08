import requests


def get_content_type(url):
    request = requests.get(url)
    return request.headers['Content-Type']
