# Busca em Lista
# Busque um numero especifico utilizando Busca Linear.


def busca_linear(lista, numero):
    for indice, valor in enumerate(lista):
        if valor == numero:
            return indice
    return -1


numeros = [4, 8, 15, 16, 23, 42]
numero_buscado = int(input("Digite o numero buscado: "))
posicao = busca_linear(numeros, numero_buscado)

if posicao == -1:
    print("Numero nao encontrado.")
else:
    print(f"Numero encontrado na posicao {posicao}.")
