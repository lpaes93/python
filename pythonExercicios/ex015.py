# Exercício 15 - Escreva um programa que pergunte a quantidade de quilômetros percorridos por um carrro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

distancia = float(input('Quantos km percorreu? '))
dias = float(input('Quantos dias? '))

preco = 60 * dias + 0.15 * distancia

print('\nO preço total a pagar é {:.0f} reais. Você rodou {:.0f} km em {:.0f} dias.'.format(preco, distancia, dias))
