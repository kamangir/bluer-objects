from blueness import module

from bluer_objects import NAME
from bluer_objects.logger import logger


NAME = module.name(__file__, NAME)


def convert(
    module_name: str,
    object_name: str,
    suffix: str,
) -> bool:
    logger.info(
        "{}.convert {}/{} -> {}".format(
            NAME,
            module_name,
            suffix,
            object_name,
        )
    )

    logger.info("🪄")

    return True
