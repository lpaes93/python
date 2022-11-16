# Exercício 43 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: ABAIXO DO PESO
# - Entre 18.5 e 25: PESO IDEAL
# - 25 até 30: SOBREPESO
# - 30 até 40: OBESIDADE
# - Acima de 40: OBESIDADE MÓRBITA
weight = float(input('Digite seu peso: '))
height = float(input('Digite sua altura: '))

imc = weight / height ** 2

if imc < 18.5:
    print(f'{imc:.2f}, ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print(f'{imc:.2f}, PESO IDEAL')
elif imc >= 25 and imc < 30:
    print(f'{imc:.2f}, SOBREPESO')
elif imc >= 30 and imc < 40:
    print(f'{imc:.2f}, OBESIDADE')
else:
    print(f'{imc:.2f}, OBESIDADE MÓBITA')
