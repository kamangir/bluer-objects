from tqdm import tqdm
from typing import List
import os

from blueness import module

from bluer_objects import NAME
from bluer_objects.env import abcli_path_git
from bluer_objects.logger import logger


NAME = module.name(__file__, NAME)


def convert(
    docs_path: str,
    module_name: str,
    list_of_suffixes: List[str],
    object_name: str,
) -> bool:
    logger.info(f"docs_path: {docs_path}")

    for suffix in tqdm(list_of_suffixes):
        logger.info(
            "{}.convert {}/{} -> {}".format(
                NAME,
                module_name,
                suffix,
                object_name,
            )
        )

        if not suffix.endswith(".md"):
            suffix = os.path.join(suffix, "README.md")
        filename = os.path.join(docs_path, suffix)

        

        logger.info("🪄")

    return True
