from typing import List, Tuple
import requests
from requests.auth import HTTPBasicAuth

from bluer_objects.storage.base import StorageInterface
from bluer_objects import env, file, path
from bluer_objects import objects
from bluer_objects.logger import logger


# https://chatgpt.com/c/6824cf43-6738-8005-8733-54b6a77f20ee
class WebDAVRequestInterface(StorageInterface):
    name = "webdav-request"

    def __init__(self):
        super().__init__()

    def mkdir(
        self,
        path: str,
        log: bool = True,
    ) -> bool:
        url = f"{env.WEBDAV_HOSTNAME}/"
        for folder in path.split("/"):
            url = f"{url}{folder}/"

            try:
                response = requests.request(
                    "MKCOL",
                    url,
                    auth=HTTPBasicAuth(
                        env.WEBDAV_LOGIN,
                        env.WEBDAV_PASSWORD,
                    ),
                )
            except Exception as e:
                logger.error(e)
                return False

            if response.status_code == 405:  # Already exists
                continue

            if response.status_code == 201:  # Created
                if log:
                    logger.info(
                        "{}.mkdir {}".format(
                            self.__class__.__name__,
                            url.split(env.WEBDAV_HOSTNAME, 1)[1],
                        )
                    )
                continue

            logger.error(
                f"failed to create directory: {response.status_code} - {response.text}"
            )
            return False

        return True
