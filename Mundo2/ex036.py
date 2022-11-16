# Exercício 36 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal sabendo que não pode exceder 30% do salário ou então o empréstimo será negado.
try:
    val = float(input('Digite o valor da casa: '))
    sal = float(input('Digite o seu salário: '))
    t = int(input('Em quantos anos pretende pagar? '))

    p = val / (t * 12)

    if p <= 0.3 * sal:
        print('\nO valor da prestação é \033[31mR${:.2f}\033[m e será paga em \033[31m{:.0f}\033[m prestações.'.format(p, t * 12))
    else:
        print('\nEmpréstimo negado.')
except:
    print('Digite um valor númerico.')
    