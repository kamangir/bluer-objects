import pytest

from bluer_objects.html_report import HTMLReport
from bluer_objects import file
from bluer_objects import objects


@pytest.mark.parametrize(
    ["filename", "dummy", "expected_success"],
    [
        [
            file.absolute(
                "../assets/template.html",
                file.path(__file__),
            ),
            False,
            True,
        ],
        [
            file.absolute(
                "../assets/non-existing-file.html",
                file.path(__file__),
            ),
            False,
            False,
        ],
        [
            "",
            True,
            True,
        ],
    ],
)
def test_html_report(
    filename: str,
    dummy: bool,
    expected_success: bool,
):
    assert (
        HTMLReport(
            template=filename,
            dummy=dummy,
        )
        .replace(
            {
                "title:::": "some title",
                "signature:::": "some signature",
            }
        )
        .replace(
            {"content:::": ["some content"]},
            contains=True,
        )
        .save(
            filename=objects.path_of(
                object_name=objects.unique_object("test_html_report"),
                filename="report.html",
            )
        )
    ) == expected_success
