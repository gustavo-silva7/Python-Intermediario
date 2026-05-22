# Controle de Salarios
# Cadastre salarios de funcionarios e organize do menor para o maior.

funcionarios = [
    {"nome": "Ana", "salario": 3200.00},
    {"nome": "Bruno", "salario": 2500.00},
    {"nome": "Carla", "salario": 4100.00},
]

ordenados = sorted(funcionarios, key=lambda funcionario: funcionario["salario"])

print("Funcionarios por salario:")
for funcionario in ordenados:
    print(f"{funcionario['nome']} - R$ {funcionario['salario']:.2f}")
