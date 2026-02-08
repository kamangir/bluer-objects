import qrcode

from blueness import module

from bluer_objects import objects
from bluer_objects import NAME
from bluer_objects.logger import logger


NAME = module.name(__file__, NAME)


def generate(
    url: str,
    object_name: str,
    filename: str,
) -> bool:
    logger.info(
        "{}.generate({}) -> {}/{}".format(
            NAME,
            url,
            object_name,
            filename,
        )
    )

    try:
        image = qrcode.make(url)
        image.save(
            objects.path_of(
                object_name=object_name,
                filename=filename,
            )
        )
    except Exception as e:
        logger.error(e)
        return False

    return True
