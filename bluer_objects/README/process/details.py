from typing import List


def process_details(template_line: str) -> List[str]:
    suffix = template_line.split(":::", 1)[1]
    if suffix:
        content_section = [
            "",
            "<details>",
            f"<summary>{suffix}</summary>",
            "",
        ]
    else:
        content_section = [
            "",
            "</details>",
            "",
        ]

    return content_section
