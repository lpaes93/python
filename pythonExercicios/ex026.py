# Exercício 26 - Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "a";
# Em que posição ela aparece a primeira vez;
# Em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip().lower()

print('A letra "a" apareceu {} vezes.'.format(frase.count('a')))
print(f'A posição que ela apareceu primeiro foi {frase.find("a") + 1}.')
print('A última vez que o "a" aparece é na posição {}.'.format(frase.rfind('a') + 1))
