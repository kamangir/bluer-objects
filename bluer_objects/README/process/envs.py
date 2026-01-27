from bluer_options.env import get_env

from bluer_objects.logger import logger


def process_envs(template_line: str) -> str:
    while "env:::" in template_line:
        env_name = template_line.split("env:::", 1)[1]
        if " " in env_name:
            env_name = env_name.split(" ", 1)[0]
        else:
            if ":::" in env_name:
                env_name = env_name.split(":::", 1)[0]

        env_value = get_env(env_name)

        template_line = template_line.replace(
            f"env:::{env_name}",
            env_value,
        )
        logger.info(f"{env_name} -> {env_value}")

    return template_line
