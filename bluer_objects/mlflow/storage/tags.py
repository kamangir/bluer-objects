from typing import Tuple, Dict, Union

from blueness import module
from bluer_options.options import Options

from bluer_objects import NAME
from bluer_objects import env
from bluer_objects import storage
from bluer_objects.mlflow.storage import api
from bluer_objects.mlflow.storage import primitives
from bluer_objects.logger import logger

NAME = module.name(__file__, NAME)


def get_tags(
    object_name: str,
    exclude_system_tags: bool = True,
) -> Tuple[bool, Dict[str, str]]:

    success, list_of_files = storage.ls(
        object_name=primitives.object_name,
        where="cloud",
    )
    if not success:
        return False, {}
    
    

    return True, {}


def set_tags(
    object_name: str,
    tags: Union[str, Dict[str, str]],
    log: bool = True,
    icon="#️⃣ ",
) -> bool:
    tags = Options(tags)

    return all(
        api.set_tag(
            object_name,
            key=key,
            value=value,
            log=log,
            verbose=env.MLFLOW_STORAGE_VERBOSE,
            icon=icon,
        )
        for key, value in tags.items()
    )
