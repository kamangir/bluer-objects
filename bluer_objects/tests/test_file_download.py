import pytest

from bluer_options.env import BLUER_AI_WEB_IS_ACCESSIBLE
from bluer_ai.env import BLUER_AI_WEB_CHECK_URL

from bluer_objects import objects, file


@pytest.mark.parametrize(
    ["url"],
    [
        [BLUER_AI_WEB_CHECK_URL],
    ],
)
def test_file_download(url: str):
    if not BLUER_AI_WEB_IS_ACCESSIBLE:
        return

    object_name = objects.unique_object("test_file_download")

    filename = objects.path_of(
        object_name=object_name,
        filename=url.split("/")[-1],
    )

    assert file.download(
        url=url,
        filename=filename,
    )

    assert file.exists(filename)
