# metadata_agent.py
# Extracts and saves metadata for a processed research paper

import json
import os
from datetime import datetime

def save_metadata(summary: str, topic: list[str], pdf_path: str, output_path: str = "results/metadata.json") -> None:
    """
    Saves metadata about the summary and source paper.

    Args:
        summary (str): The summary text.
        topic (list): List of predicted topics.
        pdf_path (str): Path to original PDF.
        output_path (str): JSON file to save the metadata.
    """
    metadata = {
        "file_name": os.path.basename(pdf_path),
        "detected_topic": topic,
        "summary_length": len(summary.split()),
        "created_at": datetime.now().isoformat()
    }

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=4)
        print(f"Metadata saved to {output_path}")
    except Exception as e:
        print(f"MetadataAgent: Error saving metadata: {e}")
