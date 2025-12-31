import pytest

from bluer_options.options import Options

from bluer_objects.objects import unique_object
from bluer_objects.mlflow.storage import tags


@pytest.mark.parametrize(
    ["tags_str"],
    [["x=1,y=2,z=3"]],
)
def test_mlflow_storage_tag_set_get(tags_str: str):
    object_name = unique_object("test_mlflow_storage_tag_set_get")

    assert tags.set_tags(
        object_name,
        tags_str,
        log=False,
    )

    success, tags_read = tags.get_tags(object_name)
    assert success

    tags_option = Options(tags_str)
    for keyword, value in tags_option.items():
        assert tags_read[keyword] == value
