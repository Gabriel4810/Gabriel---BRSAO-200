"""
1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).
"""

while(True):
  try:
    N1 = input("Digite o Primeiro Número: ")
    N1 = float(N1)
    break
  except ValueError:
    print(f"Insira Apenas Números - DADOS INVÁLIDOS - ")

while(True):
  try:
    N2 = input("Digite o Segundo Número: ")
    N2 = float(N2)
    break
  except ValueError:
    print(f"Insira Apenas Números - DADOS INVÁLIDOS - ")

op = ""

while(True):
  print("\nOperações Possiveis\n")
  print("Digite + para Somar")
  print("Digite - para Subtrair")
  print("Digite * para Multiplicar")
  print("Digite / para Dividir\n")
  print("Digite sair para terminar o programa")
  try:
    op = input(" ")
    if op in ['+','-','/','*']:
      print("\nRealizando Operações")
      if op == '+':
        print(f"Soma de {N1} + {N2}")
        print(f"{N1 + N2}")
      if op == '-':
        print(f"Subtração de {N1} - {N2}")
        print(f"{N1 - N2}")
      if op == '*':
        print(f"Multiplicação de {N1} * {N2}")
        print(f"{N1 * N2}")
      
      if op == '/':
        try:
          print(f"Divisão de {N1} /  {N2}")
          print(f"{N1 / N2}")
        except ZeroDivisionError:
          print(f"O segundo número é  {N2} (ZERO)")
          while(True):
            try:
              N2_str = input("\nDigite o novo valor para o segundo número: ")
              N2 = float(N2_str)
              if N2 == 0:
                print("\nO novo valor também é ZERO. Tente novamente.")
              else:
                print(f"\nNovo Resultado: de {N1} / {N2} =  {N1 / N2}")
                break
            except ValueError:
              print(f"'{N2_str}' Não é um número.")
              
    elif op == 'sair':
      print("Programa FINALIZADO\n")
      break
      
    else:
      raise ValueError("Opção Inválida")
      
  except ValueError:
    print("Coloque apenas Números permitidos")
    print(f"Você tentou inserir um dígito que não é permitido -> {op}")