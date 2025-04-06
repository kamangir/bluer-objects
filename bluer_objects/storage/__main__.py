import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_objects import NAME
from bluer_objects import storage
from bluer_objects.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="download | ls | upload",
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--filename",
    type=str,
    default="",
)
parser.add_argument(
    "--where",
    type=str,
    default="local",
    help="local | cloud",
)
parser.add_argument(
    "--log",
    type=int,
    default=1,
    help="0|1",
)
parser.add_argument(
    "--delim",
    type=str,
    default=",",
)
args = parser.parse_args()

delim = " " if args.delim == "space" else args.delim

success = False
if args.task == "download":
    success = storage.download(
        object_name=args.object_name,
        filename=args.filename,
    )
elif args.task == "ls":
    success, list_of_files = storage.ls(
        object_name=args.object_name,
        where=args.where,
    )

    if args.log:
        logger.info(
            "{:,} file(s).".format(len(list_of_files)),
        )
        for index, filename in enumerate(list_of_files):
            logger.info(f"#{index+1: 4d} - {filename}")
    else:
        print(delim.join(list_of_files))

elif args.task == "upload":
    success = storage.upload(
        object_name=args.object_name,
        filename=args.filename,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
