"""
MESH v5.0 — Event Store Imutável
Gerencia o log de eventos append-only para auditoria e reprodução de estados.
"""

import json
import time
from pathlib import Path
from typing import Dict, Any, List

class EventStore:
    """Registrador imutável de eventos (Append-Only Audit Log)."""

    def __init__(self, storage_path: str = "events_log.jsonl"):
        self.storage_path = Path(storage_path)

    def append_event(self, event_type: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Anexa um novo evento ao log imutável com timestamp e metadados.
        """
        event = {
            "timestamp": time.time(),
            "event_type": event_type,
            "payload": payload
        }

        with open(self.storage_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(event) + "\n")

        return event

    def read_all_events(self) -> List[Dict[str, Any]]:
        """
        Lê todo o histórico de eventos imutável do disco.
        """
        if not self.storage_path.exists():
            return []

        events = []
        with open(self.storage_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    events.append(json.loads(line))
        return events
