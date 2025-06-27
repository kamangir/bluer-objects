import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List, Any
import os

from bluer_objects import file


def log_image_grid(
    items: Dict[str, Dict[str, Any]],
    filename: str,
    rows: int = 5,
    cols: int = 4,
    log: bool = True,
) -> bool:
    while len(items) < rows * cols:
        items += [{"pass": True}]

    _, axes = plt.subplots(
        rows,
        cols,
        figsize=(
            4 * cols,
            4 * rows,
        ),
    )
    axes = axes.flatten()

    for i, item in enumerate(items):
        if item.get("pass", False):
            axes[i].axis("off")
            continue

        filename = item.get("filename", "")
        if filename:
            success, item["image"] = file.load_image(
                filename,
                log=log,
            )
            if not success:
                return False

        ax = axes[i]
        image = item["image"]
        ax.imshow(
            image,
            cmap="gray" if image.ndim == 2 else None,
        )
        ax.set_title(
            item.get("title", f"#{i}"),
            fontsize=10,
        )
        ax.axis("off")

    plt.tight_layout()

    return file.save_fig(
        filename,
        log=log,
    )
