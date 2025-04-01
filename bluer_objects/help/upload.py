from typing import List

from bluer_options.terminal import show_usage, xtra


def help_upload(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "filename=<filename>"

    return show_usage(
        [
            "@upload",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "upload <object-name>.",
        mono=mono,
    )
