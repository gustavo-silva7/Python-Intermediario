# Controle de Veiculos
# Cadastre veiculos contendo modelo, placa e ano.

veiculos = []

for i in range(3):
    print(f"\nVeiculo {i + 1}")
    modelo = input("Modelo: ")
    placa = input("Placa: ")
    ano = int(input("Ano: "))
    veiculos.append({"modelo": modelo, "placa": placa, "ano": ano})

print("\nVeiculos cadastrados:")
for veiculo in veiculos:
    print(f"{veiculo['modelo']} - {veiculo['placa']} - {veiculo['ano']}")
