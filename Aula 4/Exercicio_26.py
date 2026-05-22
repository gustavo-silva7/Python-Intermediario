# Lista de Presenca
# Registre presenca de alunos e busque um aluno pelo nome.

presencas = ["Ana", "Bruno", "Carla", "Diego"]
busca = input("Nome do aluno: ")

if busca in presencas:
    print(f"{busca} esta presente.")
else:
    print(f"{busca} nao foi encontrado na lista.")
