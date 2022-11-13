# Exercício 10 - Conversor de moedas.

real = float(input('Digite quanto tem na carteira: '))
print('\nCom \033[31mR${:.2f}\033[m você pode comprar \033[36m${:.2f}\033[m.'.format(real, real/5.29))
