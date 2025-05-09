# Vahan-AI-Research-Summary

# Research Paper Summarizer – Multi-Agent System

A multi-agent pipeline that ingests research papers (PDF), summarizes them, classifies by topic, and generates audio narration for each paper — all from the command line.

---

## Features
- Accepts research papers as PDF
- Extracts and summarizes full text
- Classifies into predefined topics
- Generates `.mp3` audio files of summaries
- Saves citation metadata in JSON
- Groups multiple summaries into topic-based synthesis

---

## Working
Uses Sentence transformers to extract and process the text data

---

## Folder Structure
```
research_engine/
├── agents/
│   ├── ingestion_agent.py
│   ├── summary_agent.py
│   ├── classification_agent.py
│   ├── audio_agent.py
│   ├── metadata_agent.py
│   └── synthesis_agent.py
├── samples/
│   └── sample_paper.pdf
├── results/
├── main.py
├── requirements.txt
└── Dockerfile
```
---

## Technologies Used
- PyMuPDF (fitz) – PDF Text Extraction
- HuggingFace Transformers – Text Summarization (facebook/bart-large-cnn)
- Sentence-BERT – Topic Classification
- gTTS – Audio Generation
- JSON – Metadata Storage


---

## Setup Instructions

### Option 1: Local Setup Using Python

```bash
pip install -r requirements.txt
python main.py
```

### Option 2: Use Docker

- Build the image
```bash 
docker build -t summarizer .
```
- Run the Container
```bash
docker run summarizer
```
