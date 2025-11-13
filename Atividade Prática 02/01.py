"""
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""
Real = 100.00
Taxa_Dólar = 5.20
Taxa_Euro = 6.15

Dolar = Real / Taxa_Dólar
Euro = Real / Taxa_Euro

print (f"O Valor em Dolar é: US$ {Dolar:.2f}")
print (f"O Valor em Euro é: € {Euro:.2f}")