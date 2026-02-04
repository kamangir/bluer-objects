from typing import Dict, List
from functools import reduce

from bluer_objects import file


class HTMLReport:
    def __init__(
        self,
        template: str,
        log: bool = True,
    ):
        self.log = log

        self.valid, self.content = file.load_text(
            filename=template,
            log=self.log,
        )

    def replace(
        self,
        macros: Dict[str, List[str]],
        contains: bool = False,
    ) -> "HTMLReport":
        for this, that in macros.items():
            self.content = (
                reduce(
                    lambda x, y: x + y,
                    [that if this in line else [line] for line in self.content],
                    [],
                )
                if contains
                else [line.replace(this, that) for line in self.content]
            )

        return self

    def save(
        self,
        filename: str,
    ) -> bool:
        return file.save_text(
            filename,
            self.content,
            log=self.log,
        )
