# Comparacao de Algoritmos
# Compare o tempo de execucao entre Bubble Sort e Quick Sort.

from time import perf_counter


def bubble_sort(lista):
    valores = lista[:]
    for i in range(len(valores)):
        for j in range(0, len(valores) - i - 1):
            if valores[j] > valores[j + 1]:
                valores[j], valores[j + 1] = valores[j + 1], valores[j]
    return valores


def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[len(lista) // 2]
    menores = [valor for valor in lista if valor < pivo]
    iguais = [valor for valor in lista if valor == pivo]
    maiores = [valor for valor in lista if valor > pivo]
    return quick_sort(menores) + iguais + quick_sort(maiores)


numeros = [64, 34, 25, 12, 22, 11, 90, 5, 77, 1, 43, 18]

inicio = perf_counter()
ordenado_bubble = bubble_sort(numeros)
tempo_bubble = perf_counter() - inicio

inicio = perf_counter()
ordenado_quick = quick_sort(numeros)
tempo_quick = perf_counter() - inicio

print("Lista original:", numeros)
print("Bubble Sort:", ordenado_bubble)
print(f"Tempo Bubble Sort: {tempo_bubble:.8f} segundos")
print("Quick Sort:", ordenado_quick)
print(f"Tempo Quick Sort: {tempo_quick:.8f} segundos")
