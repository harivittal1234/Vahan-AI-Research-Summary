# ingestion_agent.py
# Agent to extract text from a PDF file using PyMuPDF

import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts and returns plain text from all pages of a given PDF.

    Args:
        pdf_path (str): Path to the PDF file

    Returns:
        str: Extracted plain text
    """
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        print(f"[IngestionAgent] Error reading {pdf_path}: {e}")
        return ""
