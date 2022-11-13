# Exercício 20 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

pri = str(input('Primeiro nome: '))
seg = str(input('Segundo nome: '))
ter = str(input('Terceiro nome: '))
qua = str(input('Quarto nome: '))

lista = [pri, seg, ter, qua]

shuffle(lista)

print('\nA ordem de apresentação será:')
print(lista)