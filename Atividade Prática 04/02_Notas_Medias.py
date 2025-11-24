"""
2 - Criar um código que registre as notas de alunos e calcular a média da turma.
"""

Soma = 0
Quantidade = 0
Aluno = 1

while(True):
  Notas = input(f"Digite a nota do {Aluno}° ou fim: ")
  if Notas == 'fim':
    print("\nResultados:\n")
    break
  
  try:
    Nota = float(Notas)
    if 0 <= Nota <= 10:
      Soma = Soma + Nota
      Quantidade = Quantidade + 1
      print(f"Nota do {Aluno}° foi registrada")
    else:
      print(f"Nota inserida fora do intervalo válido!!!")
  except ValueError:
    print("Dado inválido, informação ignorada")

  Aluno += 1
  
if Quantidade > 0:
  Media_Notas = Soma / Quantidade
  print(f"Total de Notas Registradas {Quantidade}")
  print(f"Média da Turma {Media_Notas:.2f}")

else:
  print("Nenhuma nota foi validada, sem dados para calcular")