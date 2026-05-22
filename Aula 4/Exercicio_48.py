# Controle de Pacientes
# Cadastre pacientes e busque informacoes pelo nome.

pacientes = [
    {"nome": "Ana", "idade": 30, "convenio": "Sim"},
    {"nome": "Bruno", "idade": 45, "convenio": "Nao"},
    {"nome": "Carla", "idade": 22, "convenio": "Sim"},
]

busca = input("Nome do paciente: ")

for paciente in pacientes:
    if busca.lower() in paciente["nome"].lower():
        print(
            f"{paciente['nome']} - {paciente['idade']} anos "
            f"- convenio: {paciente['convenio']}"
        )
        break
else:
    print("Paciente nao encontrado.")
