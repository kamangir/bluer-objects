from bluer_objects.storage.base import StorageInterface
from bluer_objects.storage.WebDAV import WebDAVInterface
from bluer_objects.storage.WebDAVzip import WebDAVzipInterface
from bluer_objects import env
from bluer_objects.logger import logger

interface = StorageInterface()

if env.BLUER_OBJECTS_STORAGE_INTERFACE == WebDAVInterface.name:
    interface = WebDAVInterface()
elif env.BLUER_OBJECTS_STORAGE_INTERFACE == WebDAVzipInterface.name:
    interface = WebDAVzipInterface()
else:
    logger.error(f"{env.BLUER_OBJECTS_STORAGE_INTERFACE}: interface not found.")
    assert False


def download(
    object_name: str,
    filename: str = "",
    log: bool = True,
) -> bool:
    return interface.download(
        object_name=object_name,
        filename=filename,
        log=log,
    )


def upload(
    object_name: str,
    filename: str = "",
    log: bool = True,
) -> bool:
    return interface.upload(
        object_name=object_name,
        filename=filename,
        log=log,
    )
