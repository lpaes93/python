# Exercício 24 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome santo.
cidade = str(input('Digite uma cidade: ')).strip()
print(cidade[:5].lower() == 'santo')
