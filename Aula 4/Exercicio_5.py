# Organizador de Números 
# Organize uma lista de números utilizando o algoritmo Insertion Sort. 

def insertion_sort(numeros):
    for i in range(1, len(numeros)):
        chave = numeros[i]
        j = i - 1
        # Move os elementos que são maiores que a chave para uma posição à frente
        while j >= 0 and numeros[j] > chave:
            numeros[j + 1] = numeros[j]
            j -= 1
        numeros[j + 1] = chave
    return numeros

numeros = []

quant = int(input("QUANTOS NUMEROS DESEJA ORGANIZAR: "))
for i in range(0, quant):
    n = float(input(f"Digite o {i + 1}° numero: "))
    numeros.append(n)

print(insertion_sort(numeros))