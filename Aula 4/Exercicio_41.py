# Sistema de Hotel
# Cadastre hospedes e organize-os pelo numero do quarto.

hospedes = [
    {"nome": "Ana", "quarto": 204},
    {"nome": "Bruno", "quarto": 101},
    {"nome": "Carla", "quarto": 305},
]

ordenados = sorted(hospedes, key=lambda hospede: hospede["quarto"])

print("Hospedes por quarto:")
for hospede in ordenados:
    print(f"Quarto {hospede['quarto']} - {hospede['nome']}")
