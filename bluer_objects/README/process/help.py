from typing import List, Union, Callable, Tuple

from bluer_objects.logger import logger


def process_help(
    template_line: str,
    help_function: Union[Callable[[List[str]], str], None] = None,
) -> Tuple[bool, List[str]]:
    help_command = template_line.split("help:::")[1].strip()

    tokens = help_command.strip().split(" ")[1:]

    help_content = help_function(tokens)
    if not help_content:
        logger.error(f"help not found: {help_command}: {tokens}")
        return False, []

    logger.info(f"+= help: {help_command}")
    print(help_content)
    content_section = [
        "```bash",
        help_content,
        "```",
    ]

    return True, content_section
