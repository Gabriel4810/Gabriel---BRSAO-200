"""
4 -   Crie um programa que leia e escreva arquivos no formato , que salve em um dicionário com nome, idade e cidade em um arquivo JSON e depois leia o mesmo arquivo exibindo os dados, caso o arquivo não existir ou ocorrer erro ao salvar, mostre uma mensagem de falha.
"""

import json
import os

def escrever_json(nome_arquivo):

    if not nome_arquivo.endswith('.json'):
        nome_arquivo += '.json'

    lista_pessoas = []

    while True:
        print("\n~~~~ Novo Cadastro ~~~~")
        nome = input('Informe o nome: ')
        idade = input('Informe a idade: ')
        cidade = input('Informe a cidade: ')

        pessoa = {
            "nome": nome,
            "idade": idade,
            "cidade": cidade
        }

        lista_pessoas.append(pessoa)

        continuar = input('Deseja Inserir Mais Dados? (s/n): ').lower()
        if continuar != 's':
            break

    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(lista_pessoas, arquivo, indent=4, ensure_ascii=False)

    print(f"\nDados Salvos com Sucesso em '{nome_arquivo}'.")

def ler_json(nome_arquivo):

    if not nome_arquivo.endswith('.json'):
        nome_arquivo += '.json'

    if not os.path.exists(nome_arquivo):
        print(f"Erro: O Arquivo '{nome_arquivo}' Não Existe.")
        return

    print(f"\n--- Lendo Arquivo {nome_arquivo} ---")

    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        dados_lidos = json.load(arquivo)

    for i, pessoa in enumerate(dados_lidos, 1):
        print(f"Pessoa {i}:")
        print(f"  Nome:   {pessoa['nome']}")
        print(f"  Idade:  {pessoa['idade']}")
        print(f"  Cidade: {pessoa['cidade']}")
        print("-" * 20)

if __name__ == '__main__':
    arquivo_nome = input("Informe o nome do arquivo JSON: ")

    escrever_json(arquivo_nome)

    ler_json(arquivo_nome)