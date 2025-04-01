import pytest
import numpy as np

from bluer_options import string

from bluer_objects import file, path, objects
from bluer_objects import storage
from bluer_objects.logger import logger


@pytest.fixture
def test_object():
    object_name = objects.unique_object("test_object")
    for suffix in range(10):
        assert file.save_image(
            objects.path_of(
                object_name=object_name,
                filename=f"test-{suffix:02d}.png",
            ),
            (np.random.rand(512, 512, 3) * 255).astype(np.uint8),
        )

    depth = 10
    data = {
        string.random(length=depth): string.random(length=depth) for _ in range(depth)
    }

    assert file.save_yaml(
        objects.path_of(
            object_name=object_name,
            filename="test.yaml",
        ),
        data,
    )

    assert file.save_json(
        objects.path_of(
            object_name=object_name,
            filename="test.json",
        ),
        data,
    )

    yield object_name

    logger.info(f"deleting test_object ...")


@pytest.mark.parametrize(
    ["cloud"],
    [[True], [False]],
)
def test_objects_list_of_files(
    test_object,
    cloud: bool,
):
    if cloud:
        # TODO: enable when implemented
        return

    list_of_files = [
        file.name_and_extension(filename)
        for filename in objects.list_of_files(
            object_name=test_object,
            cloud=cloud,
        )
    ]

    assert "test-00.png" in list_of_files


def test_object_object_path():
    object_name = objects.unique_object("test_object_object_path")
    object_path = objects.object_path(object_name, create=True)
    assert object_path
    assert path.exists(object_path)


def test_objects_path_of(test_object):
    assert file.exists(
        objects.path_of(
            object_name=test_object,
            filename="test-00.png",
        )
    )


@pytest.mark.parametrize(
    ["prefix"],
    [["test_objects_unique_object"]],
)
def test_objects_unique_object(prefix: str):
    object_name = objects.unique_object(prefix)
    assert object_name
    assert object_name.startswith(prefix)
