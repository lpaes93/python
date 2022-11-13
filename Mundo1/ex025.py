# Exercício 25 - Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva?', nome.lower().find('silva') != -1)

#Outra forma de fazer:
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
