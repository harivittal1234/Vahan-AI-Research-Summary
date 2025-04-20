# summary_agent.py
# Agent to generate a summary using a transformer model

from transformers import pipeline

# Load the summarization model once during initialization
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text: str, max_chunk_tokens: int = 1024) -> str:
    """
    Summarizes the given text using a transformer-based model.

    Args:
        text (str): Full text of the research paper
        max_chunk_tokens (int): Max tokens per input chunk for the summarizer

    Returns:
        str: Generated summary
    """
    if not text or len(text.strip()) == 0:
        return "No content to summarize."

    # Break large input into chunks
    chunks = [text[i:i + max_chunk_tokens] for i in range(0, len(text), max_chunk_tokens)]
    summaries = []

    for chunk in chunks:
        try:
            result = summarizer(chunk, max_length=180, min_length=60, do_sample=False)
            summaries.append(result[0]["summary_text"])
        except Exception as e:
            summaries.append(f"[Error summarizing chunk] {e}")

    return "\n\n".join(summaries)
