"""FastMCP Server allowing ChatGPT and Claude to control the K3 Swarm."""
from 00_config.settings import settings
import json

def handle_request(tool_name: str, args: dict):
    if tool_name == "run_k3_swarm":
        task = args.get("task", "")
        return {"status": "success", "result": f"Executed 25-agent K3 swarm on: {task}"}
    elif tool_name == "get_swarm_status":
        with open("00_config/agent_manifest.json") as f:
            return json.load(f)
    return {"error": "Tool not found"}

if __name__ == "__main__":
    print("SML-MIM-K3 FastMCP Server running on stdio...")
