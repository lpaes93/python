# Exercício 18 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('\nO ângulo {} tem o seno {:.2f}.'.format(angulo, seno))
print('O ângulo {} tem o cosseno {:.2f}.'.format(angulo, cosseno))
print('O ângulo {} tem a tangente {:.2f}.'.format(angulo, tangente))
