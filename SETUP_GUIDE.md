# Step-by-Step Setup Guide for SML-MIM-K3

This guide walks you through installing dependencies, configuring environment credentials, and executing your first multi-agent task across all 25 agents.

---

## Prerequisites

- **Python**: 3.10 or higher (`python3 --version`)
- **Git**: Installed and configured on your system
- **API Keys**: (Optional) OpenAI, Anthropic, or Moonshot/Kimi keys for real model inference passthrough.

---

## 1. Clone & Set Up the Environment

Open your terminal and clone the repository:

```bash
git clone https://github.com/rajuferr-sketch/sml-mim-k3.git
cd sml-mim-k3
```

Create and activate a virtual environment:

```bash
# On Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

# On Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 2. Configure Environment Variables

Copy the example environment file:

```bash
cp .env.example .env
```

Open `.env` in your preferred editor (e.g. `nano .env` or `code .env`) and specify your keys:

```bash
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
MOONSHOT_API_KEY=sk-...
```

*Note: The emulation framework works in standalone simulation mode even without external API keys.*

---

## 3. Run Your First 25-Agent Task

### Command-Line Interface (CLI)

1. **Verify agent manifest status:**
   ```bash
   python cli.py status
   ```

2. **Execute a task through all 25 sequential agents:**
   ```bash
   python cli.py run --task "Build a distributed event bus with fault-tolerant consensus" --mode swarm
   ```

3. **Execute a task in parallel consensus mode:**
   ```bash
   python cli.py run --task "Audit schema migration for zero-downtime distributed PostgreSQL" --mode consensus
   ```

---

## 4. Run the Automated Tests

Verify that the orchestrator, consensus engine, and MCP tools function correctly:

```bash
pytest
```

All test suites under `tests/` should pass with green status.

---

## 5. Connect to ChatGPT or Claude via MCP

Start the Model Context Protocol server locally:

```bash
python 04_mcp/mcp_server.py
```

### Claude Desktop Configuration
Add the server entry to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%/Claude/claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "sml-mim-k3": {
      "command": "python",
      "args": ["/absolute/path/to/sml-mim-k3/04_mcp/mcp_server.py"]
    }
  }
}
```
