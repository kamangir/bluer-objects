from typing import Dict

from bluer_objects import file
from bluer_objects import objects
from bluer_objects import storage

object_name = "tags"


def write(
    object_name: str,
    filename: str,
    data: Dict,
    upload: bool = True,
    log: bool = True,
    verbose: bool = False,
) -> bool:
    return file.save_yaml(
        filename=objects.path_of(
            object_name=object_name,
            filename=filename,
        ),
        data=data,
        log=verbose,
    ) and (
        not upload
        or storage.upload(
            object_name=object_name,
            filename=filename,
            log=log,
        )
    )
