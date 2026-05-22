# Controle de Pedidos
# Cadastre pedidos e organize-os pela data.

from datetime import datetime

pedidos = [
    {"codigo": 101, "data": "15/05/2026"},
    {"codigo": 102, "data": "10/05/2026"},
    {"codigo": 103, "data": "20/05/2026"},
]

ordenados = sorted(
    pedidos,
    key=lambda pedido: datetime.strptime(pedido["data"], "%d/%m/%Y"),
)

print("Pedidos por data:")
for pedido in ordenados:
    print(f"Pedido {pedido['codigo']} - {pedido['data']}")
