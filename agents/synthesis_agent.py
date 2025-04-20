
# Combines summaries of papers grouped by topic

from collections import defaultdict

def group_summaries_by_topic(summaries: list[str], topics: list[list[str]]) -> dict:
    """
    Groups summaries under their predicted topics.

    Args:
        summaries (list): List of summaries (one per paper)
        topics (list): List of predicted topic(s) per summary

    Returns:
        dict: {topic: [summary1, summary2, ...]}
    """
    topic_map = defaultdict(list)
    for summary, topic_list in zip(summaries, topics):
        for topic in topic_list:
            topic_map[topic].append(summary)
    return topic_map

def write_synthesized_outputs(topic_map: dict, output_dir: str = "results") -> None:
    """
    Writes topic-wise synthesized summaries to separate text files.

    Args:
        topic_map (dict): Output of group_summaries_by_topic
        output_dir (str): Directory to write results
    """
    import os
    os.makedirs(output_dir, exist_ok=True)

    for topic, summaries in topic_map.items():
        combined = "\n\n---\n\n".join(summaries)
        filename = os.path.join(output_dir, f"synthesis_{topic.replace(' ', '_')}.txt")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(combined)
