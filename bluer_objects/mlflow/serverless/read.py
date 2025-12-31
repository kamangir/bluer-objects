from typing import Tuple, Dict, Union

from blueness import module
from bluer_options.options import Options

from bluer_objects import NAME
from bluer_objects import env
from bluer_objects import file
from bluer_objects import objects
from bluer_objects import storage
from bluer_objects.logger import logger

NAME = module.name(__file__, NAME)


def get_tags(
    object_name: str,
    exclude_system_tags: bool = True,
    log: bool = True,
) -> Tuple[bool, Dict[str, str]]:
    if not storage.download(
        object_name="_serverless_objects",
        filename=f"{object_name}.yaml",
        log=log,
    ):
        return True, {}

    return file.load_yaml(
        objects.path_of(
            object_name="_serverless_objects",
            filename=f"{object_name}.yaml",
        ),
        ignore_error=True,
        default={},
    )
