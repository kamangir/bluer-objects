from bluer_ai.tests.test_env import test_bluer_ai_env

from bluer_objects import env
from bluer_objects.storage import (
    ArvancloudInterface,
    WebDAVInterface,
    WebDAVRequestInterface,
    WebDAVzipInterface,
)


def test_required_env():
    test_bluer_ai_env()


def test_bluer_objects_env():
    assert env.ABCLI_MLFLOW_EXPERIMENT_PREFIX

    assert env.ARVANCLOUD_STORAGE_BUCKET

    assert env.ARVANCLOUD_STORAGE_ENDPOINT_URL
    assert env.ARVANCLOUD_STORAGE_AWS_ACCESS_KEY_ID
    assert env.ARVANCLOUD_STORAGE_AWS_SECRET_ACCESS_KEY

    assert env.BLUER_OBJECTS_STORAGE_INTERFACE in [
        ArvancloudInterface.name,
        WebDAVInterface.name,
        WebDAVRequestInterface.name,
        WebDAVzipInterface.name,
    ]

    assert env.MLFLOW_DEPLOYMENT

    assert env.WEBDAV_HOSTNAME
    assert env.WEBDAV_LOGIN
    assert env.WEBDAV_PASSWORD
