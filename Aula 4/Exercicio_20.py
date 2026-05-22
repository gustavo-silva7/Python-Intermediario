# Controle de Tarefas
# Cadastre tarefas diarias, permitindo buscar e organizar por prioridade.

tarefas = [
    {"descricao": "Estudar Python", "prioridade": 2},
    {"descricao": "Enviar trabalho", "prioridade": 1},
    {"descricao": "Ler livro", "prioridade": 3},
]

busca = input("Digite a tarefa buscada: ")
encontradas = [tarefa for tarefa in tarefas if busca.lower() in tarefa["descricao"].lower()]

print("\nTarefas encontradas:")
for tarefa in encontradas:
    print(f"{tarefa['descricao']} - prioridade {tarefa['prioridade']}")

print("\nTarefas por prioridade:")
for tarefa in sorted(tarefas, key=lambda tarefa: tarefa["prioridade"]):
    print(f"{tarefa['descricao']} - prioridade {tarefa['prioridade']}")
