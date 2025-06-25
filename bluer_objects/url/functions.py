import requests

from bluer_objects.logger import logger


def is_accessible(url) -> bool:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False
