from bluer_objects import NAME
from bluer_objects.README.alias import list_of_aliases


def test_alias():
    output = list_of_aliases(NAME)

    assert isinstance(output, list)
    for thing in output:
        assert isinstance(thing, str)

    assert "host" in output
    assert "void" not in output
