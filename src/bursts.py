"""
Burst detection and axis-node scoring.
Stub implementations; replace with your statistical models.
"""

from typing import List, Dict, Any


def detect_bursts(events: List[float], min_gap: float) -> List[int]:
    """Return indices where a new burst starts based on a minimum gap."""
    if not events:
        return []
    bursts = [0]
    for i in range(1, len(events)):
        if events[i] - events[i - 1] > min_gap:
            bursts.append(i)
    return bursts


def axis_scores(edges: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Compute simple influence scores for axis-node candidates.
    `edges` format: {"src": actor_id, "dst": actor_id, "weight": float}
    """
    scores: Dict[str, float] = {}
    for edge in edges:
        scores[edge["src"]] = scores.get(edge["src"], 0.0) + edge.get("weight", 1.0)
    return scores
