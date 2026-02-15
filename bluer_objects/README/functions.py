from typing import List, Dict, Union, Callable
import os
import pathlib

from blueness import module
from bluer_options.env import BLUER_AI_CLOUD_IS_ACCESSIBLE

from bluer_objects import NAME as MY_NAME
from bluer_objects import file
from bluer_objects import markdown
from bluer_objects.env import abcli_path_git
from bluer_objects.README.process.ai.process import process_ai
from bluer_objects.README.process.assets import process_assets
from bluer_objects.README.process.details import process_details
from bluer_objects.README.process.envs import process_envs
from bluer_objects.README.process.help import process_help
from bluer_objects.README.process.include import process_include
from bluer_objects.README.process.legacy import apply_legacy
from bluer_objects.README.process.mermaid import process_mermaid
from bluer_objects.README.process.metadata import process_metadata
from bluer_objects.README.process.national_internet import process_national_internet
from bluer_objects.README.process.objects import process_objects
from bluer_objects.README.process.title import process_title
from bluer_objects.README.process.signature import signature
from bluer_objects.README.process.variables import process_variable, variables
from bluer_objects.logger import logger

MY_NAME = module.name(__file__, MY_NAME)


def build(
    args,
    NAME: str,
    VERSION: str,
    REPO_NAME: str,
    items: List[str] = [],
    template_filename: str = "",
    filename: str = "",
    path: str = "",
    cols: int = 3,
    ICON: str = "",
    macros: Dict[str, str] = {},
    help_function: Union[Callable[[List[str]], str], None] = None,
    legacy_mode: bool = True,
    assets_repo: str = "kamangir/assets",
    download: bool = bool(BLUER_AI_CLOUD_IS_ACCESSIBLE),
    upload: bool = bool(BLUER_AI_CLOUD_IS_ACCESSIBLE),
    verbose: bool = False,
) -> bool:
    if path:
        if path.endswith(".md"):
            filename = path
            template_filename = file.add_suffix(path, "template")
        else:
            filename = os.path.join(path, "README.md")
            template_filename = os.path.join(path, "template.md")

    root: str = args.root if hasattr(args, "root") else "root"
    if root != "root":
        if not str(pathlib.Path(filename).resolve()).startswith(
            os.path.join(
                abcli_path_git,
                REPO_NAME,
                NAME,
                "docs",
                root,
            )
        ):
            logger.info(f"ignored {path}")
            return True

    ai_enabled: bool = args.ai == 1 if hasattr(args, "ai") else 0

    logger.info(
        "{}.build: {}:{}-{} | {} -{}{}{}{}> {}".format(
            MY_NAME,
            NAME,
            VERSION,
            REPO_NAME,
            template_filename,
            "+legacy-" if legacy_mode else "",
            "download-" if download else "",
            f"{root}-",
            "🪄 ai-" if ai_enabled else "",
            filename,
        )
    )

    if verbose:
        logger.info(f"filename: {filename}")
        logger.info(f"items: {items}")

    table_of_items = markdown.generate_table(items, cols=cols) if cols > 0 else items

    success, template = file.load_text(template_filename)
    if not success:
        return success

    if legacy_mode:
        template = apply_legacy(template)

    content: List[str] = []
    mermaid_started: bool = False
    for template_line in template:
        if template_line.startswith("ignore:::"):
            content.append(template_line)
            continue

        template_line = process_envs(template_line)

        for key, value in variables.items():
            template_line = template_line.replace(
                f"get:::{key}",
                value,
            )

        if "metadata:::" in template_line:
            content += process_metadata(
                template_line,
                download=download,
            )
            continue

        if template_line.startswith("set:::"):
            process_variable(template_line)
            continue

        template_line = process_assets(template_line, assets_repo)

        template_line = process_objects(template_line)

        if template_line.startswith("details:::"):
            content += process_details(template_line)
            continue

        if "items:::" in template_line:
            content += table_of_items
            continue

        if "include:::" in template_line:
            success, updated_content = process_include(
                template_line,
                file.path(template_filename),
            )
            if not success:
                return success

            content += updated_content
            continue

        if "signature:::" in template_line:
            content += signature(
                REPO_NAME,
                NAME,
                ICON,
                VERSION,
            )
            continue

        if template_line.startswith("title:::"):
            success, updated_content = process_title(
                template_line,
                filename,
            )
            if not success:
                return success

            content += updated_content
            continue

        if "help:::" in template_line:
            if help_function is None:
                logger.error("help_function not found.")
                return False

            success, updated_content = process_help(
                template_line,
                help_function,
            )
            if not success:
                return success

            content += updated_content
            continue

        content_section = [template_line]
        if template_line.startswith("```mermaid"):
            mermaid_started = True
            logger.info("🧜🏽‍♀️  detected ...")
        elif mermaid_started and template_line.startswith("```"):
            mermaid_started = False
        elif mermaid_started:
            if '"' in template_line and ":::folder" not in template_line:
                content_section = process_mermaid(template_line)
        else:
            for macro, macro_value in macros.items():
                if macro not in template_line:
                    continue

                if template_line.replace(macro, "").strip():
                    # this and that macro::: is going to be ...
                    content_section = [
                        template_line.replace(
                            macro,
                            (
                                " ".join(macro_value)
                                if isinstance(macro_value, list)
                                else macro_value
                            ),
                        )
                    ]
                else:
                    # macro:::
                    content_section = (
                        macro_value if isinstance(macro_value, list) else [macro_value]
                    )
                    break

        content += content_section

    content = process_national_internet(
        filename,
        content,
    )

    success, content = process_ai(
        content,
        enabled=ai_enabled,
        download=download,
        upload=upload,
    )
    if not success:
        return success

    content = [
        line.split("ignore:::", 1)[1].strip() if line.startswith("ignore:::") else line
        for line in content
    ]

    return file.save_text(filename, content)
