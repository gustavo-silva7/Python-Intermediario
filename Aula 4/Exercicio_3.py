# Busca de Produto 
# Crie uma lista de produtos e implemente uma Busca Linear para localizar 
# um produto pelo nome. 

mercado = ["Arroz", "Feijão", "Macarrão", "Azeite", "Biscoito"]

def cadastrar_produtos(lista_mercado):
    nome_produto = input("Adicione o produto na lista: ")
    lista_mercado.append(nome_produto)
    print(f"{nome_produto} adicionado com sucesso!")


def busca_linear(lista_produto, nome_produto):
    for produto in lista_produto:
        if produto.lower() == nome_produto.lower():
            return f"Produto {produto} encontrado!"
        
    
    return "Produto não encontrado!"
    
def exibir_menu():
    print("ESCOLHA UMA OPÇÃO DIGITANDO O NUMERO CORRESPONDENTE")
    print("1 - CADASTRAR PRODUTO")
    print("2 - BUSCAR PRODUTOS")
    print("3 - SAIR")
    print()

while True:
    exibir_menu()
    escolha = int(input("Escolha: "))
    print()

    if escolha == 1:
        cadastrar_produtos(mercado)

    elif escolha == 2:
        if len(mercado) == 0:
            print("MERCADO VAZIO\n")
            resposta = input("DESEJA CADASTRAR PRODUTOS AGORA (S ou N): ").upper()
            if resposta == "S":
                cadastrar_produtos(mercado)

            if resposta == "N":
                print("VOLTANDO AO MENU PRINCIPAL...\n")
                continue
                
            else:
                print("RESPOSTA INVALIDA, TENTE NOVAMNETE!")
                continue

        else:
            termo_busca = input("Digite o nome do produto que deseja buscar: ")
            resultado = busca_linear(mercado, termo_busca)
            print(resultado)
            print()

    elif escolha == 3:
        print("ENCERRANDO...")
        break

    else:
        print("RESPOSTA INVALIDA. TENTE NOVAMNETE")
        continue
