# Agenda Escolar
# Cadastre disciplinas e horarios, permitindo busca pelo nome da disciplina.

disciplinas = [
    {"nome": "Matematica", "horario": "08:00"},
    {"nome": "Portugues", "horario": "10:00"},
    {"nome": "Historia", "horario": "13:00"},
]

busca = input("Nome da disciplina: ")

for disciplina in disciplinas:
    if disciplina["nome"].lower() == busca.lower():
        print(f"{disciplina['nome']} - {disciplina['horario']}")
        break
else:
    print("Disciplina nao encontrada.")
