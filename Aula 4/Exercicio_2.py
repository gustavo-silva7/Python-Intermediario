# Ranking da Turma 
# Monte um ranking de alunos da maior nota para a menor utilizando o algoritmo Selection Sort. 
turma = []

def selection_sort(alunos):
    n = len(alunos)
    for i in range(n):
        nota_maior = i #Nota maior que muda no decorrer do codigo

        for a  in range(i+1, n):
            #compara as nota anterios com a proxima se a atual for mair mantem a variavel se nao muda para a maior
            if alunos[a] ['nota'] > alunos[nota_maior] ['nota']: 
                nota_maior = a

        # Só trocamos de lugar DEPOIS de descobrir quem tem a maior nota de verdade
        alunos[i], alunos[nota_maior] = alunos[nota_maior], alunos[i] #troca as posiçoes
    return alunos

quant = int(input("Quantos alunos deseja cadastrar: "))
for i in range(quant):
    print()
    nome = input(f"Digite o nome do(a) {i+1}° aluno(a): ")
    nota = int(input(f"Digite a nota do(a) {nome}: "))

    aluno = {"nome": nome, "nota": nota}
    turma.append(aluno)

ranking = selection_sort(turma)

print("\nRANKING DA TURMA")
for posicao, aluno in enumerate(ranking, start=1):
    print(f"{posicao}º Lugar: {aluno['nome']} - Nota: {aluno['nota']}")