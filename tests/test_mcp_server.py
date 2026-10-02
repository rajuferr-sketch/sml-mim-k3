import pytest
from 04_mcp.mcp_server import handle_request

def test_mcp_run_k3_swarm():
    res = handle_request("run_k3_swarm", {"task": "Design distributed cache"})
    assert res.get("status") == "success"
    assert "Design distributed cache" in res.get("result", "")

def test_mcp_get_swarm_status():
    res = handle_request("get_swarm_status", {})
    assert res.get("total_agents") == 25
    assert len(res.get("agents", [])) == 25

def test_mcp_invalid_tool():
    res = handle_request("unknown_tool", {})
    assert "error" in res
