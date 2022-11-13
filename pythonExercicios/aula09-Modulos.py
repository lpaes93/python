#        012345678901234567890
frase = 'Curso em Vídeo Python'

# Fatiamento
print()
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

# Análise
print()
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))

# Essa string não existe em 'frase'. Logo, retornará -1:
print(frase.find('Android'))
'Curso' in frase

# Transformação

# Substitui 'Python' por 'Andorid':
print()
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())

# Somente o primeiro caracter maiúsculo:
print(frase.capitalize())

# Cada palavra começa com maiúsculo:
print(frase.title())

print()

frase = '   Aprenda Python  '
print(frase)

# Remove os espaços inúteis:
print(frase.strip())

# Remove somente os espaços a direita:
print(frase.rstrip())

# Remove somente os espaços a esquerda:
print(frase.lstrip())

print()

frase = 'Curso em Vídeo Python'
print(frase)
print(frase.split())
print('-'.join(frase.split()))

print("""Curso em Vídeo Android
CURSO EM VÍDEO PYTHON
curso em vídeo python
Curso em vídeo python
Curso Em Vídeo Python""")
