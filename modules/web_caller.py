import requests


GOOGLE_URL = 'http://www.google.com'


def get_google():
    response = requests.get(GOOGLE_URL)
    response.raise_for_status()
    return response
