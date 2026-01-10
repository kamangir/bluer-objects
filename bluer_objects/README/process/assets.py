from bluer_objects import file


def process_assets(
    template_line: str,
    assets_repo: str,
) -> str:
    if "assets:::" in template_line:
        template_line = " ".join(
            [
                (
                    (
                        "![image](https://github.com/{}/blob/main/{}?raw=true)".format(
                            assets_repo,
                            token.split(":::")[1].strip(),
                        )
                        if any(
                            token.endswith(extension)
                            for extension in ["png", "jpg", "jpeg", "gif"]
                        )
                        else "[{}](https://github.com/{}/blob/main/{})".format(
                            file.name_and_extension(token.split(":::")[1].strip()),
                            assets_repo,
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
