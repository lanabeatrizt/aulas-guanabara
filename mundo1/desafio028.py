# Desafio 028
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir  qual foi o número escolhido pelo computador.
#
# O programa deverá escrever na rela se o usuário venceu ou perdeu.
from random import randint
from time import sleep # para dar um efeito de pensar legal
pensar = randint(0, 5)
descobrir = int(input('Tente descobrir o número que eu pensei, de 0 a 5: '))
print(f'Processando...')
sleep(3)
if pensar == descobrir:
    print(f'Parabéns, você acertou! Eu pensei no número {pensar}.')
else:
    print(f'Você errou, eu pensei no número: {pensar} e não {descobrir}.')