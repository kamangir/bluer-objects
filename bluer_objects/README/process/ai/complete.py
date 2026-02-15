from typing import List, Tuple, Dict, Any

from bluer_objects.README.process.ai import variables

from bluer_objects.README.process.ai.logger import logger


def complete(
    task: str,
    task_info: str,
    metadata: Dict[str, Any],
) -> Tuple[bool, List[str]]:
    if " " not in task_info:
        logger.error(f"prompt not found: {task_info}")
        return False, []

    query_id, query_prompt = task_info.split(" ", 1)

    variables.messages += [
        {
            "role": "user",
            "content": " ".join(variables.context + [query_prompt]),
        }
    ]

    if task == "complete":
        try:
            from bluer_agent.assistant.functions.chat import chat
        except Exception as e:
            logger.error(
                f'cannot import bluer-agent: {e}; try "pip install bluer-agent"'
            )
            return False, []

        success, reply = chat(
            messages=variables.messages,
            object_name=variables.object_name,
            filename=f"{query_id}.html",
        )
        if not success:
            return success, []

        metadata[query_id] = reply

    if task == "completed":
        reply = metadata.get(
            query_id,
            "⚠️ not available yet.",
        )
        assert isinstance(reply, str)

    variables.messages += [
        {
            "role": "assistant",
            "content": reply,
        },
    ]
    variables.context = []

    return True, (
        [
            f"> {query_prompt}",
            "",
            reply,
            "",
            f"🧠 query id: `{query_id}`",
        ]
    )
