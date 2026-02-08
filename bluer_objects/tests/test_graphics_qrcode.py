from bluer_options.env import BLUER_AI_WEB_IS_ACCESSIBLE
from bluer_options import string

from bluer_objects import objects
from bluer_objects.graphics import qrcode


def test_graphics_qrcode():
    object_name = objects.unique_object("test_graphics_qrcode")

    assert qrcode.generate(
        url="BLUER_AI_WEB_IS_ACCESSIBLE",
        object_name=object_name,
        filename="{}.png".format(string.timestamp()),
    )
