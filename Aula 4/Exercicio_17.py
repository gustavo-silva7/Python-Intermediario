# Sistema de Vendas
# Gere um relatorio de vendas ordenado do maior valor para o menor.

vendas = [
    {"produto": "Notebook", "valor": 3500.00},
    {"produto": "Mouse", "valor": 80.00},
    {"produto": "Monitor", "valor": 1200.00},
    {"produto": "Teclado", "valor": 150.00},
]

relatorio = sorted(vendas, key=lambda venda: venda["valor"], reverse=True)

print("Relatorio de vendas:")
for venda in relatorio:
    print(f"{venda['produto']} - R$ {venda['valor']:.2f}")
