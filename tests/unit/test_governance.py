import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2] / "src"))

from mesh_v5.governance.engine import GovernanceEngine
from mesh_v5.event_store.store import EventStore

def test_governance_flow():
    test_log = "test_gov_events.jsonl"
    store = EventStore(storage_path=test_log)
    engine = GovernanceEngine(event_store=store)

    # Proposta Legítima
    valid_prop = {
        "trace_id": "trc_gov_001",
        "agent": "OrchestratorAgent",
        "payload": "build_package"
    }
    res1 = engine.process_proposal(valid_prop)
    assert res1["approved"] is True
    assert res1["status"] == "CONSTITUTIONALLY_VALID"

    # Proposta Ilícita
    invalid_prop = {
        "trace_id": "trc_gov_002",
        "agent": "MaliciousAgent",
        "payload": "DROP DATABASE users"
    }
    res2 = engine.process_proposal(invalid_prop)
    assert res2["approved"] is False
    assert res2["status"] == "REJECTED_BY_CONSTITUTION"

    # Confirma gravação no Event Store
    events = store.read_all_events()
    assert len(events) == 2

    # Limpeza
    if os.path.exists(test_log):
        os.remove(test_log)

    print("\n✅ Fluxo de Governança e Proposal Gate testado com sucesso!")

if __name__ == "__main__":
    test_governance_flow()
