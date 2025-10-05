import pytest
from bluer_objects.README.consts import assets_path


@pytest.mark.parametrize(
    ["suffix", "volume"],
    [
        [
            "this",
            "that/which",
        ],
        [
            "",
            "2",
            2,
        ],
    ],
)
def test_README_assets(
    suffix: str,
    volume: str,
):
    path = assets_path(
        suffix=suffix,
        volume=volume,
    )

    assert isinstance(path, str)
    assert path.endswith(suffix)
    assert f"assets{str(volume)}" in path
