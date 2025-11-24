"""
1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  também escolha o tamanho da senha  para criar senhas seguras automaticamente.
"""

import random
import string

def gerar_senha(quantidade_caracteres):
  if quantidade_caracteres <= 0:
    while(True):
      try:
        quantidade_caracteres = int(input(f"{quantidade_caracteres} não é permitida. \nEntre uma quantidade maior que zero: "))
      except ValueError:
        print(f"Informação ainda está errada insira a Informação correta")
      break
  
  letras = string.ascii_letters
  numeros = string.digits
  caracteres ="!@#$%*()_-'`^~<>,.:;?/|°"

  palavra = letras + caracteres + numeros

  resultado = ''.join(random.choice(palavra) for _ in range(quantidade_caracteres))

  return resultado

def main():
  print("~~~~ Gerador de Senhas Fortes ~~~~")
  x = 0
  while(x == 0):
    try:
      tam = int(input(f"Digite a quantidade de caracteres para gerar uma senha forte: "))
      senha_forte = gerar_senha(tam)
      print(f"A Senha Forte Gerada é {senha_forte}")
      x = int(input('Digite 0 para gerar nova senha ou qualquer número para sair: '))
    except ValueError:
      print("Erro de Entrada ")

if __name__ == '__main__':
  main()