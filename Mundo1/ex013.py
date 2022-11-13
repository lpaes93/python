# Exercício 13 - Faça um algoritmo que leia o salário do funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input('Qual o salário? '))
print('\nUm funcionário que ganhava R${:.2f}, com 15% de aumento, passa a ganhar R${:.2f}.'.format(salario, salario * 1.15))
