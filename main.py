# main.py

import os
from agents.ingestion_agent import extract_text_from_pdf
from agents.summary_agent import generate_summary
from agents.classification_agent import classify_topic
from agents.audio_agent import generate_audio
from agents.metadata_agent import save_metadata
from agents.synthesis_agent import group_summaries_by_topic, write_synthesized_outputs

topic_list = [
    "Natural Language Processing",
    "Computer Vision",
    "Healthcare AI",
    "Quantum Computing",
    "Cybersecurity",
    "Bioinformatics"
]

def main():
    samples_dir = "samples"
    results_dir = "results"
    os.makedirs(results_dir, exist_ok=True)

    all_summaries = []
    all_topics = []

    for file in os.listdir(samples_dir):
        if not file.lower().endswith(".pdf"):
            continue

        pdf_path = os.path.join(samples_dir, file)
        print(f"\nProcessing {file}...")

        text = extract_text_from_pdf(pdf_path)
        if not text:
            print(f"Failed to extract text from {file}")
            continue

        summary = generate_summary(text)
        summary_file = os.path.join(results_dir, f"{file}_summary.txt")
        with open(summary_file, "w", encoding="utf-8") as f:
            f.write(summary)

        predicted_topic = classify_topic(summary, topic_list)
        print(f"Predicted Topic for {file}: {predicted_topic}")

        audio_path = os.path.join(results_dir, f"{file}_summary.mp3")
        generate_audio(summary, output_path=audio_path)

        metadata_path = os.path.join(results_dir, f"{file}_metadata.json")
        save_metadata(summary, predicted_topic, pdf_path, output_path=metadata_path)

        all_summaries.append(summary)
        all_topics.append(predicted_topic)

    # Group summaries by topic and write synthesis files
    topic_map = group_summaries_by_topic(all_summaries, all_topics)
    write_synthesized_outputs(topic_map, output_dir=results_dir)

if __name__ == "__main__":
    main()
