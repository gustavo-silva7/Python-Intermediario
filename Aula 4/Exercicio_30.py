# Controle de Medicamentos
# Cadastre medicamentos contendo nome, preco e quantidade em estoque.

medicamentos = [
    {"nome": "Dipirona", "preco": 8.50, "quantidade": 20},
    {"nome": "Paracetamol", "preco": 12.00, "quantidade": 15},
    {"nome": "Vitamina C", "preco": 25.90, "quantidade": 8},
]

print("Medicamentos cadastrados:")
for medicamento in medicamentos:
    print(
        f"{medicamento['nome']} - R$ {medicamento['preco']:.2f} "
        f"- estoque: {medicamento['quantidade']}"
    )
