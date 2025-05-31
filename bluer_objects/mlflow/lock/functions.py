from blueness import module

from bluer_objects import NAME
from bluer_objects.logger import logger


NAME = module.name(__file__, NAME)


def func(arg: str) -> bool:
    logger.info(f"{NAME}.func: arg={arg}")
    return True
