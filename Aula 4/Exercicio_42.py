# Controle de Funcionarios
# Cadastre funcionarios e busque informacoes pelo nome.

funcionarios = [
    {"nome": "Ana", "cargo": "Analista", "salario": 3500.00},
    {"nome": "Bruno", "cargo": "Tecnico", "salario": 2800.00},
    {"nome": "Carla", "cargo": "Gerente", "salario": 6200.00},
]

busca = input("Nome do funcionario: ")

for funcionario in funcionarios:
    if busca.lower() in funcionario["nome"].lower():
        print(
            f"{funcionario['nome']} - {funcionario['cargo']} "
            f"- R$ {funcionario['salario']:.2f}"
        )
        break
else:
    print("Funcionario nao encontrado.")
