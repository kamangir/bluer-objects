import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_objects import NAME
from bluer_objects.pdf.convert import convert
from bluer_objects.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="convert",
)
parser.add_argument(
    "--module_name",
    type=str,
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--suffix",
    type=str,
)
args = parser.parse_args()

success = False
if args.task == "convert":
    success = convert(
        module_name=args.module_name,
        object_name=args.object_name,
        suffix=args.suffix,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
