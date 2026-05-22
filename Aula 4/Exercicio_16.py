# Quick Sort
# Implemente o algoritmo Quick Sort para ordenar uma lista de valores.


def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[len(lista) // 2]
    menores = [valor for valor in lista if valor < pivo]
    iguais = [valor for valor in lista if valor == pivo]
    maiores = [valor for valor in lista if valor > pivo]
    return quick_sort(menores) + iguais + quick_sort(maiores)


valores = [10, 7, 8, 9, 1, 5]
print("Valores originais:", valores)
print("Valores ordenados:", quick_sort(valores))
