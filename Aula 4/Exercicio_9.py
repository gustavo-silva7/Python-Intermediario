# Sistema de Biblioteca
# Cadastre livros contendo titulo, autor e ano de publicacao.

livros = []

for i in range(3):
    print(f"\nLivro {i + 1}")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    ano = int(input("Ano de publicacao: "))
    livros.append({"titulo": titulo, "autor": autor, "ano": ano})

print("\nLivros cadastrados:")
for livro in livros:
    print(f"{livro['titulo']} - {livro['autor']} ({livro['ano']})")
