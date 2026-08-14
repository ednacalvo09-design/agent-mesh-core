"""
MESH v5.0 — Orquestrador Central
Ponto de entrada único para execução de tarefas sob o Harness de Governança.
"""

from typing import Dict, Any
from mesh_v5.governance.engine import GovernanceEngine

class MeshOrchestrator:
    """Orquestrador MESH v5.0 que garante o fluxo sob governança."""

    def __init__(self, governance_engine: GovernanceEngine = None):
        self.governance = governance_engine or GovernanceEngine()

    def dispatch(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recebe uma tarefa, passa pelo Proposal Gate de Governança e agenda/executa.
        """
        # Submete a proposta ao Proposal Gate
        gov_response = self.governance.process_proposal(task)

        if not gov_response["approved"]:
            return {
                "executed": False,
                "reason": "EXECUTION_BLOCKED_BY_GOVERNANCE",
                "governance_details": gov_response
            }

        # Simulação de despacho e execução bem-sucedida do Agente
        return {
            "executed": True,
            "status": "COMPLETED",
            "agent": task.get("agent"),
            "trace_id": task.get("trace_id"),
            "result": f"Tarefa '{task.get('payload')}' executada com sucesso sob o MESH Harness v5.0."
        }
