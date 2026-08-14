"""
MESH v5.0 — Motor de Governança (Proposal Gate)
Coordena a submissão de propostas, verificação constitucional e registro imutável.
"""

from typing import Dict, Any
from mesh_v5.constitution.verifier import ConstitutionVerifier
from mesh_v5.event_store.store import EventStore

class GovernanceEngine:
    """Motor central de validação e aprovação de propostas de agentes."""

    def __init__(self, event_store: EventStore = None):
        self.verifier = ConstitutionVerifier()
        self.event_store = event_store or EventStore()

    def process_proposal(self, proposal: Dict[str, Any]) -> Dict[str, Any]:
        """
        Submete uma proposta ao fluxo rigoroso de governança MESH.
        """
        # 1. Validação Constitucional
        verification = self.verifier.verify_proposal(proposal)

        # 2. Construção da resposta de governança
        governance_result = {
            "trace_id": proposal.get("trace_id"),
            "agent": proposal.get("agent"),
            "approved": verification["approved"],
            "status": verification["status"],
            "violations": verification["violations"]
        }

        # 3. Registro obrigatório no Event Store imutável
        self.event_store.append_event(
            event_type="GOVERNANCE_PROPOSAL_EVALUATED",
            payload=governance_result
        )

        return governance_result
