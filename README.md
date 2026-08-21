# Agent Mesh Core - MESH v5.0
### Constitutional Multi-Agent Orchestration | Zero-Trust Execution | Immutable Event Memory | A2A Governance

![Release: v5.0](https://img.shields.io/badge/release-v5.0-blue) ![tests](https://img.shields.io/badge/tests-4%20passed-brightgreen) ![Python](https://img.shields.io/badge/Python-3.9.6-blue) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

> **MESH v5.0 is a constitutional framework for governing, orchestrating and validating autonomous AI agents.** It operates under Harness Engineering paradigm - focusing on predictability, determinism, security and constitutional compliance instead of raw text generation.

**What is MESH v5.0?** An advanced core framework for orchestrating autonomous AI agents in distributed mesh architectures with Zero-Trust execution and immutable event memory.

## Quick Start - 2 Autonomous Agents Talking Alone (A2A)

```python
from mesh_v5 import MasterAgent, Agent

# Your dream: IAs conversando entre si sem sua interlocução
coordinator = MasterAgent(constitution="immutable_rules.yaml")
agent1 = Agent(role="proposer", task="analyze_data")
agent2 = Agent(role="executor", task="validate_and_execute")

# They talk alone via A2A protocol
coordinator.orchestrate([agent1, agent2], zero_trust=True)
print("Agents converged autonomously - 100% Zero-Trust PASSED")
