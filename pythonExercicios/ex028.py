# Exercício 28 - Escreva um programa que faça um computador pensar em um número entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário ganhou ou perdeu.

from random import choice

try:
    n = int(input('Digite um número: '))
    print()

    if n > 5 or n < 0:
        print('Digite um número inteiro entre 0 e 5.')
    else:
        choosed = choice(range(0, 5))

        if n == choosed:
            print('Você acertou!')
        else:
            print('Você errou.')

except:
    print('Digite um número inteiro entre 0 e 5.')