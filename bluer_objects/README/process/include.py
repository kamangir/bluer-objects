from typing import List

from bluer_objects import file
from bluer_objects import NAME as MY_NAME
from bluer_objects.logger import logger


def process_include(
    template_line: str,
    template_path: str,
) -> List[str]:
    include_filename_relative = template_line.split(" ")[1].strip()
    include_filename = file.absolute(
        include_filename_relative,
        template_path,
    )

    success, content_section = file.load_text(include_filename)
    if not success:
        return success

    content_section = [
        line for line in content_section if not line.startswith("used by:")
    ]

    include_title = (template_line.split(" ", 2) + ["", "", ""])[2]
    if include_title:
        content_section = [f"## {include_title}"] + content_section[1:]

    if "include:::noref" not in template_line:
        content_section += [
            "using [{}]({}).".format(
                file.name(include_filename),
                include_filename_relative,
            )
        ]

    logger.info(f"{MY_NAME}.build: including {include_filename} ...")

    return content_section
