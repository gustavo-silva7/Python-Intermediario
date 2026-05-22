# Controle de Livros
# Cadastre livros e organize-os por ano de publicacao.

livros = [
    {"titulo": "Dom Casmurro", "ano": 1899},
    {"titulo": "Capitaes da Areia", "ano": 1937},
    {"titulo": "O Alienista", "ano": 1882},
]

ordenados = sorted(livros, key=lambda livro: livro["ano"])

print("Livros por ano de publicacao:")
for livro in ordenados:
    print(f"{livro['titulo']} - {livro['ano']}")
