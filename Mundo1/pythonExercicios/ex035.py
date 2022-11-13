# Exercício 35 - Desenvolva um programa que leia o comprimeto de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# Pra ser um triângulo a soma de dois lados é sempre menor que o terceiro lado.

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print('As retas {}, {} e {} formam um triângulo.'.format(r1, r2, r3))
else:
  print('As retas {}, {} e {} NÃO formam um triângulo.'.format(r1, r2, r3))
