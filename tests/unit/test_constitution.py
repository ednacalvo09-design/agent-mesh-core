import sys
from pathlib import Path

# Adiciona 'src' ao PATH do Python
sys.path.append(str(Path(__file__).resolve().parents[2] / "src"))

from mesh_v5.constitution.verifier import ConstitutionVerifier

def test_constitution():
    verifier = ConstitutionVerifier()

    # Caso 1: Ação válida
    valid_action = {
        "trace_id": "trc_12345",
        "agent": "MasterAgent",
        "payload": "git status"
    }
    res_valid = verifier.verify_proposal(valid_action)
    print("Test 1 (Ação Válida):", res_valid)
    assert res_valid["approved"] is True

    # Caso 2: Ação proibida (comando destrutivo)
    invalid_action = {
        "trace_id": "trc_67890",
        "agent": "RogueAgent",
        "payload": "sudo rm -rf /"
    }
    res_invalid = verifier.verify_proposal(invalid_action)
    print("Test 2 (Comando Proibido):", res_invalid)
    assert res_invalid["approved"] is False

    # Caso 3: Ação sem trace_id
    untraced_action = {
        "agent": "UnknownAgent",
        "payload": "ls -la"
    }
    res_untraced = verifier.verify_proposal(untraced_action)
    print("Test 3 (Sem Trace ID):", res_untraced)
    assert res_untraced["approved"] is False

    print("\n✅ Todos os testes constitutivos passaram perfeitamente!")

if __name__ == "__main__":
    test_constitution()
