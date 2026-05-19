# Sistema de Alunos 
# Cadastre o nome e a nota de 5 alunos. Depois, organize as notas em ordem crescente utilizando o algoritmo Bubble Sort. 

alunos = []

def organiza_alunos(alunos):
    n = len(alunos)
    for i in range(n):
        for a in range(0, n - i - 1):
            if alunos[a] [1] > alunos[a + 1] [1]:#compara as notas
                alunos[a], alunos[a+1] = alunos[a+1], alunos[a]#troca os alunos de lugar
    return alunos

quant = int(input("Quantos alunos vc deseja comparar as notas: "))
for i in range(quant):
    nome = input("Nome do aluno(a): ")
    nota = float(input("Nota desse aluno(a): "))
    print()
    alunos.append((nome, nota))

ordenar = organiza_alunos(alunos)

print("\nAlunos ordenados por nota:")

for nome, nota in ordenar:
    print(f"{nome} - {nota}\n")