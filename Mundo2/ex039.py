# Exercício 39 - Faça um programa que leia o ano de nascimento  de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime

sexo = str(input('Digite o sexo: [ H ] ou [ M ]: ').strip().upper())
born = int(input('Digite seu ano de nascimento: '))
idade = datetime.date.today().year - born

if sexo == 'M':
    print('\nVocê não precisa se alistar.')

elif sexo == 'H':
    print('\nQuem nasceu em {} tem {} anos em {}.'.format(born, idade, datetime.date.today().year))

    if idade < 18:
        print('\nFaltam {} anos para o seu alistamento.'.format(18 - idade))
        print('Seu alistamento será em {}.'.format(18 - idade + 2022))
    elif idade == 18:
        print('\nVocê deve se alistar este ano!')
    elif idade > 18:
        print('\nJá passou do ano de alistamento. Espero que tenha se alistado há {} anos.'.format(idade - 18))
        print('Seu alistamento aconteceu em {}.'.format(-1 * (idade - 18 - 2022)))

else:
    print('\nDigite somente [ H ] para homem ou [ M ] para mulher.')
