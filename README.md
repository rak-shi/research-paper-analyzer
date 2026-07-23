# 📄 AI-Powered Research Paper Analyzer

An end-to-end Multi-Agent AI system that automatically analyzes academic research papers and generates a comprehensive research brief using LangGraph and Google Gemini.

🌐 Live Demo: https://research-paper-analyzer1.streamlit.app/

---

## 🚀 Project Overview

Researchers and students often spend significant time reading research papers to understand their methodology, contributions, and findings.

This project automates that process using a Multi-Agent AI architecture where specialized agents collaborate to analyze research papers, generate executive summaries, extract citations, identify key insights, and produce a final research brief.

The system is built using **LangGraph**, **Google Gemini**, **Streamlit**, and **pdfplumber**, following a production-style agent orchestration workflow.

---

# Features

- 📄 Upload Research Paper (PDF)
- 🌐 Analyze Public PDF URLs
- 🤖 Multi-Agent AI Workflow
- 📝 Executive Summary Generation
- 🔍 Research Methodology Analysis
- 📚 Citation & Reference Extraction
- 💡 Key Insights Generation
- ✅ Review Agent with Quality Validation
- 📋 Final Research Brief Generation
- 🎨 Interactive Streamlit Web Interface

---

# Tech Stack

| Category | Technology |
|-----------|------------|
| Framework | LangGraph |
| LLM | Google Gemini |
| Frontend | Streamlit |
| PDF Parser | pdfplumber |
| Language | Python |
| Workflow | Multi-Agent System |
| Logging | Loguru |
| Environment | Python 3.12+ |

---

# Multi-Agent Architecture

"C:\Users\Rakshitha\Downloads\architecture_diagram.svg"

```

```

---

# Agent Responsibilities

## Boss Agent

- Controls workflow execution
- Delegates tasks
- Collects outputs
- Produces final report

---

## Paper Analyzer Agent

Extracts:

- Research Problem
- Methodology
- Experiments
- Results
- Contributions

---

## Summary Agent

Generates:

- 150–200 word executive summary
- Research overview
- Major findings

---

## Citation Agent

Extracts:

- References
- Citations
- Related work

---

## Insights Agent

Generates:

- Practical implications
- Future work
- Applications
- Important observations

---

## Review Agent

Evaluates each generated output based on:

- Accuracy
- Completeness
- Clarity

If the score is below the threshold, the agent regenerates the response before approval.

---

# Project Structure

```
research-paper-analyzer/

│
├── app/
│   ├── agents/
│   ├── graph/
│   ├── prompts/
│   ├── schemas/
│   ├── services/
│   └── utils/
│
├── frontend/
│   └── streamlit_app.py
│
├── outputs/
│
├── sample_papers/
│
├── architecture.png
├── requirements.txt
├── README.md
└── .env.example
```

---

# Installation

Clone repository

```bash
git clone https://github.com/rak-shi/research-paper-analyzer.git

cd research-paper-analyzer
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

# Run the Application

```bash
streamlit run frontend/streamlit_app.py
```

---

# Usage

### Option 1

Upload a Research Paper PDF.

### Option 2

Paste a publicly accessible PDF URL.

The system automatically:

- Extracts paper text
- Runs the multi-agent workflow
- Reviews generated outputs
- Produces a structured research brief

---

# Sample Input

Example Paper

```
sample_papers/
Attention Is All You Need.pdf
```

---

# Sample Output

The generated report contains:

- Paper Metadata
- Research Analysis
- Executive Summary
- Citations & References
- Key Insights

---

# Error Handling

The application includes:

- PDF parsing validation
- API exception handling
- Logging using Loguru
- Review-based quality validation
- Retry mechanism for failed agent outputs

---

# Future Improvements

- Support scanned PDFs using OCR
- Batch paper analysis
- Semantic search over multiple papers
- RAG-based literature review
- Research paper comparison
- Export report to PDF
- Citation visualization
- Progress tracking for agents

---

# Known Limitations

- Requires a valid Google Gemini API key.
- Performance depends on LLM response quality.
- Scanned/image-only PDFs are not fully supported.
- Public PDF URLs are supported; some publisher websites (IEEE, ScienceDirect, Springer, ACM, etc.) may require authentication.
- Large papers may take longer to process due to LLM latency.
- Processes one research paper at a time.

---

# Screenshots

## Home Page

(Add screenshot here)

## Generated Research Brief

(Add screenshot here)

---

# Deployment

Frontend

Streamlit Community Cloud

Live Application

https://research-paper-analyzer1.streamlit.app/

---

# GitHub Repository

https://github.com/rak-shi/research-paper-analyzer

---

# Author

**Rakshitha Valipireddy**

AI/ML Engineer

GitHub:
https://github.com/rak-shi

LinkedIn:
https://www.linkedin.com/in/rakshitha-valipireddy/

---

# Assignment Coverage

✔ LangGraph Workflow

✔ Multi-Agent Architecture

✔ Boss Agent

✔ Analyzer Agent

✔ Summary Agent

✔ Citation Agent

✔ Insights Agent

✔ Review Agent

✔ PDF Upload

✔ URL Support

✔ Gemini Integration

✔ Streamlit UI

✔ Deployment

✔ Documentation

✔ Sample Input & Output

✔ Architecture Diagram

✔ Error Handling

✔ Environment Variables

✔ GitHub Repository
