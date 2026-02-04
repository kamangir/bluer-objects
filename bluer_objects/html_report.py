from typing import Dict, List
from functools import reduce

from bluer_objects import file


class HTMLReport:
    def __init__(
        self,
        template: str = "",
        log: bool = True,
        dummy: bool = False,
    ):
        self.log = log
        self.dummy: bool = template == ""

        self.valid: bool = True
        self.content: List[str] = []

        if self.dummy:
            return

        self.valid, self.content = file.load_text(
            filename=template,
            log=self.log,
        )

    def replace(
        self,
        macros: Dict[str, List[str]],
        contains: bool = False,
    ) -> "HTMLReport":
        if self.dummy or not self.valid:
            return self

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
        if self.dummy:
            return True

        if not self.valid:
            return False

        return file.save_text(
            filename,
            self.content,
            log=self.log,
        )
