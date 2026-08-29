# Desafio 019:
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome
# escolhido.
import random
nome1 = input('Informe o nome do aluno 1: ')
nome2 = input('Do aluno 2: ')
nome3 = input('Do aluno 3: ')
nome4 = input('Do aluno 4: ')
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi: {escolhido}')