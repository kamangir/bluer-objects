from tqdm import tqdm
from typing import List
import os
import pypandoc
import subprocess

from blueness import module
from bluer_options.logger import crash_report

from bluer_objects import NAME
from bluer_objects import file, objects, path
from bluer_objects.logger import logger


NAME = module.name(__file__, NAME)


def convert(
    docs_path: str,
    module_name: str,
    list_of_suffixes: List[str],
    object_name: str,
) -> bool:
    logger.info(f"docs_path: {docs_path}")

    css = """
    <style>
        body { font-family: sans-serif; margin: 2cm; }
        img { max-width: 100%; height: auto; }
        table { width: 100%; border-collapse: collapse; word-break: break-word; }
        th, td { border: 1px solid #ccc; padding: 4px; vertical-align: top; }
        code, pre { white-space: pre-wrap; }
    </style>
    """

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
        filename_html = file.add_extension(
            objects.path_of(
                filename=f"docs/{module_name}/{suffix}",
                object_name=object_name,
            ),
            "html",
        )
        filename_pdf = file.add_extension(
            filename_html,
            "pdf",
        )

        if file.exists(filename_pdf):
            logger.info(f"✅ {filename_pdf}")
            continue

        logger.info(f"{filename_md} -> {filename_pdf}")

        try:
            with open(filename_md, "r", encoding="utf-8") as f:
                markdown_text = f.read()

            html_text = pypandoc.convert_text(
                markdown_text,
                "html",
                format="md",
            )

            html_text = f"<!DOCTYPE html><html><head>{css}</head><body>{html_text}</body></html>"

            if not path.create(
                file.path(filename_html),
                log=True,
            ):
                return (False,)

            with open(
                filename_html,
                "w",
                encoding="utf-8",
            ) as f:
                f.write(html_text)

            subprocess.run(
                [
                    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                    "--headless",
                    "--disable-gpu",
                    "--no-margins",
                    f"--print-to-pdf={filename_pdf}",
                    os.path.abspath(filename_html),
                ],
                check=True,
            )
        except Exception as e:
            crash_report(e)
            return False

    return True
