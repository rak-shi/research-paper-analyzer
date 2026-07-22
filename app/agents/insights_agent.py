from app.prompts.insights_prompt import INSIGHTS_PROMPT
from app.services.gemini_service import ask_gemini

def insights_agent(state):

    prompt = f"""
{INSIGHTS_PROMPT}

Research Paper:

{state["paper_text"]}
"""

    state["insights"] = ask_gemini(prompt)

    return state