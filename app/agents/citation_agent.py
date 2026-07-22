from app.prompts.citation_prompt import CITATION_PROMPT
from app.services.gemini_service import ask_gemini

def citation_agent(state):

    prompt = f"""
{CITATION_PROMPT}

Research Paper:

{state["paper_text"]}
"""

    state["citations"] = ask_gemini(prompt)

    return state