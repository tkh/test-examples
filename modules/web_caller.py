import requests


GOOGLE_URL = 'http://www.google.com'


def get_google():
    return requests.get(GOOGLE_URL)
