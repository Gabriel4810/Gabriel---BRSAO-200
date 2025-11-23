"""
1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais).
"""

Nome = input("Digite seu Nome: ")
Idade = int(input("Digite a sua Idade: "))

if Idade >= 0 and Idade <= 12:
    print(f"{Nome} é uma Criança de: {Idade} anos")

if Idade >= 13 and Idade <= 17:
    print(f"{Nome} é um Adolescente de: {Idade} anos")

if Idade >= 18 and Idade <= 59:
    print(f"{Nome} é uma Adulto(a) de: {Idade} anos")

if Idade >= 60:
    print(f"{Nome} é uma Idoso(a) de: {Idade} anos")