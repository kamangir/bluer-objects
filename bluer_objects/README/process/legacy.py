from typing import List

from bluer_objects.logger import logger


def apply_legacy_on_line(line: str) -> str:
    for before, after in {
        "yaml:::": "metadata:::",
        "--help--": "help:::",
        "--include": "include:::",
        "--table--": "items:::",
        "--signature--": "signature:::",
    }.items():
        line = line.replace(before, after)
    return line


def apply_legacy(template: List[str]) -> List[str]:
    logger.info("applying legacy conversions...")
    template = [apply_legacy_on_line(line) for line in template]
    return template
