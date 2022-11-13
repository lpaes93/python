# Exercício 17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import sqrt

cat_op = float(input('Qual o comprimento do Cateto Oposto? '))
cat_adj = float(input('Qual o comprimento do Cateto Adjacente? '))

hipotenusa = math.sqrt(pow(cat_op, 2) + pow(cat_adj, 2))

print('\nQuando o cateto oposto for {} e o cateto adjacente for {} a hipotenusa será {:.2f}.'.format(cat_op, cat_adj, hipotenusa))

# Outra forma de fazer:
import math

co = float(input('Digite o cateto oposto. '))
ca = float(input('Digite o cateto adjacente. '))
hi = math.hypot(ca, co)

print(f'\nQuando o cateto oposto for {co} e o cateto adjacente for {ca} a hipotenusa será {hi:.2f}.')

# Outra forma:

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('\nQuando o cateto oposto for {} e o cateto adjacente for {} a hipotenusa será {:.2f}.'.format(co, ca, hi))
