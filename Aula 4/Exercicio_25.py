# Controle de Notas
# Cadastre notas de alunos e calcule a media da turma.

notas = []

for i in range(3):
    nome = input(f"Nome do aluno {i + 1}: ")
    nota = float(input("Nota: "))
    notas.append({"nome": nome, "nota": nota})

media = sum(aluno["nota"] for aluno in notas) / len(notas)

print("\nNotas cadastradas:")
for aluno in notas:
    print(f"{aluno['nome']} - {aluno['nota']:.1f}")

print(f"Media da turma: {media:.2f}")
