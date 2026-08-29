# Desafio 024:
# Crie um programa que leia o nome de uma cidade e diga se 
# ela começa ou não com o nome "Santo".
cidade = str(input('Diga o nome de uma cidade: ')).strip()
print(f'A cidade {cidade} começa com "Santo"? {cidade[:5].upper() == 'SANTO'}')
# mpegou os 5 indices, colocou em upper case, 
# caso a pessoa escreva de várias formas o santo e assim 
# pôde comprar se era igual a SANTO