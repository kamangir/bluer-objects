import requests
from requests.auth import HTTPBasicAuth
import glob
from typing import Tuple, List
from xml.etree import ElementTree as ET

from bluer_objects.storage.base import StorageInterface
from bluer_objects import env, file, path
from bluer_objects import objects
from bluer_objects.logger import logger


# https://chatgpt.com/c/6824cf43-6738-8005-8733-54b6a77f20ee
class WebDAVRequestInterface(StorageInterface):
    name = "webdav-request"

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

    def download(
        self,
        object_name: str,
        filename: str = "",
        log: bool = True,
    ) -> bool:
        if filename:
            local_path = objects.path_of(
                object_name=object_name,
                filename=filename,
                create=True,
            )

            if not path.create(file.path(local_path)):
                return False

            url = f"{env.WEBDAV_HOSTNAME}/{object_name}/{filename}"

            try:
                response = requests.get(
                    url,
                    auth=HTTPBasicAuth(
                        env.WEBDAV_LOGIN,
                        env.WEBDAV_PASSWORD,
                    ),
                )
            except Exception as e:
                logger.error(e)
                return False

            if response.status_code == 200:
                try:
                    with open(local_path, "wb") as file_:
                        file_.write(response.content)
                except Exception as e:
                    logger.error(e)
                    return False

                return super().download(
                    object_name=object_name,
                    filename=filename,
                    log=log,
                )

            logger.error(f"failed to download: {response.status_code}")
            return False

        logger.error("not implemented")
        return False

    def ls(
        self,
        object_name: str,
        where: str = "local",
    ) -> Tuple[bool, List[str]]:
        if where == "cloud":
            # https://chatgpt.com/c/6824f8d3-d9c0-8005-a7fa-d646f812f4b7
            headers = {
                "Depth": "infinity",
                "Content-Type": "application/xml",
            }

            # Minimal PROPFIND XML body
            data = """<?xml version="1.0"?>
            <d:propfind xmlns:d="DAV:">
            <d:prop><d:displayname/></d:prop>
            </d:propfind>"""

            response = requests.request(
                method="PROPFIND",
                url=f"{env.WEBDAV_HOSTNAME}/{object_name}/",
                data=data,
                headers=headers,
                auth=HTTPBasicAuth(
                    env.WEBDAV_LOGIN,
                    env.WEBDAV_PASSWORD,
                ),
            )

            if response.status_code == 404:  # object not found
                return True, []
            elif response.status_code in (207, 207):
                tree = ET.fromstring(response.content)
                ns = {"d": "DAV:"}
                files = []
                for resp in tree.findall("d:response", ns):
                    href = resp.find("d:href", ns).text
                    files.append(href)

                return True, sorted(
                    [
                        filename
                        for filename in [
                            filename.split(f"{env.WEBDAV_LOGIN}/{object_name}/", 1)[1]
                            for filename in files
                            if not filename.endswith("/")
                        ]
                        if filename
                    ]
                )
            else:
                logger.error(
                    f"failed to list: {response.status_code} - {response.text}"
                )
                return False, []

        return super().ls(
            object_name=object_name,
            where=where,
        )

    def upload(
        self,
        object_name: str,
        filename: str = "",
        log: bool = True,
    ) -> bool:
        if filename:
            if not self.mkdir(
                path="{}/{}".format(
                    object_name,
                    file.path(filename),
                ),
                log=log,
            ):
                return False

            url = f"{env.WEBDAV_HOSTNAME}/{object_name}/{filename}"

            local_path = objects.path_of(
                object_name=object_name,
                filename=filename,
            )

            try:
                with open(local_path, "rb") as file_data:
                    response = requests.put(
                        url,
                        data=file_data,
                        auth=HTTPBasicAuth(
                            env.WEBDAV_LOGIN,
                            env.WEBDAV_PASSWORD,
                        ),
                    )
            except Exception as e:
                logger.error(e)
                return False

            if response.status_code in [200, 201, 204]:
                return super().upload(
                    object_name=object_name,
                    filename=filename,
                    log=log,
                )

            logger.error(f"failed to upload: {response.status_code} - {response.text}")
            return False

        object_path = "{}/".format(objects.object_path(object_name=object_name))
        for filename_ in glob.glob(
            objects.path_of(
                object_name=object_name,
                filename="**",
            ),
            recursive=True,
        ):
            if not file.exists(filename_):
                continue

            if not self.upload(
                object_name=object_name,
                filename=filename_.split(object_path, 1)[1],
                log=log,
            ):
                return False

        return True
