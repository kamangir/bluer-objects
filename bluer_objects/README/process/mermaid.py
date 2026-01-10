from typing import List

from bluer_objects.logger import logger


def process_mermaid(template_line: str) -> List[str]:
    template_line_pieces = template_line.split('"')
    if len(template_line_pieces) != 3:
        logger.error(f"🧜🏽‍♀️  mermaid line not in expected format: {template_line}.")
        return False

    template_line_pieces[1] = (
        template_line_pieces[1]
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace(" ", "<br>")
        .replace("~~", " ")
    )

    return ['"'.join(template_line_pieces)]
