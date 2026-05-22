# Controle de Estoque Avancado
# Cadastre produtos e gere relatorios organizados por quantidade.

produtos = [
    {"nome": "Arroz", "quantidade": 30},
    {"nome": "Feijao", "quantidade": 18},
    {"nome": "Cafe", "quantidade": 45},
]

relatorio = sorted(produtos, key=lambda produto: produto["quantidade"], reverse=True)

print("Relatorio de estoque por quantidade:")
for produto in relatorio:
    print(f"{produto['nome']} - {produto['quantidade']} unidades")
