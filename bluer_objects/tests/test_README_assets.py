import pytest
from bluer_objects.README.consts import assets_path, asset_volume


@pytest.mark.parametrize(
    ["suffix"],
    [
        ["this"],
        ["that/which"],
    ],
)
@pytest.mark.parametrize(
    ["volume"],
    [
        [""],
        ["2"],
        [2],
    ],
)
def test_README_assets(
    suffix: str,
    volume: str,
):
    volume_path = asset_volume(volume=volume)
    assert isinstance(volume_path, str)
    assert volume_path.endswith(volume_path)

    path = assets_path(
        suffix=suffix,
        volume=volume,
    )

    assert isinstance(path, str)
    assert path.endswith(suffix)
    assert volume_path in path
