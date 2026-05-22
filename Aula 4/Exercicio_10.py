# Sistema de Filmes
# Organize filmes pela avaliacao utilizando Quick Sort.


def quick_sort_filmes(filmes):
    if len(filmes) <= 1:
        return filmes

    pivo = filmes[len(filmes) // 2]["avaliacao"]
    menores = [filme for filme in filmes if filme["avaliacao"] < pivo]
    iguais = [filme for filme in filmes if filme["avaliacao"] == pivo]
    maiores = [filme for filme in filmes if filme["avaliacao"] > pivo]
    return quick_sort_filmes(maiores) + iguais + quick_sort_filmes(menores)


filmes = [
    {"titulo": "Matrix", "avaliacao": 9.0},
    {"titulo": "Avatar", "avaliacao": 8.1},
    {"titulo": "Interestelar", "avaliacao": 9.5},
    {"titulo": "Titanic", "avaliacao": 8.7},
]

print("Filmes por avaliacao:")
for filme in quick_sort_filmes(filmes):
    print(f"{filme['titulo']} - {filme['avaliacao']}")
