# \033[style text backm
# \033[0;33;44m
# style 0(nada), 1(negrito), 4(underline), 7(negativo)
#  cor 30(branco), 31(vermelho), 32(verde), 33(amarelo), 34(azul), 35(roxo), 36(azul piscina), 37(cinza)
# back 40          41            42         43           44        45        46                47

print('\033[1:31:43mOlá, Mundo!')
print('\033[1:31:43mOlá, Mundo!\033[m')
print('\033[1:31:43mOlá, Mundo!')
print('\033[1:30:45mOlá, Mundo!\033[m')
print('\033[33:44mOlá, Mundo!\033[m')
print('\033[7:33:44mOlá, Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Lucas'
print('Muito prazer, {}{}{}.'.format('\033[4:34m', nome.upper(), '\033[m'))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'
         }

print('Muito prazer, {}{}{}.'.format(cores['amarelo'], nome.upper(), cores['limpa']))
