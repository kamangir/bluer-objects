from typing import List

from bluer_options.terminal import show_usage, xtra


def help_replace(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        "--this this-1+this-2",
        "--that that-1+that-2",
    ]

    return show_usage(
        [
            "@file",
            "replace",
            "<filename>",
        ]
        + args,
        "<this> -> <that> in <filename>.",
        mono=mono,
    )


def help_size(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        "--pretty 0",
    ]

    return show_usage(
        [
            "@file",
            "size",
            "<filename>",
        ]
        + args,
        "size of <filename>",
        mono=mono,
    )


help_functions = {
    "replace": help_replace,
    "size": help_size,
}
