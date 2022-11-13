# Exercício - Faça um programa que peça entrada de um número e retorne o número com seu antecessor e sucessor.

num = int(input('Digite um número: '))

ant = num - 1
suc = num + 1

print(f'Analisando o valor {num}, seu antecessor é {ant} e o sucessor é {suc}.')

# Outra forma de fazer

num = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}.'.format(num, (num - 1), (num + 1)))
