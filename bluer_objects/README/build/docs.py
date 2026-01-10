from bluer_objects import NAME
from bluer_objects.README.build import modules
from bluer_objects.README.alias import list_of_aliases
from bluer_objects.README.build import aliases

docs = (
    [
        {
            "path": ".",
        },
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
    + modules.docs
)
