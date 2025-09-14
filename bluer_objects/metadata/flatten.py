from typing import Any
import numpy as np


def flatten(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {k: flatten(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [flatten(x) for x in obj]
    elif isinstance(obj, tuple):
        return tuple(flatten(x) for x in obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif hasattr(obj, "__dict__"):
        return flatten(vars(obj))
    elif isinstance(obj, (int, float, str)):
        return obj
    else:
        try:
            return str(obj)
        except:
            return obj.__class__.__name__
