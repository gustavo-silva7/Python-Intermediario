# Controle Financeiro
# Registre receitas e despesas e mostre o saldo final.

receitas = [2500.00, 800.00, 450.00]
despesas = [1200.00, 350.00, 180.00]

total_receitas = sum(receitas)
total_despesas = sum(despesas)
saldo = total_receitas - total_despesas

print(f"Total de receitas: R$ {total_receitas:.2f}")
print(f"Total de despesas: R$ {total_despesas:.2f}")
print(f"Saldo final: R$ {saldo:.2f}")
