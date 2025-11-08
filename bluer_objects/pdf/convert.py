from tqdm import tqdm
from typing import List
import os
import pypandoc
import subprocess

from blueness import module
from bluer_options.logger import crash_report

from bluer_objects import NAME
from bluer_objects import file, objects
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
        filename_md = os.path.join(docs_path, suffix)
        filename_pdf = file.add_extension(
            objects.path_of(
                filename=f"docs/{module_name}/{suffix}",
                object_name=object_name,
            ),
            "pdf",
        )
        filename_html = file.add_extension(
            filename_pdf,
            "html",
        )

        if file.exists(filename_pdf):
            logger.info(f"✅ {filename_pdf}")
            continue

        logger.info(f"{filename_md} -> {filename_pdf}")

        try:
            pypandoc.convert_file(
                filename_md,
                "html",
                outputfile=filename_html,
            )

            subprocess.run(
                [
                    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                    "--headless",
                    "--disable-gpu",
                    f"--print-to-pdf={filename_pdf}",
                    os.path.abspath(filename_html),
                ],
                check=True,
            )
        except Exception as e:
            crash_report(e)
            return False

    return True
