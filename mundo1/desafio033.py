# Desafio 033:
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
numero1 = float(input('Digite o número 1: '))
numero2 = float(input('Digite o número 2: '))
numero3 = float(input('Digite o número 3: '))
# checagem maior número
if numero1 > numero2 or numero1 > numero3:
    print(f'O número 1 {numero1} é o maior número')
    if numero2 > numero1 or numero2 > numero3:
        print(f'O número 2 {numero2} é o maior número')
else:
    print(f'O número 3 {numero3} é o maior número')
# checagem menor número
if numero1 < numero2 and numero1 < numero3:
    print(f'O número 1 {numero1} é o menor número')
    if numero2 < numero1 and numero2 < numero3:
        print(f'O número 2 {numero2} é o menor número')
else:
    print(f'O número 3 {numero3} é o menor número')