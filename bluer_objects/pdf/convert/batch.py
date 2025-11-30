from blueness import module

from bluer_objects import NAME
from bluer_objects.metadata import get_from_object
from bluer_objects.pdf.convert.convert import convert
from bluer_objects.env import abcli_path_git
from bluer_objects.logger import logger


NAME = module.name(__file__, NAME)


def batch(
    object_name: str,
    combine: bool,
    count: int = -1,
) -> bool:
    logger.info(
        "{}.batch: {}{}{}".format(
            NAME,
            object_name,
            " + combine" if combine else "",
            "" if count == -1 else f" {count} files",
        )
    )

    list_of_suffixes = get_from_object(
        object_name,
        "pdf",
        [],
    )

    return convert(
        docs_path=abcli_path_git,
        list_of_suffixes=list_of_suffixes,
        object_name=object_name,
        combine=combine,
        count=count,
    )
