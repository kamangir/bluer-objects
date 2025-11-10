from typing import List

from bluer_options.terminal import show_usage, xtra


def help_convert(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("install,", mono=mono),
            "combine",
            xtra(",~compress", mono=mono),
        ]
    )

    usage_1 = show_usage(
        [
            "@pdf",
            "convert",
            f"[{options}]",
            "<module-name>",
            "<.,this,this/that.md,this/that.jpg,this/that.pdf>",
            "[-|<object-name>]",
        ],
        "md -> pdf.",
        mono=mono,
    )

    # ---

    options = f"filename=<filename.yaml>,{options},yaml"

    usage_2 = show_usage(
        [
            "@pdf",
            "convert",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "md -> pdf.",
        mono=mono,
    )

    return "\n".join(
        [
            usage_1,
            usage_2,
        ]
    )


help_functions = {
    "convert": help_convert,
}
