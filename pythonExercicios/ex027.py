# Exercício 27 - Faça um programa que laia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo: ')).strip()
nome_lista = nome.split()

print('\nMuito prazer!')
print('Seu primeiro nome é {}.'.format(nome_lista[0]))
print(f'Seu último nome é {nome_lista[-1]}.')
