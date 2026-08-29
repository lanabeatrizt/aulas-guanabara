# Desafio 020:
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de
# trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos
# e mostre a ordem sorteada.
import random
nome1 = input('Nome do aluno 1: ')
nome2 = input('Nome do aluno 2: ')
nome3 = input('Nome do aluno 3: ')
nome4 = input('Nome do aluno 4: ')
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista) # embaralha a lista diretamente
print(f'A ordem de apresentação será: {lista}')