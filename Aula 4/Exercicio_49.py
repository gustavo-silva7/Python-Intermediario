# Sistema Integrado
# Sistema com cadastro, busca, ordenacao, relatorios e menu interativo.

registros = []

while True:
    print("\n1 - Cadastrar produto")
    print("2 - Buscar produto")
    print("3 - Ordenar por preco")
    print("4 - Relatorio")
    print("0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        preco = float(input("Preco: "))
        quantidade = int(input("Quantidade: "))
        registros.append({"nome": nome, "preco": preco, "quantidade": quantidade})
    elif opcao == "2":
        busca = input("Produto buscado: ")
        encontrados = [
            item for item in registros if busca.lower() in item["nome"].lower()
        ]
        print(encontrados if encontrados else "Produto nao encontrado.")
    elif opcao == "3":
        registros.sort(key=lambda item: item["preco"])
        print("Produtos ordenados por preco.")
    elif opcao == "4":
        print("\nRelatorio:")
        for item in registros:
            total = item["preco"] * item["quantidade"]
            print(
                f"{item['nome']} - R$ {item['preco']:.2f} "
                f"- qtd: {item['quantidade']} - total: R$ {total:.2f}"
            )
    elif opcao == "0":
        break
    else:
        print("Opcao invalida.")
