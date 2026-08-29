# Desafio 026:
# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A".
# - Em que posição aparece a primeira vez.
# - Em que posição aparece a última vez.
frase = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra "A" aparece {frase.count('a')} vezes na frase')
print(f'A primeira letra "A" apareceu na posição {frase.find('a')+1}') # pq a primeira posição é 0
print(f'A última letra "A" apareceu na posição {frase.rfind('a')+1}') # searches a string for a specified substring and returns the highest index (the rightmost or last occurrence) where that substring is found