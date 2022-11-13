# Exercício 9 - Exiba a tabuada completa do número digitado.

n = int(input('Digite um número: '))

n1 = n * 1
n2 = n * 2
n3 = n * 3
n4 = n * 4
n5 = n * 5
n6 = n * 6
n7 = n * 7
n8 = n * 8
n9 = n * 9
n10 = n * 10

print('----------------')
print(f'{n} * 1 = {n1}')
print(f'{n} * 2 = {n2}')
print(f'{n} * 3 = {n3}')
print(f'{n} * 4 = {n4}')
print(f'{n} * 5 = {n5}')
print(f'{n} * 6 = {n6}')
print(f'{n} * 7 = {n7}')
print(f'{n} * 8 = {n8}')
print(f'{n} * 9 = {n9}')
print(f'{n} * 10 = {n10}')
print('----------------')


# Outra forma de fazer:

n = int(input('Digite um número: '))

print('-' * 12)
print('{} x {:2} = {}'.format(n, 1, n * 1))
print('{} x {:2} = {}'.format(n, 2, n * 2))
print('{} x {:2} = {}'.format(n, 3, n * 3))
print('{} x {:2} = {}'.format(n, 4, n * 4))
print('{} x {:2} = {}'.format(n, 5, n * 5))
print('{} x {:2} = {}'.format(n, 6, n * 6))
print('{} x {:2} = {}'.format(n, 7, n * 7))
print('{} x {:2} = {}'.format(n, 8, n * 8))
print('{} x {:2} = {}'.format(n, 9, n * 9))
print('{} x {:2} = {}'.format(n, 10, n * 10))
print('-' * 12)
