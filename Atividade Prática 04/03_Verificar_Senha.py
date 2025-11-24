"""
3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.
"""

while (True):
    Senha = input("Digite a sua Senha: ")
    if Senha.lower() == 'sair':
        print("Programa Encerrado")
        break
    try:
        if len(Senha) < 8:
            raise ValueError("Senha curta. Deve conter no minimo 8 caracteres.")
        
        Tem_Numero = False
        for caractere in Senha:
            if caractere.isdigit():
                Tem_Numero = True
                break 
        
        if not Tem_Numero:
            raise ValueError("Senha inválida. Deve ter pelo menos 1 número.")

        print(f"SUCESSO! A sua senha '{Senha}' é forte.")
        break 

    except ValueError as e:
        print(f"ERRO: {e}")