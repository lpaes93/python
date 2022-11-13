# Exercício 8 - Dê entrada de uma distância em metros e retorne a conversão em km, hm, dam, dm, cm, mm.

d = float(input('Digite uma disância em metros: '))

km = d / 1000 # Quilômetro
hm =  d / 100 # Hectômetro
dam = d / 10 # Decâmetro
dm = d * 10 # Decímetro
cm = d * 100 # Centímetro
mm =  d * 1000 # Milímetro

print(f'A medida {d:.2f} metros corresponde a:\n\033[1:31m{km:.2f} km.\n{hm:.1f} hm.\n{dam:.0f} dam.\n{dm:.0f} dm.\n{cm:.0f} cm.\n{mm:.0f} mm.')
