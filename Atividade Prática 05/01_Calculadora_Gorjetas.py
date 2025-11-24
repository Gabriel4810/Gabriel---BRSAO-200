"""
1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros:
a - valor_conta (float): O valor total da conta
b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
c - retorna: float: O valor da gorjeta calculada
"""

def calc_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * porcentagem_gorjeta / 100.00

def main():
    print("~~~~ Calculadora de Gorjetas ~~~~")
    nome_garcom = input("Digite o nome do Garçom que vai receber a gorjeta: ")
    
    try:
        valor_conta = float(input("Informe o valor total da conta R$: "))
        porcentagem_gorjeta = float(input("Digite o valor da porcentagem a ser dada (Ex: 20): "))
        valor_da_gorjeta = calc_gorjeta(valor_conta, porcentagem_gorjeta)
        total_com_gorjeta = valor_conta + valor_da_gorjeta
        
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print(f"Calculadora da Gorjeta para o Garçom: {nome_garcom}")
        print(f"Valor da Conta: R$ {valor_conta:.2f}")
        print(f"Valor a ser recebido de Gorjeta: R$ {valor_da_gorjeta:.2f}")
        print(f"Total a ser Pagar (Conta + Gorjeta): R$ {total_com_gorjeta:.2f}")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        
    except ValueError:
        print("\n[Erro] Digite apenas números para o valor da conta e a porcentagem (utilize ponto para decimais).")
if __name__ == "__main__":
    main()