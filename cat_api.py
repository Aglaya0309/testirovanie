import requests

def get_random_cat_image():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    if response.ok:
        try:
            return response.json()[0]['url']
        except (ValueError, IndexError, KeyError):
            pass
    return None