"""
4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.
"""

from datetime import datetime

def dias_vida(dia, mes, ano_nascimento, dia_hoje):
  data = f"{dia}/{mes}/{ano_nascimento}"
  vida_inicial = datetime.strptime(data, "%d/%m/%Y")
  return dia_hoje - vida_inicial

def main():
  try:
    dia = int(input("Informe o seu dia de nascimento: "))
    mes = int(input("Informe o seu mês de nascimento: "))
    ano = int(input("Informe o seu ano de nascimento: "))

    today = datetime.now()

    vidas = dias_vida(dia, mes, ano, today)

    if vidas.days < 0:
      print(f"Algum dado seu deve estar errado...\n")
    else:
      print(f"Você está vivo nesse mundo a {vidas.days} dias")

  except ValueError:
    print("Apenas dados numérios são permitidos")

if __name__ == "__main__":
  main()