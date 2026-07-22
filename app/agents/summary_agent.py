from app.prompts.summary_prompt import SUMMARY_PROMPT
from app.services.gemini_service import ask_gemini

def summary_agent(state):

    prompt = f"""
{SUMMARY_PROMPT}

Research Paper:

{state["paper_text"]}
"""

    state["summary"] = ask_gemini(prompt)

    return state