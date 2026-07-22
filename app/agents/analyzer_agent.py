from app.prompts.analyzer_prompt import ANALYZER_PROMPT
from app.services.gemini_service import ask_gemini

def analyzer_agent(state):

    prompt = f"""
{ANALYZER_PROMPT}

Research Paper:

{state["paper_text"]}
"""

    state["analysis"] = ask_gemini(prompt)

    return state