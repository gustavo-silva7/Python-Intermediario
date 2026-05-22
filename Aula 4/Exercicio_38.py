# Controle de Chamados
# Cadastre chamados tecnicos e organize-os pela prioridade.

chamados = [
    {"descricao": "Computador nao liga", "prioridade": 1},
    {"descricao": "Impressora sem tinta", "prioridade": 3},
    {"descricao": "Sistema fora do ar", "prioridade": 0},
]

ordenados = sorted(chamados, key=lambda chamado: chamado["prioridade"])

print("Chamados por prioridade:")
for chamado in ordenados:
    print(f"Prioridade {chamado['prioridade']} - {chamado['descricao']}")
