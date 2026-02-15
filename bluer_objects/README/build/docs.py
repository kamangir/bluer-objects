from bluer_objects import NAME
from bluer_objects.README.alias import list_of_aliases
from bluer_objects.README.build import aliases, bluer_README, mlflow

docs = (
    [
        {
            "path": "../..",
            "macros": {
                "aliases:::": list_of_aliases(NAME),
            },
        },
        {
            "path": "../docs",
        },
    ]
    + aliases.docs
    + bluer_README.docs
    + mlflow.docs
)
