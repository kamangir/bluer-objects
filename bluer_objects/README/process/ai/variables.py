from typing import List, Dict

from bluer_options import string

context: List[str] = []

ignore_started: bool = False

messages: List[Dict] = []

object_name: str = string.timestamp()
