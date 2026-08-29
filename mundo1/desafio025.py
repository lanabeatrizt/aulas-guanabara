# Desafio 025:
# Crie um programa que leia o nome de uma pessoa e diga se 
# ela tem "Silva" no nome.
# True ou False
nome = str(input('Qual seu nome completo? ')).strip()
print(f'Você tem Silva no nome? {'SILVA' in nome.upper()}')