"""
1 -  Crie um programa que lê um arquivo CSV de  com a biblioteca , calcule e exiba a  e o  da coluna tempo_execucao, caso e o arquivo não exista ou houver erro na leitura, mostre uma mensagem de erro. 
"""
import pandas as pd

def processar_logs_treinamento(nome_arquivo):
    try:
        df = pd.read_csv(nome_arquivo)
        media_tempo = df['tempo_execucao'].mean()
        desvio_padrao_tempo = df['tempo_execucao'].std()
        print(f"Média do Tempo de Execução: {media_tempo:.2f} segundos")
        print(f"Desvio Padrão do Tempo de Execução: {desvio_padrao_tempo:.2f} segundos")
    except FileNotFoundError:
        print(f"Erro: O Arquivo {nome_arquivo} não foi Encotrado.")
    except Exception as e:
        print(f"Ocorreu um Eerro ao Processar o Arquivo: {e}")

nome_arquivo = 'Logs_de_Treinamento.csv'
processar_logs_treinamento(nome_arquivo)