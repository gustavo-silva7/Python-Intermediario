# Busca Binária 
# Utilize uma lista ordenada e implemente a Busca Binária para localizar um número informado pelo usuário. 

def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        
        if lista[meio] == alvo:
            return f"Número {alvo} encontrado na posição {meio}!"
        elif lista[meio] < alvo:
            esquerda = meio + 1  # Descarta a metade esquerda
        else:
            direita = meio - 1   # Descarta a metade direita
            
    return "Número não encontrado."

# A lista DEVE estar ordenada
numeros_ordenados = [5, 12, 18, 23, 35, 42, 50]
print(busca_binaria(numeros_ordenados, 35))