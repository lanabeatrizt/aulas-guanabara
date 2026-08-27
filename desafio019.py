# Desafio 019:
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome
# escolhido.
import math
nome1 = input('Informe o nome do aluno 1: ')
nome2 = input('Do aluno 2: ')
nome3 = input('Do aluno 3: ')
nome4 = input('Do aluno 4: ')
escolhido = math.comb(0, 3)
print(f'O aluno escolhido foi: {escolhido}')