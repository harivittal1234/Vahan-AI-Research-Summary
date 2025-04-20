# classification_agent.py
# Classifies text into one of several topics using SBERT + cosine similarity

from sentence_transformers import SentenceTransformer, util

# Load once for efficiency
model = SentenceTransformer('all-MiniLM-L6-v2')

def classify_topic(text: str, topic_list: list[str], top_k: int = 1) -> list[str]:
    """
    Classifies the input text into one or more topics based on similarity.

    Args:
        text (str): The input text (summary or full paper text)
        topic_list (list): List of topic strings
        top_k (int): Number of top matches to return

    Returns:
        list[str]: List of matched topics
    """
    if not text or not topic_list:
        return []

    text_embedding = model.encode(text, convert_to_tensor=True)
    topic_embeddings = model.encode(topic_list, convert_to_tensor=True)

    cosine_scores = util.pytorch_cos_sim(text_embedding, topic_embeddings)[0]
    top_results = cosine_scores.topk(top_k)

    return [topic_list[idx] for idx in top_results.indices]
