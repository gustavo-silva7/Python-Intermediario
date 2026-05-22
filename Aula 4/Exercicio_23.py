# Cadastro de Clientes
# Cadastre clientes contendo nome, telefone e e-mail, com busca por nome.

clientes = [
    {"nome": "Ana Silva", "telefone": "1199999-1111", "email": "ana@email.com"},
    {"nome": "Bruno Lima", "telefone": "1198888-2222", "email": "bruno@email.com"},
    {"nome": "Carla Souza", "telefone": "1197777-3333", "email": "carla@email.com"},
]

busca = input("Nome do cliente: ")

for cliente in clientes:
    if busca.lower() in cliente["nome"].lower():
        print(f"{cliente['nome']} - {cliente['telefone']} - {cliente['email']}")
        break
else:
    print("Cliente nao encontrado.")
