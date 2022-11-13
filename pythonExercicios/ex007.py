# Exercício 7 - Dê entrada de duas notas e traga sua média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

print(f'A média entre {n1} e {n2} é {media}.')

# Outra forma de fazer:

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

print('A média entre {} e {} é {}'.format(n1, n2, ((n1 + n2) / 2)))
