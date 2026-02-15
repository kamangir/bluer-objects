from typing import List
import yaml

from bluer_options.logger import shorten_text

from bluer_objects.metadata import get_from_object
from bluer_objects.logger import logger


def process_metadata(
    template_line: str,
    download: bool = True,
) -> List[str]:
    object_name_and_key = template_line.split("metadata:::", 1)[1]
    if " " in object_name_and_key:
        object_name_and_key = object_name_and_key.split(" ", 1)[0]
    if ":::" not in object_name_and_key:
        object_name_and_key += ":::"
    object_name, key = object_name_and_key.split(":::", 1)

    value = get_from_object(
        object_name,
        key,
        {},
        download=download,
    )

    logger.info(shorten_text(f"metadata[{object_name_and_key}] = {value}"))

    if template_line.startswith("metadata:::"):
        return (
            ["```yaml"]
            + yaml.dump(
                value,
                default_flow_style=False,
            ).split("\n")
            + ["```"]
        )

    return [
        template_line.replace(
            f"metadata:::{object_name}:::{key}",
            str(value),
        )
    ]
