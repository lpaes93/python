# Exercício 34 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
# Para salários superiores a 1.250 reais. Calcule um aumento de 10%. Para os inferiores ou iguais o aumento é de 15%.
sal = float(input('Digite o salário: '))

if sal > 1250:
  print('O salário reajustado em 10% é R${:.2f}.'.format(sal * 1.1))
else:
  if sal <= 1250:
    salFinal = sal * 1.15
    print(f'O salário reajustado em 15% é R${salFinal:.2f}.')
    print('O salário reajustado em 15% é R${:.2f}.'.format(salFinal))
  else:
    if sal <= 0:
      print('Digite um valor maior que 0!')
