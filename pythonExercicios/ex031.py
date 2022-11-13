# Exercício 31 - Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem cobrando 0.50 reais por km para viagens até 200 km e 0.45 reais para viagens mais longas.
try:
    d = float(input('Digite a distância da viagem em km: '))

    if d <= 0:
        print('Digite um número positivo.')
    else:
        if d <= 200:
            preco = d * 0.5
            print('O preço da passagem é R${:.2f}.'.format(preco))
        else:
            preco = d * 0.45
            print('O preço da passagem é R${:.2f}.'.format(preco))


except:
    print('Digite somente números!')
