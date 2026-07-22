import os


def save_report(report):

    os.makedirs("outputs", exist_ok=True)

    with open("outputs/final_report.md", "w", encoding="utf-8") as f:
        f.write(report)