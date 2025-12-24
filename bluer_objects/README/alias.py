from typing import List
import importlib
from pathlib import Path
import os
import re

from bluer_objects import file
from bluer_objects.logger import logger


def list_of_aliases(
    module_name: str,
    log: bool = False,
) -> List[str]:
    module = importlib.import_module(module_name)
    module_path = str(Path(module.__file__).parent)

    alias_sh_path = os.path.join(
        module_path,
        ".abcli/alias.sh",
    )

    output: List[str] = []

    success, content = file.load_text(
        alias_sh_path,
        ignore_error=True,
        log=log,
    )
    if not success:
        return output

    def extract_alias_name(s: str) -> str:
        m = re.fullmatch(r"alias\s+@([^=]+)=.+", s.strip())
        return m.group(1) if m else ""

    return [
        alias_name
        for alias_name in [extract_alias_name(line) for line in content]
        if alias_name
    ]
