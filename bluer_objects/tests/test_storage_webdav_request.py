from bluer_objects import objects
from bluer_objects.testing import create_test_asset
from bluer_objects.storage import WebDAVRequestInterface


def test_storage_webdav_request():
    object_name = objects.unique_object("test_storage_webdav_request")

    assert create_test_asset(
        object_name=object_name,
        depth=10,
    )

    storage = WebDAVRequestInterface()

    for filename in [
        "this.yaml",
        "subfolder/this.yaml",
        "test-00.png",
    ]:
        assert storage.upload(
            object_name=object_name,
            filename=filename,
        )

    assert storage.upload(object_name=object_name)

    for filename in [
        "this.yaml",
        "subfolder/this.yaml",
        "test-00.png",
    ]:
        assert storage.download(
            object_name=object_name,
            filename=filename,
        )

    # TODO: enable
    # assert storage.download(object_name=object_name)
