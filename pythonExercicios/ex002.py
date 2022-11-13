# Exercício 2 - Faça um programa que leia o nome de uma pessoa e mostra uma mensagem de boas-vindas.

nome = input('Digite seu nome: ')
print('É um prazer te conhecer, \033[4:33m{}\033[m.'.format(nome))
print(f'É um prazer te conhecer, {nome}')
