from bluer_objects import env


def process_objects(template_line: str) -> str:
    def suffix(token: str):
        words = token.split(":::")
        object_name = token.split(":::")[1].strip()

        if len(words) <= 2:
            return f"{object_name}.tar.gz"

        filename = words[2].strip()
        return f"{object_name}/{filename}"

    if "object:::" in template_line:
        template_line = " ".join(
            [
                (
                    "[{}](https://{}.{}/{})".format(
                        suffix(token),
                        env.S3_PUBLIC_STORAGE_BUCKET,
                        env.S3_STORAGE_ENDPOINT_URL.split("https://", 1)[1],
                        suffix(token),
                    )
                    if token.startswith("object:::")
                    else token
                )
                for token in template_line.split(" ")
            ]
        )

    return template_line
