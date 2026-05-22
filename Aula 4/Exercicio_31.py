# Agenda de Eventos
# Cadastre eventos com nome, data e local, permitindo busca por nome.

eventos = [
    {"nome": "Feira de Ciencias", "data": "10/06/2026", "local": "Auditorio"},
    {"nome": "Palestra", "data": "15/06/2026", "local": "Sala 2"},
    {"nome": "Mostra Cultural", "data": "20/06/2026", "local": "Patio"},
]

busca = input("Nome do evento: ")

for evento in eventos:
    if busca.lower() in evento["nome"].lower():
        print(f"{evento['nome']} - {evento['data']} - {evento['local']}")
        break
else:
    print("Evento nao encontrado.")
