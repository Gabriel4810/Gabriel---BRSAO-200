"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

Temperatura = float(input("Indique a Temperatura a ser convertida: "))
Unidade = str(input("Indique a unidade (C para Celsius, F para Fahrenheit, K para Kelvin): ")).lower()
Converter = str(input(f"Indique qual a unidade deseja converter (C, F, K): ")).lower()
Resultado = 0.0


if Unidade == Converter:
    print(f"A conversão não é necessária . A temperatura já está em {Unidade}.")
    resultado = Temperatura


elif Converter == 'c':
    if Unidade == 'f':
        
        resultado = (Temperatura - 32) * 5/9
        print(f"{Temperatura}°F é igual a {resultado:.2f}°C")
    elif Unidade == 'k':
        
        resultado = Temperatura - 273.15
        print(f"{Temperatura}K é igual a {resultado:.2f}°C")
    else:
        print(f"Unidade de origem '{Unidade}' inválida.")


elif Converter == 'f':
    if Unidade == 'c':
        
        resultado = (Temperatura * 9/5) + 32
        print(f"{Temperatura}°C é igual a {resultado:.2f}°F")
    elif Unidade == 'k':
        
        resultado = (Temperatura - 273.15) * 9/5 + 32
        print(f"{Temperatura}K é igual a {resultado:.2f}°F")
    else:
        print(f"Unidade de origem '{Unidade}' inválida.")


elif Converter == 'k':
    if Unidade == 'c':
        
        resultado = Temperatura + 273.15
        print(f"{Temperatura}°C é igual a {resultado:.2f}K")
    elif Unidade == 'f':
        
        resultado = (Temperatura - 32) * 5/9 + 273.15
        print(f"{Temperatura}°F é igual a {resultado:.2f}K")
    else:
        print(f"Unidade de origem '{Unidade}' inválida.")


else:
    print(f"Unidade de destino '{Converter}' inválida.")