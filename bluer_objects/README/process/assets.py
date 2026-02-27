from bluer_objects import file


def process_token(
    token: str,
    assets_repo: str,
) -> str:
    if not token.startswith("assets:::"):
        return token

    suffix: str = token.split(":::", 1)[1].strip()
    volume: str = ""

    if ":::" in suffix:
        volume, suffix = suffix.split(":::", 1)

    prefix = f"https://github.com/{assets_repo}{volume}/blob/main"

    if any(
        token.endswith(extension)
        for extension in [
            "png",
            "jpg",
            "jpeg",
            "gif",
        ]
    ):
        return "![image]({}/{}?raw=true)".format(
            prefix,
            suffix,
        )

    return "[{}]({}/{})".format(
        file.name_and_extension(suffix),
        prefix,
        suffix,
    )


def process_assets(
    template_line: str,
    assets_repo: str,
) -> str:
    if "assets:::" in template_line:
        template_line = " ".join(
            [
                process_token(
                    token=token,
                    assets_repo=assets_repo,
                )
                for token in template_line.split(" ")
            ]
        )

    return template_line
