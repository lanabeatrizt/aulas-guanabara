# Desafio 011:
# Faça um programa que leia a largura e a algura de uma parede
# em metros, calcule sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta pinta uma área
# de 2m2.
largura = float(input('Largura: '))
altura = float(input('Altura: '))
area = largura * altura
litros = area / 2
print(f'Você precisa de {litros} litros')