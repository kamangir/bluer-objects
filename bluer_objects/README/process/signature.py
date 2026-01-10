from typing import List

from bluer_objects import ICON as MY_ICON
from bluer_objects.logger import logger


def signature(
    REPO_NAME: str,
    NAME: str,
    ICON: str,
    MODULE_NAME: str,
    VERSION: str,
) -> List[str]:
    return [
        "",
        " ".join(
            [
                f"[![pylint](https://github.com/kamangir/{REPO_NAME}/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/{REPO_NAME}/actions/workflows/pylint.yml)",
                f"[![pytest](https://github.com/kamangir/{REPO_NAME}/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/{REPO_NAME}/actions/workflows/pytest.yml)",
                f"[![bashtest](https://github.com/kamangir/{REPO_NAME}/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/{REPO_NAME}/actions/workflows/bashtest.yml)",
                f"[![PyPI version](https://img.shields.io/pypi/v/{MODULE_NAME}.svg)](https://pypi.org/project/{MODULE_NAME}/)",
                f"[![PyPI - Downloads](https://img.shields.io/pypi/dd/{MODULE_NAME})](https://pypistats.org/packages/{MODULE_NAME})",
            ]
        ),
        "",
        "built by {} [`{}`]({}), based on {}[`{}-{}`]({}).".format(
            MY_ICON,
            "bluer README",
            "https://github.com/kamangir/bluer-objects/tree/main/bluer_objects/README",
            f"{ICON} " if ICON else "",
            NAME,
            VERSION,
            f"https://github.com/kamangir/{REPO_NAME}",
        ),
    ]
