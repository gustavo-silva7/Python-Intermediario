# Sistema Completo
# Sistema com cadastro, busca, ordenacao e menu interativo.

itens = []

while True:
    print("\n1 - Cadastrar item")
    print("2 - Buscar item")
    print("3 - Ordenar itens")
    print("4 - Listar itens")
    print("0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        itens.append(input("Nome do item: "))
    elif opcao == "2":
        nome = input("Item buscado: ")
        print("Encontrado." if nome in itens else "Nao encontrado.")
    elif opcao == "3":
        itens.sort()
        print("Itens ordenados.")
    elif opcao == "4":
        print("Itens:", itens)
    elif opcao == "0":
        break
    else:
        print("Opcao invalida.")
