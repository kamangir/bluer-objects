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
    for suffix in [
        f"keys/{key}/{object_name}",
        f"objects/{object_name}/{key}",
    ]:
        if not write(
            suffix=suffix,
            data={"value": value},
            upload=upload,
            log=log,
            verbose=verbose,
        ):
            return False

    if log:
        logger.info("{} {}.{}={}".format(icon, object_name, key, value))

    return True
