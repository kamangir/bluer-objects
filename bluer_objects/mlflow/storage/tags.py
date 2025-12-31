from typing import Tuple, Dict, Union

from blueness import module
from bluer_options.options import Options

from bluer_objects import NAME
from bluer_objects.logger import logger

NAME = module.name(__file__, NAME)


def get_tags(
    object_name: str,
    exclude_system_tags: bool = True,
) -> Tuple[bool, Dict[str, str]]:

    return True, {}


def set_tag_internal(
    object_name: str,
    key: str,
    value: str,
    log: bool = True,
    icon="#️⃣ ",
) -> bool:
    if log:
        logger.info("{} {}.{}={}".format(icon, object_name, key, value))

    return True


def set_tags(
    object_name: str,
    tags: Union[str, Dict[str, str]],
    log: bool = True,
    icon="#️⃣ ",
) -> bool:
    tags = Options(tags)

    return all(
        set_tag_internal(
            object_name,
            key=key,
            value=value,
            log=log,
            icon=icon,
        )
        for key, value in tags.items()
    )
