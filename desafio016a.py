# Desafio 016:
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela
# a sua porção inteira. 
# Ex: Digite um número: 6.127.
# O número 6.127 tem a parte Inteira 6.
import math
numero = float(input('Informe um número real: '))
inteiro = math.trunc(numero)
print(f'O valor digitado foi {numero} e a sua porção inteira é: {inteiro}.')