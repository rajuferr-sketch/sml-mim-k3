"""Terminal CLI Entrypoint for SML-MIM-K3 Swarm."""
import sys
import argparse
from 00_config.settings import settings
from 01_core.swarm_orchestrator import SwarmOrchestrator

def main():
    parser = argparse.ArgumentParser(description="SML-MIM-K3: 800B Emulated 25-Agent Swarm")
    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run", help="Run a task through the swarm")
    run_parser.add_argument("--task", required=True, help="Task or prompt description")
    run_parser.add_argument("--mode", default="swarm", choices=["swarm", "consensus", "sequential"])

    status_parser = subparsers.add_parser("status", help="Display swarm agent status")

    args = parser.parse_args()

    if args.command == "run":
        orchestrator = SwarmOrchestrator()
        result = orchestrator.run_pipeline(args.task, mode=args.mode)
        print("\n=== EXECUTION RESULT ===")
        print(result["result"])
    elif args.command == "status":
        with open("00_config/agent_manifest.json") as f:
            print(f.read())
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
