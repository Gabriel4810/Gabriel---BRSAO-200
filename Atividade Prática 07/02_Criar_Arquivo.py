"""
2 - Crie um programa que cria um arquivo  com nome, idade e cidade de algumas pessoas, que este programa escreva os dados em formato tabular e salva no arquivo escolhido pelo usuário, caso ocorra um erro ao salvar, mostre uma mensagem de falha. 
"""

import csv

def escrever_dados(nome_arquivo):

    if not nome_arquivo.endswith('.csv'):
        nome_arquivo += '.csv'

    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        escrever = csv.writer(arquivo_csv)
        escrever.writerow(['nome', 'idade', 'cidade'])
        
        while True:
            print("\n~~~~ Novo Registro ~~~~")
            nome = input('Informe o nome: ')
            idade = input('Informe a idade: ')
            cidade = input('Informe a cidade: ')
 
            escrever.writerow([nome, idade, cidade])
            print(f"✓ {nome}, {idade}, {cidade} salvos com sucesso.")
            
            entrada = input('Deseja inserir mais dados? (s/n): ').lower()
            if entrada != 's':
                break

if __name__ == '__main__':
    nome_arquivo = input("Digite o Nome do Arquivo csv: ")
    escrever_dados(nome_arquivo)
    print(f"Arquivo {nome_arquivo} fechado.")