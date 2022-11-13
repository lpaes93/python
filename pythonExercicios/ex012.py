# Exercício 12 - Faça um algoritmo que leia o preço do produto e mostre seu novo preço com 5% de desconto.

preco = float(input('Qual é o preço do produto? '))

print('O produto que custava R${:.2f}, na promoção com 5% de desconto vai custar R${:.2f}.'.format(preco, preco * 0.95))
