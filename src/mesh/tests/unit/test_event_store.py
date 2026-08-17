import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2] / "src"))

from mesh_v5.event_store.store import EventStore

def test_event_store():
    test_log_file = "test_events.jsonl"
    store = EventStore(storage_path=test_log_file)

    # Anexa um evento constitucional
    evt = store.append_event(
        event_type="CONSTITUTIONAL_VERIFICATION",
        payload={"trace_id": "trc_999", "status": "APPROVED"}
    )
    
    events = store.read_all_events()
    assert len(events) >= 1
    print("Test Event Store (Evento Registrado):", events[-1])

    # Limpeza do arquivo de teste temporário
    if os.path.exists(test_log_file):
        os.remove(test_log_file)

    print("\n✅ Teste do Event Store aprovado com sucesso!")

if __name__ == "__main__":
    test_event_store()
