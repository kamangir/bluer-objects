from typing import Union

github_kamangir = "https://github.com/kamangir"


def asset_volume(volume: Union[str, int] = "") -> str:
    return f"{github_kamangir}/assets{str(volume)}/raw/main"


assets = asset_volume(volume="")
assets2 = asset_volume(volume="2")


def assets_path(
    path: str,
    volume: Union[str, int] = "",
) -> str:
    return f"{assets}{str(volume)}/{path}"
