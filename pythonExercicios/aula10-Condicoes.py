tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
  print('Carro novo!')
else:
  print('Carro velho.')

# Outra forma de fazer:

print('Carro novo!' if tempo <= 3 else 'Carro velho.')

# ------------------

nome = str(input('Digite seu nome: '))
if nome == 'Gustavo':
  print('Que nome lindo!')
print('Bom dia, {}.'.format(nome))

# ------------------

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

print('Sua média foi {}.'.format(m))

if m >= 6:
  print('Sua média foi boa!')
else:
  print('Precisa estudar mais.')

# Outra forma:

print('Parabéns!' if m >= 6 else 'Estude mais.')

