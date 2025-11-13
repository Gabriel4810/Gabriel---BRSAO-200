"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""
Produto = "Camiseta"
Preço_Original = 50.00
Porcentagem_Desconto = 20.00

Desconto = Preço_Original * (Porcentagem_Desconto/100)
Preço_Final = Preço_Original - Desconto

print("--- Detalhes da Compra ---")
print(f"Nome do Produto: {Produto}")
print(f"Preço original: R$ {Preço_Original:.2f}")
print(f"Porcentagem do Desconto: {Porcentagem_Desconto:} %")
print(f"Valor do desconto: R$ {Desconto:.2f}")

print(f"Preço final com desconto: R$ {Preço_Final:.2f}")

