# Sistema de Compras
# Organize produtos pelo preco.

produtos = [
    {"nome": "Arroz", "preco": 22.50},
    {"nome": "Feijao", "preco": 8.90},
    {"nome": "Cafe", "preco": 16.75},
    {"nome": "Leite", "preco": 5.20},
]

produtos_ordenados = sorted(produtos, key=lambda produto: produto["preco"])

print("Produtos por preco:")
for produto in produtos_ordenados:
    print(f"{produto['nome']} - R$ {produto['preco']:.2f}")
