"""
generate_report.py

Creates PDF report for
Fuzzy Shower Controller.
"""

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_report():

    file_path = "results/report.pdf"


    document = SimpleDocTemplate(
        file_path
    )


    styles = getSampleStyleSheet()


    content = []


    content.append(

        Paragraph(

            "Fuzzy Shower Temperature Controller Report",

            styles["Title"]

        )

    )


    content.append(
        Spacer(
            1,
            20
        )
    )


    sections = [

        "Project combines Fuzzy Logic and Machine Learning.",

        "Fuzzy controller adjusts hot and cold valves.",

        "Machine learning predicts valve behaviour.",

        "Simulation models real shower temperature control."

    ]


    for text in sections:

        content.append(

            Paragraph(
                text,
                styles["BodyText"]
            )

        )

        content.append(
            Spacer(
                1,
                10
            )
        )


    document.build(
        content
    )


    print(
        "PDF Report Generated"
    )


if __name__ == "__main__":

    generate_report()