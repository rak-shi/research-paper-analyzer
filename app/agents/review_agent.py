
import json
import re

from app.prompts.review_prompt import REVIEW_PROMPT
from app.services.gemini_service import ask_gemini


def has_any(text, keywords):
    text = text.lower()
    return any(k.lower() in text for k in keywords)


def review_agent(state):
    paper = state["paper_text"]

    prompt = f'''
{REVIEW_PROMPT}

=========================
ORIGINAL PAPER
=========================

{paper}

=========================
GENERATED ANALYSIS
=========================

{state["analysis"]}

=========================
GENERATED SUMMARY
=========================

{state["summary"]}

=========================
GENERATED INSIGHTS
=========================

{state["insights"]}

=========================
GENERATED CITATIONS
=========================

{state["citations"]}

Review ONLY the generated output.

Return ONLY JSON.

{{
    "accuracy":8,
    "completeness":8,
    "clarity":8,
    "issues":[]
}}
'''

    response = ask_gemini(prompt)

    print("\n========== REVIEW RESPONSE ==========")
    print(response)
    print("=====================================\n")

    try:
        clean = response.strip()
        clean = re.sub(r"^```json\s*", "", clean, flags=re.IGNORECASE)
        clean = re.sub(r"^```", "", clean)
        clean = re.sub(r"```$", "", clean)

        review = json.loads(clean)

        accuracy = int(review.get("accuracy", 5))
        completeness = int(review.get("completeness", 5))
        clarity = int(review.get("clarity", 5))
        issues = review.get("issues", [])

        llm_score = round((accuracy + completeness + clarity) / 3)

        checks = [
            ("Abstract", ["abstract"]),
            ("Introduction", ["introduction"]),
            ("Methodology", ["methodology", "methods"]),
            ("Experiments", ["experiment", "experimental"]),
            ("Results", ["results"]),
            ("Conclusion", ["conclusion"]),
            ("References", ["references", "bibliography"]),
        ]

        present = 0
        missing = []

        for name, keys in checks:
            if has_any(paper, keys):
                present += 1
            else:
                missing.append(name)

        paper_score = round((present / len(checks)) * 10)

        final_score = round((0.6 * llm_score) + (0.4 * paper_score))

        if present <= 1:
            final_score = min(final_score, 4)
        elif present <= 2:
            final_score = min(final_score, 5)
        elif present <= 3:
            final_score = min(final_score, 6)

        if len(state["analysis"].split()) < 250:
            final_score -= 1
            issues.append("Research analysis could be more detailed.")

        if len(state["summary"].split()) < 120:
            final_score -= 1
            issues.append("Executive summary is too short.")

        if missing:
            issues.append("Missing paper sections: " + ", ".join(missing))

        final_score = max(1, min(final_score, 10))

        state["review_score"] = final_score
        state["review_reason"] = issues

        print("========== REVIEW RESULT ==========")
        print(f"Accuracy           : {accuracy}/10")
        print(f"Completeness       : {completeness}/10")
        print(f"Clarity            : {clarity}/10")
        print(f"LLM Score          : {llm_score}/10")
        print(f"Paper Score        : {paper_score}/10")
        print(f"Final Review Score : {final_score}/10")
        print(f"Present Sections   : {present}/{len(checks)}")
        print(f"Missing Sections   : {missing}")

        if issues:
            print("\nIssues Found:")
            for issue in issues:
                print("-", issue)
        else:
            print("\nNo issues found.")

        print("===================================\n")

    except Exception as e:
        print("JSON Parsing Error:", e)
        print(response)
        state["review_score"] = 5
        state["review_reason"] = ["Unable to parse Gemini review."]

    return state
