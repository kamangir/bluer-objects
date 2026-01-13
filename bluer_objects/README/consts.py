import os
from typing import Union

from bluer_objects.env import abcli_path_git

github_kamangir = "https://github.com/kamangir"
designs_repo = f"{github_kamangir}/bluer-designs/"


def designs_url(suffix: str) -> str:
    return "{}/blob/main{}".format(
        designs_repo,
        f"/{suffix}" if suffix else "",
    )


def assets_url(
    suffix: str = "",
    volume: Union[str, int] = "",
    blob: bool = False,
) -> str:
    return "{}/assets{}/{}/main{}".format(
        github_kamangir,
        str(volume),
        "blob" if blob else "raw",
        f"/{suffix}" if suffix else "",
    )


assets = assets_url(volume="")
assets2 = assets_url(volume="2")


def assets_path(
    suffix: str = "",
    volume: Union[str, int] = "",
) -> str:
    return os.path.join(
        abcli_path_git,
        "assets{}{}".format(
            str(volume),
            f"/{suffix}" if suffix else "",
        ),
    )
