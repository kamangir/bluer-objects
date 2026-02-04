from bluer_objects.html_report import HTMLReport
from bluer_objects import file
from bluer_objects import objects


def test_html_report():
    assert (
        HTMLReport(
            file.absolute(
                "../assets/template.html",
                file.path(__file__),
            ),
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
    )
