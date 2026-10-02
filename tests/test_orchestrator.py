import pytest
from 01_core.swarm_orchestrator import SwarmOrchestrator

def test_orchestrator_initialization():
    orchestrator = SwarmOrchestrator()
    assert orchestrator.memory is not None
    assert orchestrator.consensus is not None

def test_pipeline_execution():
    orchestrator = SwarmOrchestrator()
    result = orchestrator.run_pipeline("Test task prompt", mode="swarm")
    assert result["status"] == "completed"
    assert "result" in result
    # Check that all 25 agents completed their stage
    for i in range(1, 26):
        assert result.get(f"agent_{i:02d}_completed") is True
