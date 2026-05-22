# Lista Telefônica 
# Monte uma lista telefônica contendo nome e telefone. 
# Permita buscar um contato pelo nome. 

lista_telefonica = {
    "João": "11 99999-1111",
    "Maria": "21 98888-2222",
    "Lucas": "31 97777-3333",
    "Ana": "11 99111-2222",
    "Pedro": "21 98222-3333",
    "Beatriz": "31 97333-4444",
    "Carlos": "41 96444-5555",
    "Mariana": "51 95555-6666",
    "Ricardo": "61 94666-7777",
    "Julia": "71 93777-8888",
    "Gabriel": "81 92888-9999",
    "Larissa": "91 91999-0000",
    "Fernando": "11 99888-1111",
    "Camila": "21 98777-2222",
    "Gustavo": "31 97666-3333",
    "Sofia": "41 96555-4444",
    "Bruno": "51 95444-5555",
    "Amanda": "61 94333-6666",
    "Rodrigo": "71 93222-7777",
    "Isabela": "81 92111-8888",
    "Thiago": "91 91000-9999",
    "Letícia": "11 98999-1234",
    "Mateus": "21 97888-5678" 
}

contato = input("Digite o contato que vc quer buscar: ").capitalize()

if contato in lista_telefonica:
    print(f"O telefone de {contato} é {lista_telefonica[contato]}")

else:
    print("Não encontrado")
