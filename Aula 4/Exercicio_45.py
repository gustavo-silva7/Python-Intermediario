# Sistema de Oficina
# Cadastre servicos realizados e organize-os pelo valor.

servicos = [
    {"descricao": "Troca de oleo", "valor": 150.00},
    {"descricao": "Alinhamento", "valor": 120.00},
    {"descricao": "Revisao completa", "valor": 650.00},
]

ordenados = sorted(servicos, key=lambda servico: servico["valor"])

print("Servicos por valor:")
for servico in ordenados:
    print(f"{servico['descricao']} - R$ {servico['valor']:.2f}")
