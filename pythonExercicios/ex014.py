# Exercício 14 - Escreva um programa que converta um temperatura digitada em Celsius para Farenheit.

temp = float(input('Qual a temperatura em oC? '))
print('A temperatura de {:.2f} oC corresponde a {:.2f} oF.'.format(temp, temp * 9 / 5 + 32))
