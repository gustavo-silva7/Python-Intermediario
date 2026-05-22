# Sistema de Estoque 
# Gerencie um estoque contendo nome, preço e quantidade dos produtos. 
# Inicializando o estoque

estoque = [
    {"nome": "Camiseta", "preco": 49.90, "quantidade": 20},
    {"nome": "Calça Jeans", "preco": 119.90, "quantidade": 15},
    {"nome": "Tênis", "preco": 199.90, "quantidade": 8}
]

# Função para exibir o estoque
for item in estoque:
    total_valor = item["preco"] * item["quantidade"]
    print(f"Produto: {item['nome']} | Qtd: {item['quantidade']} | Total em Estoque: R${total_valor:.2f}")