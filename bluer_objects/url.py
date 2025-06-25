import requests

from bluer_objects.logger import logger


def is_accessible(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        logger.error(e)
        return False
