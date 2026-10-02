# SML-MIM-K3: 800B Parameter Emulation Terminal Swarm

A high-performance terminal framework designed to emulate an 800-Billion parameter foundation intelligence (Kimi K3 architecture). It utilizes a 25-agent specialized swarm system operating in both consensus-based parallel mode and sequential pipeline handoffs for complex tasks.

## Key Features
- **Zero GUI Dependency**: Operates 100% natively from terminal CLI.
- **ChatGPT & Claude MCP Integration**: Exposes Model Context Protocol (MCP) server endpoints allowing external LLMs to orchestrate the swarm directly.
- **25 Specialized Agents**: Ordered and numbered modular components from Strategic Planning to Final Validation.
- **Consensus & Sequential Pipeline**: Agents perform identical distributed verification on complex stages before sequential handoff.

## Architecture & File Structure

```text
.
├── .gitignore
├── README.md
├── requirements.txt
├── cli.py                          # Primary terminal entrypoint
├── 00_config/
│   ├── settings.py                 # Swarm runtime configuration
│   └── agent_manifest.json         # Complete registry of all 25 agents
├── 01_core/
│   ├── swarm_orchestrator.py       # Main pipeline controller
│   ├── consensus_engine.py         # Parallel voting & consensus engine
│   └── context_memory.py           # Shared context and state memory
├── 02_agents/
│   ├── 01_master_planner.py
│   ├── 02_prompt_architect.py
│   ├── 03_context_retriever.py
│   ├── 04_code_synthesizer.py
│   ├── 05_code_debugger.py
│   ├── 06_code_reviewer.py
│   ├── 07_security_auditor.py
│   ├── 08_test_engineer.py
│   ├── 09_refactoring_specialist.py
│   ├── 10_system_architect.py
│   ├── 11_database_engineer.py
│   ├── 12_api_integrator.py
│   ├── 13_performance_optimizer.py
│   ├── 14_devops_automator.py
│   ├── 15_documentation_writer.py
│   ├── 16_research_analyst.py
│   ├── 17_data_scientist.py
│   ├── 18_nlp_specialist.py
│   ├── 19_vision_processor.py
│   ├── 20_logic_verifier.py
│   ├── 21_edge_case_hunter.py
│   ├── 22_dependency_manager.py
│   ├── 23_benchmarking_expert.py
│   ├── 24_synthesis_director.py
│   └── 25_final_validator.py
├── 03_actions/
│   ├── 01_ingest_prompt.py
│   ├── 02_decompose_task.py
│   ├── 03_parallel_swarm_vote.py
│   ├── 04_sequential_handoff.py
│   └── 05_aggregate_output.py
└── 04_mcp/
    ├── mcp_server.py               # FastMCP server for Claude & ChatGPT
    └── tools.json                  # MCP tools specification
```

## Quick Start (Terminal)

```bash
# 1. Clone repository
git clone https://github.com/rajuferr-sketch/sml-mim-k3.git
cd sml-mim-k3

# 2. Install dependencies
pip install -r requirements.txt

# 3. Execute prompt via Swarm CLI
python cli.py run --task "Architect a distributed high-throughput message broker" --mode swarm
```

## MCP Integration (ChatGPT & Claude)

Run the local MCP server:
```bash
python 04_mcp/mcp_server.py
```
Attach the server via Claude Desktop or ChatGPT developer connector using the JSON schema located in `04_mcp/tools.json`.
