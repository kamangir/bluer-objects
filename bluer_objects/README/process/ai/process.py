from typing import List

from bluer_objects.README.process.ai import variables
from bluer_objects.README.process.ai.logger import logger


def process_ai(template_line: str) -> List[str]:
    pieces = template_line.split("ai:::", 1)[1].split(" ", 1)
    if len(pieces) < 2:
        logger.warning(f"bad template line: {template_line}")
        return [
            f"⚠️ bad template line: {template_line}",
        ]

    task = pieces[0]
    if task == "ignore":
        return []

    if task == "object":
        variables.object_name = pieces[1]
        logger.info(f"object_name={variables.object_name}")
        return []

    return []
