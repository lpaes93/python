# Exercício 4 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite algo: ')

print('O tipo é ', type(algo))
print('É um dígito?', algo.isdigit())
print('É somente espaços? ', algo.isspace())
print('É um número? ', algo.isnumeric())
print('É alfabético', algo.isalpha())
print('É alfanumérico? ', algo.isalnum())
print('Está em minúscula? ', algo.islower())
print('Está em maiúscula? ', algo.isupper())
