import argparse
from tqdm import tqdm

from blueness import module
from blueness.argparse.generic import sys_exit
from bluer_options import string

from bluer_objects import file, NAME
from bluer_objects.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="replace | size",
)
parser.add_argument(
    "--filename",
    type=str,
)
parser.add_argument(
    "--this",
    type=str,
    help="<this-1+this-2+this-3>",
)
parser.add_argument(
    "--that",
    type=str,
    help="<that-1+that-2+that-3>",
)
parser.add_argument(
    "--pretty",
    type=int,
    default=1,
    help="0 | 1",
)
args = parser.parse_args()

success = False
if args.task == "replace":
    logger.info(f"{NAME}.{args.task}: {args.this} -> {args.that} in {args.filename}")

    success, content = file.load_text(args.filename)
    if success:
        for this, that in tqdm(zip(args.this.split("+"), args.that.split("+"))):
            content = [line.replace(this, that) for line in content]

        success = file.save_text(args.filename, content)
elif args.task == "size":
    size = file.size(args.filename)
    print(string.pretty_bytes(size) if args.pretty == 1 else size)
    success = True
else:
    success = None

sys_exit(logger, NAME, args.task, success)
