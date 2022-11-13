# Exercício 30 - Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
try:
    n = int(input('Digite um número inteiro: '))

    if n == 0:
        print('{} é um elemento neutro.'.format(n))
    else:
        if n % 2 == 0:
            print('{} é par'.format(n))
        else:
            print('{} é ímpar.'.format(n))

except:
    print('Digite somente números inteiros!')