from typing import Union
import os

from bluer_options.env import load_config, load_env, get_env

load_env(__name__)
load_config(__name__)

HOME = get_env("HOME")

abcli_object_path = get_env("abcli_object_path")

ABCLI_PATH_STORAGE = get_env(
    "ABCLI_PATH_STORAGE",
    os.path.join(HOME, "storage"),
)

abcli_object_name = get_env("abcli_object_name")


ABCLI_OBJECT_ROOT = get_env(
    "ABCLI_OBJECT_ROOT",
    os.path.join(ABCLI_PATH_STORAGE, "abcli"),
)

abcli_path_git = get_env(
    "abcli_path_git",
    os.path.join(HOME, "git"),
)

ABCLI_PATH_STATIC = get_env("ABCLI_PATH_STATIC")

VANWATCH_TEST_OBJECT = get_env("VANWATCH_TEST_OBJECT")

# https://www.randomtextgenerator.com/
DUMMY_TEXT = "This is some dummy text. This is some dummy text. This is some dummy text. This is some dummy text. This is some dummy text. This is some dummy text. This is some dummy text. This is some dummy text. This is some dummy text. This is some dummy text."

DATABRICKS_WORKSPACE = get_env("DATABRICKS_WORKSPACE")

DATABRICKS_HOST = get_env("DATABRICKS_HOST")
DATABRICKS_TOKEN = get_env("DATABRICKS_TOKEN")

ABCLI_MLFLOW_EXPERIMENT_PREFIX = get_env("ABCLI_MLFLOW_EXPERIMENT_PREFIX")

ABCLI_S3_OBJECT_PREFIX = "to-be-removed"

BLUER_OBJECTS_STORAGE_INTERFACE = get_env("BLUER_OBJECTS_STORAGE_INTERFACE")

WEBDAV_HOSTNAME = get_env("WEBDAV_HOSTNAME")
WEBDAV_LOGIN = get_env("WEBDAV_LOGIN")
WEBDAV_PASSWORD = get_env("WEBDAV_PASSWORD")
