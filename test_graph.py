from app.graph.workflow import graph
from app.services.pdf_parser import extract_text
pdf_path = r"D:\research-paper-analyzer\sample_papers\Fine-Tuning-Large-Language-Models-for-Entity-Matching.pdf"

paper_text = extract_text(pdf_path)

state = {
    "paper_text": paper_text
}

result = graph.invoke(state)

print(result)
