# Exercício 22 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas;
# O nome com todas as letras minúsculas;
# Quantas letras ao total sem considerar os espaços;
# Quantas letras tem o primeiro nome.

nome = str(input('Digite o nome completo: ')).strip()

print()
print(nome.upper())
print(nome.lower())
print()

qtd_letra = len(nome) - nome.count(' ')

print(f'O nome tem {qtd_letra} letras.')

pri_nome = nome.split()
pri_nome = len(pri_nome[0])

print(f'O primeiro nome tem {pri_nome} letras.')
