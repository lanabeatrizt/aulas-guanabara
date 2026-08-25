# Desafio 008:
# Escreva um programa que leia um valor em metros e o exiba
# convertido em centímetros e milímetros.
valor = int(input('Informe uma distância em metros: '))
km = valor / 1000
dm = valor * 10
cm = valor * 100
mm = valor * 1000
print(f'O valor de {valor}m corresponde a {km}km, {dm}dm, {cm}cm e {mm}mm')