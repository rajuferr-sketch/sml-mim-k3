"""Global configuration settings for SML-MIM-K3 swarm."""
from pydantic import BaseModel
import os

class SwarmSettings(BaseModel):
    model_name: str = "sml-mim-k3-800b"
    total_agents: int = 25
    consensus_threshold: float = 0.80
    timeout_seconds: int = 120
    shared_memory_limit_mb: int = 2048
    output_dir: str = "./runs"

settings = SwarmSettings()
