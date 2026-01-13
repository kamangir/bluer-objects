from typing import List

from bluer_options import env
from bluer_options.help.parsing import list_of_modules

from bluer_objects import file
from bluer_objects import path
from bluer_objects.env import abcli_path_git
from bluer_objects.README.consts import github_kamangir
from bluer_objects.logger import logger


def process_national_internet(
    filename: str,
    content: List[str],
) -> List[str]:
    if env.BLUER_AI_WEB_STATUS == "online":
        return content

    logger.info("🇮🇷 national internet adjustments...")

    for this, that in {
        "{}/{}/{}/main".format(
            github_kamangir,
            repo_name,
            "blob" if blob else "raw",
        ): "{}/{}".format(
            abcli_path_git,
            repo_name,
        )
        for repo_name in (
            [
                "assets",
                "assets2",
            ]
            + [module.replace("_", "-") for module in list_of_modules]
        )
        for blob in [
            False,
            True,
        ]
    }.items():
        content = [
            line.replace(
                this,
                path.relative(
                    that,
                    file.path(filename),
                ),
            )
            for line in content
        ]

    return content
