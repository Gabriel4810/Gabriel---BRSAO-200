"""
4 - Crie um programa que realize consultas a  em relação ao Real (BRL) usando a API mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.
"""

import requests

def consultar_cotacao():
    print("~~~~ Consulta de Cotação (vs BRL) ~~~~")
    print("Exemplos de códigos: USD (Dólar), EUR (Euro), GBP (Libra), BTC (Bitcoin)")
    
    moeda = input("Digite o Código da Moeda Desejada: ").upper().strip()
    
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            dados = response.json()
            
            chave_moeda = f"{moeda}BRL"
            
            if chave_moeda in dados:
                info = dados[chave_moeda]
                
                nome = info['name']
                atual = float(info['bid'])
                maximo = float(info['high'])
                minimo = float(info['low'])
                data_hora = info['create_date']
                
                print("\n" + "="*40)
                print(f"Moeda: {nome}")
                print(f"Cotação Atual: R$ {atual:.4f}")
                print(f"Mínimo do dia: R$ {minimo:.4f}")
                print(f"Máximo do dia: R$ {maximo:.4f}")
                print(f"Atualizado em: {data_hora}")
                print("="*40 + "\n")
            else:
                print("\nErro: Formato de Resposta Inesperado.")
        
        elif response.status_code == 404:
            print("\nErro: Moeda não Encontrada. Verifique o Código Digitado (ex: USD, EUR).")
        else:
            print(f"\nErro na Conexão: Código {response.status_code}")

    except Exception as e:
        print(f"\nOcorreu um Erro Crítico: {e}")

if __name__ == "__main__":
    consultar_cotacao()