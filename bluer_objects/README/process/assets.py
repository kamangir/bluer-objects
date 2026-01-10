from bluer_objects import file


def process_assets(
    template_line: str,
    assets_repo: str,
) -> str:
    prefix = f"https://github.com/{assets_repo}/blob/main"

    if "assets:::" in template_line:
        template_line = " ".join(
            [
                (
                    (
                        "![image]({}/{}?raw=true)".format(
                            prefix,
                            token.split(":::")[1].strip(),
                        )
                        if any(
                            token.endswith(extension)
                            for extension in ["png", "jpg", "jpeg", "gif"]
                        )
                        else "[{}]({}/{})".format(
                            file.name_and_extension(token.split(":::")[1].strip()),
                            prefix,
                            token.split(":::")[1].strip(),
                        )
                    )
                    if token.startswith("assets:::")
                    else token
                )
                for token in template_line.split(" ")
            ]
        )

    return template_line
