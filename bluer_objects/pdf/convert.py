from tqdm import tqdm
from typing import List
import os
import pypandoc

from blueness import module
from bluer_options.logger import crash_report

from bluer_objects import NAME
from bluer_objects import objects
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
        input_filename = os.path.join(docs_path, suffix)
        outputs_filename = objects.path_of(
            filename=f"{module_name}/{suffix}",
            object_name=object_name,
        )

        logger.info(f"{input_filename} -> {outputs_filename}")

        try:
            pypandoc.convert_text(
                open(input_filename).read(),
                "pdf",
                format="md",
                outputfile=outputs_filename,
                extra_args=["--standalone"],
            )
        except Exception as e:
            crash_report(e)
            return False

    return True
