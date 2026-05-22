# Sistema de Transporte
# Cadastre veiculos de transporte e organize-os pela capacidade.

veiculos = [
    {"tipo": "Van", "capacidade": 15},
    {"tipo": "Onibus", "capacidade": 45},
    {"tipo": "Micro-onibus", "capacidade": 28},
]

ordenados = sorted(veiculos, key=lambda veiculo: veiculo["capacidade"])

print("Veiculos por capacidade:")
for veiculo in ordenados:
    print(f"{veiculo['tipo']} - {veiculo['capacidade']} passageiros")
