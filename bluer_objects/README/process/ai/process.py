from typing import List

from bluer_objects.README.process.ai import variables
from bluer_objects.README.process.ai.logger import logger


def process_ai(
    template_line: str,
    enabled: bool = True,
) -> List[str]:
    error_message = f"bad template line: {template_line}"

    pieces = template_line.split("ai:::", 1)[1].split(" ", 1)
    if len(pieces) < 1:
        logger.error(error_message)
        return [f"⚠️ {error_message}"]

    task = pieces[0]
    if task == "ignore":
        return []

    if len(pieces) < 2:
        logger.error(error_message)
        return [f"⚠️ {error_message}"]

    if task == "object":
        variables.object_name = pieces[1]
        logger.info(f"object_name={variables.object_name}")
        return []

    return []
