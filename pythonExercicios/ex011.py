# Exercício 11 - Faça um programa que leia a largura e altura de uma parede em metros e calcule a sua área e a quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta pinta uma área de 2 m2.

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))

print('\nSua parede tem a dimensão {:.2f} x {:.2f} e sua área é {:.3f} m2.'.format(largura, altura, largura * altura))

# cada 2 m2 precisa de 1 l de tinta
print('Para pintar essa parade, você precisará de {:.2f} litros de tinta.'.format((largura * altura) / 2))
