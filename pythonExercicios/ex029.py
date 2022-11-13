# Exercício 29 - Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 km/h mostre uma mensagem dizendo que ele foi multado. A multa vai custar 7 reais por cada km acima do limite.
try:
  v = float(input('Digite a velocidade em km/h: '))

  if v > 80:
    multa = (v - 80) * 7
    print('Multa de R${:.2f}'.format(multa))
  8
except:
  print('Digite um valor numérico.')
