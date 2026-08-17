class ProposerAgent:
    def __init__(self, agent_id):
        self.agent_id=agent_id
    def propose_action(self, action):
        print(f"[PROPOSER {self.agent_id}] propondo: {action}")
        return {"agent_id": self.agent_id, "action": action, "input_data": action, "output_data": "resultado"}
