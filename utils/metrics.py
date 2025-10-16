from typing import List

def compute_relevance_scores(scores: List[float]) -> dict:
    if not scores:
        return {"mean": 0.0, "max": 0.0, "min": 0.0}
    return {
        "mean": sum(scores) / len(scores),
        "max": max(scores),
        "min": min(scores)
    }
