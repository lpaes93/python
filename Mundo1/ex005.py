# Exercício - Faça um programa que peça entrada de um número e retorne o número com seu antecessor e sucessor.

num = int(input('Digite um número: '))

ant = num - 1
suc = num + 1

print(f'Analisando o valor \033[4:33m{num}\033[m, seu antecessor é \033[4:34m{ant}\033[m e o sucessor é \033[4:34m{suc}\033[m.')

# Outra forma de fazer

num = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}.'.format(num, (num - 1), (num + 1)))
