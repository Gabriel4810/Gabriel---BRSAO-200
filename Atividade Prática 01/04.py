"""
4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""
Produto = "Cadeira Infantil"
Preço_Unitário = 12.40
Quantidade = 3

Compra = Preço_Unitário * Quantidade

print("--- Detalhes da Compra ---")
print(f"Nome do Produto: {Produto}")
print(f"Preço Unitário: R$ {Preço_Unitário:.2f}")
print(f"Quantidade: {Quantidade:}")
print(f"Valor Total da Compra: R$ {Compra:.2f}")