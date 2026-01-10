from typing import Dict

from bluer_objects.logger import logger


variables: Dict[str, str] = {}


def process_variable(template_line: str):
    key, value = template_line.split("set:::", 1)[1].split(" ", 1)
    variables[key] = value
    logger.info(f"{key} = {value}")
