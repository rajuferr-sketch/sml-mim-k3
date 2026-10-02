"""Consensus engine for parallel validation on complex stages."""
from typing import List, Dict, Any

class ConsensusEngine:
    def __init__(self, threshold: float = 0.80):
        self.threshold = threshold

    def evaluate_votes(self, responses: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not responses:
            return {"status": "failed", "consensus": False, "score": 0.0}
        
        valid_votes = [r for r in responses if r.get("approved", False)]
        score = len(valid_votes) / len(responses)
        passed = score >= self.threshold

        return {
            "status": "success" if passed else "consensus_failed",
            "consensus": passed,
            "score": score,
            "total_votes": len(responses),
            "approved_votes": len(valid_votes)
        }
