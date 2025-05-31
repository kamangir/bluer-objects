from typing import List

from bluer_options.terminal import show_usage, xtra


def help_lock(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun,lock=<lock-name>", mono=mono)

    args = [
        "[--timeout <10>]",
    ]

    return show_usage(
        [
            "@lock",
            "lock",
            f"[{options}]",
            "[.|<object-name>]",
        ]
        + args,
        "lock <object-name>.",
        mono=mono,
    )


def help_unlock(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun,lock=<lock-name>", mono=mono)

    return show_usage(
        [
            "@lock",
            "unlock",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "unlock <object-name>.",
        mono=mono,
    )


help_functions = {
    "lock": help_lock,
    "unlock": help_unlock,
}
