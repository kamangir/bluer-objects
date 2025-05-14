from bluer_objects import objects
from bluer_objects.testing import create_test_asset
from bluer_objects.storage import WebDAVzipInterface


def test_storage_webdav_zip():
    object_name = objects.unique_object("test_storage_webdav_zip")

    assert create_test_asset(
        object_name=object_name,
        depth=10,
    )

    storage = WebDAVzipInterface()

    assert storage.upload(object_name=object_name)

    assert storage.download(object_name=object_name)
