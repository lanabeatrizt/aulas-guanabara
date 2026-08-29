# Desafio 022:
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas.
# - O nome com todas minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.
nome = str(input('Qual o seu nome completo? ')).strip() # pra tirar os espaços antes e depois que o usuário pode digitar sem querer
print(f'Analisando seu nome')
print(f'Seu nome em maiúsculo fica: {nome.upper()}')
print(f'Seu nome em minúsculo fica: {nome.lower()}')
print(f'Seu nome tem {len(nome.replace(" ", ""))} letras ao todo')
print(f'Seu primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras')
# Fiz bem diferente do Guanabara