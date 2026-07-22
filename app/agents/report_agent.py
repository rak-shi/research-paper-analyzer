from app.utils.save_report import save_report


def report_agent(state):

    report = f"""
# Research Paper Analysis Report

## Summary

{state["summary"]}

----------------------------------------------------

## Detailed Analysis

{state["analysis"]}

----------------------------------------------------

## Key Insights

{state["insights"]}

----------------------------------------------------

## Citations

{state["citations"]}

----------------------------------------------------

## Review Score

{state["review_score"]}/10
"""

    state["final_report"] = report

    save_report(report)

    return state