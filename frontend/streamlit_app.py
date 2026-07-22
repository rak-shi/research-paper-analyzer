import os
import sys
import tempfile
from urllib.parse import urljoin

import requests
import streamlit as st
from bs4 import BeautifulSoup

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from app.graph.workflow import graph
from app.services.pdf_parser import extract_text_from_pdf

st.set_page_config(
    page_title="AI-Powered Research Paper Analyzer",
    page_icon="📄",
    layout="wide",
)

st.title("📄 AI-Powered Research Paper Analyzer")
st.markdown("### Upload a PDF or provide a Research Paper URL")

uploaded_file = st.file_uploader(
    "Upload Research Paper (PDF)",
    type=["pdf"]
)

paper_url = st.text_input(
    "OR Paste Research Paper URL"
)

paper_text = None


def download_pdf_from_url(url: str):
    headers = {"User-Agent": "Mozilla/5.0"}

    # arXiv abstract -> PDF
    if "arxiv.org/abs/" in url:
        url = url.replace("/abs/", "/pdf/") + ".pdf"

    response = requests.get(url, headers=headers, timeout=30)

    content_type = response.headers.get("Content-Type", "").lower()

    if "application/pdf" in content_type or url.lower().endswith(".pdf"):
        return response.content

    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find_all("a", href=True):
        href = link["href"]

        if ".pdf" in href.lower():
            pdf_url = urljoin(url, href)

            pdf_response = requests.get(
                pdf_url,
                headers=headers,
                timeout=30
            )

            if pdf_response.status_code == 200:
                return pdf_response.content

    return None


if uploaded_file:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    paper_text = extract_text_from_pdf(pdf_path)

elif paper_url:

    try:

        pdf_bytes = download_pdf_from_url(paper_url)

        if pdf_bytes is None:
            st.error(
                "Could not find a downloadable PDF. "
                "Please upload the PDF directly."
            )
            st.stop()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(pdf_bytes)
            pdf_path = tmp.name

        paper_text = extract_text_from_pdf(pdf_path)

    except Exception as e:
        st.error(f"Error: {e}")
        st.stop()

if paper_text:

    with st.spinner("Analyzing Research Paper..."):

        result = graph.invoke(
            {
                "paper_text": paper_text,
                "analysis": "",
                "summary": "",
                "citations": "",
                "insights": "",
                "review_score": 0,
                "review_reason": [],
                "final_report": "",
                "retries": 0,
            }
        )

    st.success("✅ Analysis Completed!")

    st.subheader("📝 Executive Summary")
    st.write(result["summary"])

    st.subheader("📚 Research Analysis")
    st.write(result["analysis"])

    st.subheader("💡 Key Insights")
    st.write(result["insights"])

    st.subheader("📖 Citations")
    st.write(result["citations"])

    st.subheader("✅ Review")
    st.metric("Review Score", f'{result["review_score"]}/10')

    if result["review_reason"]:
        st.markdown("### Review Feedback")
        for reason in result["review_reason"]:
            st.write(f"• {reason}")

    st.subheader("📄 Final Research Brief")
    st.markdown(result["final_report"])
