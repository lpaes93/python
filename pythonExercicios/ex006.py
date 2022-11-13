# Exercício 6 - Entre com um número e retorne o dobro, triplo e a raiz quadrada.

n = int(input('Digite um número: '))

print('O dobro de {} é {}.'.format(n, (n * 2)))
print('O triplo de {} é {}.'.format(n, (n * 3)))
print('A raiz de {} é {}.'.format(n, (n ** (1/2))))

# Outra forma de fazer:

n = int(input('Digite um número: '))

n2 = n * 2
n3 = n * 3

# Eleva a um expoente.
nraiz = pow(n, (1/2))

print(f'O dobro de {n} é {n2}.')
print(f'O triplo de {n} é {n3}.')
print(f'A raiz de {n} é {nraiz}.')
