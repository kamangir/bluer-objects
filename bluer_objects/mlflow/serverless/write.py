from typing import Dict, Union

from blueness import module
from bluer_options.options import Options

from bluer_objects import NAME
from bluer_objects import file
from bluer_objects import objects
from bluer_objects import storage
from bluer_objects.logger import logger

NAME = module.name(__file__, NAME)


def set_tags(
    object_name: str,
    tags: Union[str, Dict[str, str]],
    log: bool = True,
    verbose: bool = False,
    icon="#️⃣ ",
) -> bool:
    tags = Options(tags)

    # f"_serverless_objects/{object_name}.yaml"

    filename = objects.path_of(
        object_name="_serverless_objects",
        filename=f"{object_name}.yaml",
    )

    if not storage.download(
        object_name="_serverless_objects",
        filename=f"{object_name}.yaml",
        log=verbose,
    ):
        return False

    _, current_tags = file.load_yaml(
        filename,
        ignore_error=True,
        default={},
    )
    if not isinstance(current_tags, dict):
        logger.error(
            "dict expected, {} received".format(
                current_tags.__class__.__name__,
            )
        )
        return False

    tags = Options(tags)
    current_tags.update(tags)

    if not file.save_yaml(
        filename,
        current_tags,
        log=verbose,
    ):
        return False

    if not storage.upload(
        object_name="_serverless_objects",
        filename=f"{object_name}.yaml",
        log=verbose,
    ):
        return False

    # f"_serverless_key_{key}/{object_name}.yaml"
    for key, value in tags.items():
        if not file.save_yaml(
            objects.path_of(
                object_name=f"_serverless_key_{key}",
                filename=f"{object_name}.yaml",
            ),
            {"value": value},
            log=verbose,
        ):
            return False

        if not storage.upload(
            object_name=f"_serverless_key_{key}",
            filename=f"{object_name}.yaml",
            log=verbose,
        ):
            return False

        if log:
            logger.info("{} {}.{}={}".format(icon, object_name, key, value))

    return True
