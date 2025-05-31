from blueness import module
from bluer_options import string

from bluer_objects import NAME
from bluer_objects.mlflow.lock.classes import Lock
from bluer_objects.logger import logger


NAME = module.name(__file__, NAME)


def lock(
    object_name: str,
    lock_name: str = "lock",
    timeout: int = -1,
    verbose: bool = False,
) -> bool:
    logger.info(
        "{}.lock: {}.{} @ {}".format(
            NAME,
            object_name,
            lock_name,
            string.pretty_duration(timeout),
        )
    )

    logger.info("🪄")

    return True


def unlock(
    object_name: str,
    lock_name: str = "lock",
    verbose: bool = False,
) -> bool:
    logger.info(
        "{}.unlock: {}.{}".format(
            NAME,
            object_name,
            lock_name,
        )
    )

    logger.info("🪄")

    return True
