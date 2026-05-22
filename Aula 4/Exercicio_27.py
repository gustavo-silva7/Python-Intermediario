# Sistema Bancario Simples
# Cadastre contas bancarias e ordene os saldos do maior para o menor.

contas = [
    {"numero": "001", "titular": "Ana", "saldo": 1500.00},
    {"numero": "002", "titular": "Bruno", "saldo": 800.00},
    {"numero": "003", "titular": "Carla", "saldo": 2300.00},
]

ordenadas = sorted(contas, key=lambda conta: conta["saldo"], reverse=True)

print("Contas por saldo:")
for conta in ordenadas:
    print(f"{conta['numero']} - {conta['titular']} - R$ {conta['saldo']:.2f}")
