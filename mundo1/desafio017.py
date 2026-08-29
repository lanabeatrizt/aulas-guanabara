# Desafio 017:
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de
# um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
cat_op = float(input('Qual o comprimento do cateto oposto: '))
cat_adj = float(input('Qual o comprimento do cateto adjacente: '))
hipotenusa = hypot(cat_op, cat_adj)
# hipotenusa = (cat_op ** 2 + cat_adv ** 2) ** (1/2) modo matemático sem o math
print(f'A hipotenusa é: {hipotenusa:.2f}')