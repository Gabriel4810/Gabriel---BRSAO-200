"""
3 - Crie um programa que consulte informações de um  na API , retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.
"""

import requests

def verifica_CEP(cep):

  aux = cep.replace("-","").replace(".","").strip()

  if aux.isdigit() and len(aux) == 8:

    try:

      response = requests.get(f"https://viacep.com.br/ws/{aux}/json/?")
      response.raise_for_status()
      dados = response.json()

      if dados.get("erro"):

        return None

      logradouro = dados['logradouro']
      bairro = dados['bairro']
      cidade = dados['localidade']
      estado = dados['estado']

      return logradouro, bairro, cidade, estado

    except requests.RequestException as e:

      print(f'Erro na requisição: {e}')
      return None

  else:
    print("CEP Inválido. Informe 8 dígitos (xxxxx-xxx)")
    return None

def main():

  print(f"\t ~~~~ Consulta CEP ~~~~")
  
  while(True):
    
    cep = input("Entre com um CEP no formato (xxxxx-xxx): ")

    resultado = verifica_CEP(cep)

    if resultado:

      logradouro, bairro, cidade, estado = resultado
      print(f"Cidade: ", {cidade})
      print(f"Logradouro: ", {logradouro})
      print(f"Bairro: ", {bairro})
      print(f"Estado: ", {estado})
    
    else:
      print("Não foi possível consultar o CEP informado")

    nova_consulta = input("Deseja fazer uma nova consulta de CEP? Digite (S/N) ").strip().lower()

    if nova_consulta != 's':
      break
if __name__ == '__main__':
  main()