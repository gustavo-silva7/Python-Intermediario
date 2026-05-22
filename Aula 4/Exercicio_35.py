# Sistema Escolar
# Cadastre alunos e organize-os pela media final.

alunos = [
    {"nome": "Ana", "media": 8.5},
    {"nome": "Bruno", "media": 6.9},
    {"nome": "Carla", "media": 9.2},
]

ordenados = sorted(alunos, key=lambda aluno: aluno["media"], reverse=True)

print("Alunos por media final:")
for aluno in ordenados:
    print(f"{aluno['nome']} - media {aluno['media']:.1f}")
