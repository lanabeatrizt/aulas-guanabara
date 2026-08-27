# Desafio 018:
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.
import math
angulo = float(input('Informe um ângulo qualquer: '))
angulo_radiano = math.radians(angulo) # pq o angulo em graus tem que converter para radianos
seno = math.sin(angulo_radiano)
cosseno = math.cos(angulo_radiano)
tangente = math.tan(angulo_radiano)
print(f'O ângulo {angulo} tem o seno de {seno:.2f}, o cosseno de {cosseno:.2f} e a tangente de {tangente:.2f}')