"""
4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.
"""

Pares = 0
Impares = 0

while True:
    Entrada = input("Digite um Número (ou 'fim'): ")    
    if Entrada.lower() == 'fim':
        print("\nCalculando Resultados...")
        break   
    try:
        Numero = int(Entrada)       
       
        if Numero % 2 == 0:
            print(f"-> {Numero} é Par.")
            Pares = Pares + 1
        else:
            print(f"-> {Numero} é Ímpar.")
            Impares = Impares + 1

    except ValueError:        
        print(f"Dado inválido. '{Entrada}' Não é um número inteiro.")
       

print(f"Total  Pares: {Pares}")
print(f"Total  Ímpares: {Impares}")