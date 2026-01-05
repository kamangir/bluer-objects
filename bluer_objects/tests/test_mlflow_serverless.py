import pytest

from bluer_options.options import Options

from bluer_objects.objects import unique_object
from bluer_objects.mlflow.serverless import get_tags, set_tags


@pytest.mark.parametrize(
    ["tags_str"],
    [["x=1,y=2,z=3"]],
)
def test_mlflow_serverless_tags_set_get(tags_str: str):
    object_name = unique_object("test_mlflow_serverless_tags_set_get")

    assert set_tags(
        object_name,
        tags_str,
        log=False,
    )

    success, tags_read = get_tags(object_name)
    assert success

    tags_option = Options(tags_str)
    for keyword, value in tags_option.items():
        assert tags_read[keyword] == value
