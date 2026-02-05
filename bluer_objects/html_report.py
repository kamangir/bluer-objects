from typing import Dict, List
from functools import reduce

from bluer_options.timing import ElapsedTimer

from bluer_objects import file
from bluer_objects import objects
from bluer_objects.logger import logger


class HTMLReport:
    def __init__(
        self,
        template: str = "",
        log: bool = True,
    ):
        self.elapsed_timer = ElapsedTimer()

        self.log = log
        self.dummy: bool = template == ""

        self.valid: bool = True
        self.content: List[str] = []

        if self.dummy:
            return

        success, self.content = file.load_text(
            filename=template,
            log=self.log,
        )
        if not success:
            logger.warning(f"{self.__class__.__name__} is dummy now.")

    def replace(
        self,
        macros: Dict[str, List[str]],
        contains: bool = False,
    ) -> "HTMLReport":
        if self.dummy:
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
        object_name: str,
        filename: str = "report.html",
    ) -> bool:
        if self.dummy:
            return True

        self.replace(
            {
                "elapsed_time:::": self.elapsed_timer.as_str(),
                "object_signature:::": " | ".join(
                    objects.signature(
                        object_name=object_name,
                        info=filename,
                    )
                ),
            }
        )

        return file.save_text(
            objects.path_of(
                object_name=object_name,
                filename=filename,
            ),
            self.content,
            log=self.log,
        )
