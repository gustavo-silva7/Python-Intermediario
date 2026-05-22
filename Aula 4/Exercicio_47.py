# Sistema de Locadora
# Cadastre filmes e organize-os pela avaliacao.

filmes = [
    {"titulo": "Matrix", "avaliacao": 9.0},
    {"titulo": "Avatar", "avaliacao": 8.1},
    {"titulo": "Interestelar", "avaliacao": 9.5},
]

ordenados = sorted(filmes, key=lambda filme: filme["avaliacao"], reverse=True)

print("Filmes por avaliacao:")
for filme in ordenados:
    print(f"{filme['titulo']} - {filme['avaliacao']}")
