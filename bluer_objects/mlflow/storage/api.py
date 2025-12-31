from bluer_objects import env
from bluer_objects.mlflow.storage.primitives import write
from bluer_objects.logger import logger


def set_tag(
    object_name: str,
    key: str,
    value: str,
    log: bool = True,
    verbose: bool = env.MLFLOW_STORAGE_VERBOSE,
    icon="#️⃣ ",
    upload: bool = True,
) -> bool:
    for object_name_, filename_ in {
        f"__keys_{key}": f"{object_name}.yaml",
        "__objects": f"{object_name}.yaml",
    }.items():
        if not write(
            object_name=object_name_,
            filename=filename_,
            data={"value": value},
            upload=upload,
            log=log,
            verbose=verbose,
        ):
            return False

    if log:
        logger.info("{} {}.{}={}".format(icon, object_name, key, value))

    return True
