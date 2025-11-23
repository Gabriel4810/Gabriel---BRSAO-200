"""
2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
"""

Peso = float(input("Digite seu Peso: "))
Altura = float(input("Digite sua Altura: "))

imc = Peso / (Altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")

if imc < 25:
    print("Peso normal")

if imc < 30:
    print("Sobrepeso")