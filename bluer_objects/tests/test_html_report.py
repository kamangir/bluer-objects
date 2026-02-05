import pytest

from bluer_objects.html_report import HTMLReport
from bluer_objects import file
from bluer_objects import objects


@pytest.mark.parametrize(
    ["filename"],
    [
        [
            file.absolute(
                "../assets/template.html",
                file.path(__file__),
            ),
        ],
        [
            file.absolute(
                "../assets/non-existing-file.html",
                file.path(__file__),
            ),
        ],
        [
            "",
        ],
    ],
)
def test_html_report(
    filename: str,
):
    assert (
        HTMLReport(template=filename)
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
            object_name=objects.unique_object("test_html_report"),
            filename="report.html",
        )
    )
