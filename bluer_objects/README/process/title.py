import os
from typing import List, Tuple

from bluer_objects import file
from bluer_objects.logger import logger


def process_title(
    template_line: str,
    filename: str,
) -> Tuple[bool, List[str]]:
    template_line_pieces = [
        piece for piece in template_line.strip().split(":::") if piece
    ]
    reference = template_line_pieces[1] if len(template_line_pieces) >= 2 else "docs"

    filename_path_pieces = file.path(filename).split(os.sep)
    if reference not in filename_path_pieces:
        logger.error(
            "reference: {} not found in {}.".format(
                reference,
                template_line,
            )
        )
        return False, []

    title_pieces = filename_path_pieces[filename_path_pieces.index(reference) + 1 :]
    filename_name = file.name(filename)
    if filename_name != "README":
        title_pieces.append(filename_name)

    return True, [
        "# {}".format(
            ": ".join(
                [
                    piece.replace(
                        "_",
                        "-",
                    )
                    for piece in title_pieces
                ]
            )
        )
    ]
