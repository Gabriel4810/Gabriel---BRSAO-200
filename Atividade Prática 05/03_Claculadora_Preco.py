"""
3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.
"""

def preco_desconto(preco_produto, desconto):
  return preco_produto * desconto / 100.00

def preco_final(preco_inicial, preco_desconto):
  return preco_inicial - preco_desconto

def main():
  print(f"\nCalculadora de Preço Final do Produto com Desconto\n")
  while(True):
    try:
      preco = float(input(f"Informe o Preço do Produto: "))
      
    except ValueError:
      print("Digite apenas Dados Numéricos")
    try:
      desconto = float(input("Insira o Desconto que será Aplicado em % "))
      
    except ValueError:
      print("Digite apenas Dados Numéricos")
    break

  desconto_dado = preco_desconto(preco, desconto)
  total = preco_final(preco, desconto_dado)

  print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
  print(f"Preço do Produto sem Desconto R$ {preco:.2f}")
  print(f"Desconto de {desconto:.2f} % aplicado")
  print(f"Valor do Desconto R$ {desconto_dado:.2f} reais")
  print(f"Preço Final R$ {total:.2f} reais")
  print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

if __name__ == "__main__":
    main()