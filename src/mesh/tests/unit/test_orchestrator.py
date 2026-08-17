import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2] / "src"))

from mesh_v5.orchestrator.mesh import MeshOrchestrator
from mesh_v5.event_store.store import EventStore

def test_orchestrator():
    test_log = "test_orch_events.jsonl"
    store = EventStore(storage_path=test_log)
    orchestrator = MeshOrchestrator()
    orchestrator.governance.event_store = store

    # 1. Despacho Válido
    valid_task = {
        "trace_id": "trc_orch_001",
        "agent": "MasterAgent",
        "payload": "run_security_scan"
    }
    res_valid = orchestrator.dispatch(valid_task)
    assert res_valid["executed"] is True
    print("Orchestrator Test 1 (Executado):", res_valid["result"])

    # 2. Despacho Bloqueado
    blocked_task = {
        "trace_id": "trc_orch_002",
        "agent": "SubAgent",
        "payload": "format /dev/sda"
    }
    res_blocked = orchestrator.dispatch(blocked_task)
    assert res_blocked["executed"] is False
    print("Orchestrator Test 2 (Bloqueado):", res_blocked["reason"])

    # Limpeza
    if os.path.exists(test_log):
        os.remove(test_log)

    print("\n✅ Orquestrador Central testado e aprovado com sucesso!")

if __name__ == "__main__":
    test_orchestrator()
