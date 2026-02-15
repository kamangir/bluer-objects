from typing import List, Tuple


from bluer_objects.metadata import get_from_object, post_to_object
from bluer_objects.README.process.ai import variables
from bluer_objects.README.process.ai.complete import complete
from bluer_objects.README.process.ai.logger import logger


def process_ai(
    content: List[str],
    enabled: bool = True,
    download: bool = False,
    upload: bool = False,
) -> Tuple[bool, List[str]]:
    logger.info("ai processing...")

    variables.ignore_started = False
    variables.context = []

    metadata = get_from_object(
        variables.object_name,
        "bluer-README-metadata",
        {},
        download=download,
    )
    assert isinstance(metadata, dict)

    output: List[str] = []
    for line in content:
        if line.startswith("ai:::"):
            line_ = line.split("ai:::", 1)[1]
            task, task_info = line_.split(" ", 1) if " " in line_ else (line_, "")

            if task == "ignore":
                variables.ignore_started = not variables.ignore_started
                continue

            if task in ["complete", "completed"]:
                success, output_ = complete(
                    task=task if enabled else "completed",
                    task_info=task_info,
                    metadata=metadata,
                )
                if not success:
                    return False, []

                output += output_

                continue

            if task == "object":
                variables.object_name = task_info
                logger.info(f"object_name={variables.object_name}")
                continue

            logger.error(f"unknown task: ai:::{task}.")
            return False, []
        else:
            output.append(line)

            if not variables.ignore_started:
                variables.context.append(line)

    return (
        post_to_object(
            variables.object_name,
            "bluer-README-metadata",
            metadata,
            upload=upload,
        ),
        output,
    )
