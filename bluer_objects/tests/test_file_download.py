import pytest

from bluer_objects import objects, file


@pytest.mark.parametrize(
    ["url"],
    [
        ["https://raw.githubusercontent.com/jbrownlee/Datasets/master/shampoo.csv"],
    ],
)
def test_file_download(url: str):
    object_name = objects.unique_object("test_file_download")

    assert file.download(
        url=url,
        filename=objects.path_of(
            object_name=object_name,
            filename=url.split("/")[-1],
        ),
    )
