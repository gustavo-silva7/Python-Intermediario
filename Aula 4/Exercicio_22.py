# Controle de Gastos
# Registre despesas mensais e organize os valores do maior para o menor.

despesas = [1200.00, 85.50, 320.00, 42.90, 600.00]
despesas_ordenadas = sorted(despesas, reverse=True)

print("Despesas do maior para o menor:")
for valor in despesas_ordenadas:
    print(f"R$ {valor:.2f}")
