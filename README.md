# SML-MIM-K3: 800B Parameter Emulation Terminal Swarm

A high-performance terminal framework designed to emulate an 800-Billion parameter foundation intelligence (Kimi K3 architecture). It utilizes a 25-agent specialized swarm system operating in both consensus-based parallel mode and sequential pipeline handoffs for complex tasks.

## Key Features
- **Zero GUI Dependency**: Operates 100% natively from terminal CLI.
- **ChatGPT & Claude MCP Integration**: Exposes Model Context Protocol (MCP) server endpoints allowing external LLMs to orchestrate the swarm directly.
- **25 Specialized Agents**: Ordered and numbered modular components from Strategic Planning to Final Validation.
- **Consensus & Sequential Pipeline**: Agents perform distributed verification on complex stages before sequential handoff.
- **Automated Test Suite**: Full `pytest` coverage for the orchestrator, consensus engine, and MCP tools.

---

## Repository Structure

```text
.
├── .env.example                    # Template for environment variables and API keys
├── .gitignore                      # Git ignore patterns
├── README.md                       # Main architecture and documentation
├── SETUP_GUIDE.md                  # Comprehensive step-by-step setup guide
├── requirements.txt                # Python package dependencies
├── cli.py                          # Primary terminal entrypoint
├── 00_config/
│   ├── settings.py                 # Swarm runtime configuration
│   └── agent_manifest.json         # Complete registry of all 25 agents
├── 01_core/
│   ├── swarm_orchestrator.py       # Main pipeline controller
│   ├── consensus_engine.py         # Parallel voting & consensus engine
│   └── context_memory.py           # Shared context and state memory
├── 02_agents/                      # 25 Specialized numbered agents
│   ├── 01_master_planner.py
│   ├── ...
│   └── 25_final_validator.py
├── 03_actions/                     # Pipeline execution steps
│   ├── 01_ingest_prompt.py
│   ├── ...
│   └── 05_aggregate_output.py
├── 04_mcp/                         # MCP Server for ChatGPT and Claude
│   ├── mcp_server.py
│   └── tools.json
└── tests/                          # Automated Pytest suite
    ├── test_orchestrator.py
    ├── test_consensus_engine.py
    └── test_mcp_server.py
```

---

## Environment Variables (.env)

Copy `.env.example` to `.env` to configure your runtime parameters:

| Variable | Description | Default |
|:---|:---|:---|
| `OPENAI_API_KEY` | Optional OpenAI key for external model delegation | `None` |
| `ANTHROPIC_API_KEY` | Optional Anthropic key for external model delegation | `None` |
| `MOONSHOT_API_KEY` | Moonshot / Kimi API key | `None` |
| `SWARM_MODEL_NAME` | Active emulation architecture identifier | `sml-mim-k3-800b` |
| `SWARM_TOTAL_AGENTS` | Total number of agents in the pipeline | `25` |
| `SWARM_CONSENSUS_THRESHOLD` | Required consensus percentage for complex stages | `0.80` |
| `SWARM_TIMEOUT_SECONDS` | Pipeline timeout per agent stage | `120` |
| `SWARM_SHARED_MEMORY_LIMIT_MB` | In-memory context cache ceiling | `2048` |
| `SWARM_OUTPUT_DIR` | Output artifact directory | `./runs` |
| `MCP_SERVER_HOST` | Host IP address for local MCP service | `127.0.0.1` |
| `MCP_SERVER_PORT` | Port for MCP network server | `8000` |

---

## Quick Start (Terminal)

```bash
# 1. Clone repository
git clone https://github.com/rajuferr-sketch/sml-mim-k3.git
cd sml-mim-k3

# 2. Create virtual environment and install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. Configure credentials
cp .env.example .env

# 4. Execute prompt via Swarm CLI
python cli.py run --task "Architect a distributed high-throughput message broker" --mode swarm
```

---

## Running Automated Tests

Run the full automated test suite using `pytest`:

```bash
pytest -v
```

---

## MCP Integration (ChatGPT & Claude)

Run the local MCP server:
```bash
python 04_mcp/mcp_server.py
```

See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed instructions on configuring Claude Desktop and ChatGPT.
