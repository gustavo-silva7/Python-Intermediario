# Sistema de Cursos
# Cadastre cursos e organize-os pela quantidade de alunos.

cursos = [
    {"nome": "Python", "alunos": 35},
    {"nome": "JavaScript", "alunos": 28},
    {"nome": "Banco de Dados", "alunos": 42},
]

ordenados = sorted(cursos, key=lambda curso: curso["alunos"], reverse=True)

print("Cursos por quantidade de alunos:")
for curso in ordenados:
    print(f"{curso['nome']} - {curso['alunos']} alunos")
