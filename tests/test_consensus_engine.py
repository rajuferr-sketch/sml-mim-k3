import pytest
from 01_core.consensus_engine import ConsensusEngine

def test_consensus_success():
    engine = ConsensusEngine(threshold=0.80)
    # 25 agents: 21 approve (84% > 80%)
    votes = [{"agent_id": f"{i:02d}", "approved": True} for i in range(1, 22)]
    votes += [{"agent_id": f"{i:02d}", "approved": False} for i in range(22, 26)]
    
    result = engine.evaluate_votes(votes)
    assert result["consensus"] is True
    assert result["status"] == "success"
    assert result["approved_votes"] == 21
    assert result["score"] >= 0.80

def test_consensus_failure():
    engine = ConsensusEngine(threshold=0.80)
    # Only 10 approve (40% < 80%)
    votes = [{"agent_id": f"{i:02d}", "approved": True} for i in range(1, 11)]
    votes += [{"agent_id": f"{i:02d}", "approved": False} for i in range(11, 26)]
    
    result = engine.evaluate_votes(votes)
    assert result["consensus"] is False
    assert result["status"] == "consensus_failed"
    assert result["score"] < 0.80

def test_consensus_empty_votes():
    engine = ConsensusEngine(threshold=0.80)
    result = engine.evaluate_votes([])
    assert result["consensus"] is False
