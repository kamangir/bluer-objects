from bluer_ai.help.generic import help_functions as generic_help_functions

from bluer_objects import ALIAS
from bluer_objects.help.clone import help_clone
from bluer_objects.help.download import help_download
from bluer_objects.help.metadata import help_functions as help_metadata
from bluer_objects.help.mlflow import help_functions as help_mlflow
from bluer_objects.help.upload import help_upload

help_functions = generic_help_functions(plugin_name=ALIAS)

help_functions.update(
    {
        "clone": help_clone,
        "download": help_download,
        "metadata": help_metadata,
        "mlflow": help_mlflow,
        "upload": help_upload,
    }
)
