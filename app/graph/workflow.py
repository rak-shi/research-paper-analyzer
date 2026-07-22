from langgraph.graph import StateGraph, END

from app.agents.boss_agent import boss_agent
from app.agents.analyzer_agent import analyzer_agent
from app.agents.summary_agent import summary_agent
from app.agents.citation_agent import citation_agent
from app.agents.insights_agent import insights_agent
from app.agents.review_agent import review_agent
from app.agents.report_agent import report_agent


def review_decision(state):

    if state["review_score"] >= 7:
        return "approved"

    state["retries"] = state.get("retries", 0) + 1

    if state["retries"] >= 2:
        return "approved"

    return "retry"


workflow = StateGraph(dict)

workflow.add_node("boss", boss_agent)
workflow.add_node("analyzer", analyzer_agent)
workflow.add_node("summary", summary_agent)
workflow.add_node("citations", citation_agent)
workflow.add_node("insights", insights_agent)
workflow.add_node("review", review_agent)
workflow.add_node("report", report_agent)

workflow.set_entry_point("boss")

workflow.add_edge("boss", "analyzer")
workflow.add_edge("analyzer", "summary")
workflow.add_edge("summary", "citations")
workflow.add_edge("citations", "insights")
workflow.add_edge("insights", "review")

workflow.add_conditional_edges(
    "review",
    review_decision,
    {
        "approved": "report",
        "retry": "analyzer",
    },
)

workflow.add_edge("report", END)

graph = workflow.compile()