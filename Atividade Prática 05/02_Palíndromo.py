"""
2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""

import unicodedata

def eh_palindromo(texto):
    txt = unicodedata.normalize('NFKD', texto)

    limpa = ''.join(
        ch.lower() for ch in txt
        if ch.isalnum()
    )
    
    invertido = limpa[::-1]
    return limpa == invertido

def main():
    print("\n~~~~ Verificador de Palíndromos  ~~~~")
    print("Reconhece Frases, Acentos e Pontuação.")
    txt = input("Digite o texto: ")

    if eh_palindromo(txt):
        print(f"\nSim! \"{txt}\" é um Palíndromo.")
    else:
        print(f"\nNão. \"{txt}\" não é um Palíndromo.")

if __name__ == "__main__":
    main()