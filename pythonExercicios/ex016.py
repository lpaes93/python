# Exercício 16 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.
from math import trunc
from math import trunc
n = float(input('Digite um valor: '))
n_int = trunc(n)

print('Valor digitado foi {} e sua porção inteira é {}.'.format(n, n_int))

# Outra forma de fazer:
n = float(input('Digite um número: '))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(n, int(n)))
