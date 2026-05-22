# Controle de Produtos
# Cadastre produtos e permita busca pelo nome.

produtos = [
    {"nome": "Caderno", "preco": 18.90},
    {"nome": "Caneta", "preco": 2.50},
    {"nome": "Mochila", "preco": 120.00},
]

busca = input("Nome do produto: ")

for produto in produtos:
    if busca.lower() in produto["nome"].lower():
        print(f"{produto['nome']} - R$ {produto['preco']:.2f}")
        break
else:
    print("Produto nao encontrado.")
