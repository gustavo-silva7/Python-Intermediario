# Sistema de Restaurante
# Cadastre pratos e organize-os pelo preco.

pratos = [
    {"nome": "Lasanha", "preco": 32.00},
    {"nome": "Salada", "preco": 18.50},
    {"nome": "Risoto", "preco": 40.00},
]

ordenados = sorted(pratos, key=lambda prato: prato["preco"])

print("Cardapio por preco:")
for prato in ordenados:
    print(f"{prato['nome']} - R$ {prato['preco']:.2f}")
