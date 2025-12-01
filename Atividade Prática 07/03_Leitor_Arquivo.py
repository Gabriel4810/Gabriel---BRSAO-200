"""
3 -  Crie um programa que leia um arquivo  informado pelo usuário, percorrendo cada linha do arquivo e a exibe na tela, caso o arquivo não seja encontrado, mostre uma mensagem de erro.
"""

import csv


def ler_csv(nome_arquivo):
    with open(nome_arquivo, 'r', newline='') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)


if __name__ == '__main__':

    entrada = input("Informe o nome do arquivo csv -> ")
    ler_csv(entrada)
    print("Arquivo Fechado")