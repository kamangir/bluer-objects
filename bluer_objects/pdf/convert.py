from tqdm import tqdm
from typing import List
import os
import pypandoc
import subprocess
from PyPDF2 import PdfMerger
from PIL import Image

from blueness import module
from bluer_options.logger import crash_report

from bluer_objects import NAME
from bluer_objects.env import abcli_path_git
from bluer_objects import file, objects, path
from bluer_objects.metadata import get_from_object, post_to_object
from bluer_objects.logger import logger


NAME = module.name(__file__, NAME)


def convert(
    docs_path: str,
    module_name: str,
    list_of_suffixes: List[str],
    object_name: str,
    combine: bool,
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

    list_of_pdfs: List[str] = get_from_object(
        object_name,
        "list_of_pdfs",
        [],
    )
    logger.info(f"found {len(list_of_pdfs)} pdf(s)...")

    for suffix in tqdm(list_of_suffixes):
        logger.info(
            "{}.convert {}/{} -> {}".format(
                NAME,
                module_name,
                suffix,
                object_name,
            )
        )

        source_filename = os.path.join(docs_path, suffix)
        if path.exists(source_filename):
            source_filename = os.path.join(source_filename, "README.md")
            suffix = os.path.join(suffix, "README.md")

        if source_filename.endswith(".md"):
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

            if filename_pdf not in list_of_pdfs:
                list_of_pdfs.append(filename_pdf)

            if file.exists(filename_pdf):
                logger.info(f"✅ {filename_pdf}")
                continue

            logger.info(f"{source_filename} -> {filename_pdf}")

            try:
                with open(source_filename, "r", encoding="utf-8") as f:
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
        elif file.extension(source_filename) == "pdf":
            logger.info("🌠 pdf found!")
            filename_pdf = file.add_extension(
                objects.path_of(
                    filename="docs/{}".format(
                        (
                            suffix.split(abcli_path_git, 1)[1]
                            if abcli_path_git in suffix
                            else suffix
                        ),
                    ),
                    object_name=object_name,
                ),
                "pdf",
            )

            if filename_pdf not in list_of_pdfs:
                list_of_pdfs.append(filename_pdf)

            if file.exists(filename_pdf):
                logger.info(f"✅ {filename_pdf}")
                continue

            if not file.copy(
                source_filename,
                filename_pdf,
            ):
                return False

            logger.info(f"-> {filename_pdf}")
        elif file.extension(source_filename) in [
            extension.split(".", 1)[1]
            for extension in Image.registered_extensions().keys()
        ]:
            logger.info("🌠 image found!")
            filename_pdf = file.add_extension(
                objects.path_of(
                    filename="docs/{}".format(
                        (
                            suffix.split(abcli_path_git, 1)[1]
                            if abcli_path_git in suffix
                            else suffix
                        ),
                    ),
                    object_name=object_name,
                ),
                "pdf",
            )

            if filename_pdf not in list_of_pdfs:
                list_of_pdfs.append(filename_pdf)

            if file.exists(filename_pdf):
                logger.info(f"✅ {filename_pdf}")
                continue

            if not path.create(
                file.path(filename_pdf),
                log=True,
            ):
                return False

            try:
                image = Image.open(source_filename)
                image = image.convert("RGB")
                image.save(filename_pdf)
            except Exception as e:
                crash_report(e)
                return False

            logger.info(f"-> {filename_pdf}")
        else:
            logger.error(f"{source_filename}: cannot convert to pdf.")
            return False

    logger.info(f"{len(list_of_pdfs)} pdf(s) so far ...")
    if not post_to_object(
        object_name,
        "list_of_pdfs",
        list_of_pdfs,
    ):
        return False

    if combine:
        logger.info(f"combining {len(list_of_pdfs)} pdf(s)...")
        combined_filename = objects.path_of(
            filename="release.pdf",
            object_name=object_name,
        )

        try:
            merger = PdfMerger()
            for filename in list_of_pdfs:
                merger.append(filename)

            merger.write(combined_filename)
            merger.close()
        except Exception as e:
            crash_report(e)
            return False

        logger.info(f"-> {combined_filename}")

    return True
