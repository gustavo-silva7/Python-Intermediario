# Sistema de Delivery
# Registre pedidos de delivery e organize pelo valor total.

pedidos = [
    {"cliente": "Ana", "valor_total": 45.90},
    {"cliente": "Bruno", "valor_total": 72.50},
    {"cliente": "Carla", "valor_total": 31.00},
]

ordenados = sorted(pedidos, key=lambda pedido: pedido["valor_total"], reverse=True)

print("Pedidos por valor total:")
for pedido in ordenados:
    print(f"{pedido['cliente']} - R$ {pedido['valor_total']:.2f}")
