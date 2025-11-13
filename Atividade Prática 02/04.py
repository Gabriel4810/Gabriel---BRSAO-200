"""
4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""

Distância_Percorrida = 300
Combustível_Gasto = 25.0

Consumo_Médio = Distância_Percorrida / Combustível_Gasto

print("=== Dados da Viagem ===")
print(f"Distância Percorrida: {Distância_Percorrida:.2f}Km")
print(f"Combustível Gasto: {Combustível_Gasto:.2f} Litros")
print(f"Consumo Médio: {Consumo_Médio:.2f} Km/L")