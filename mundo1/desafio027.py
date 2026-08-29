# Desafio 027:
# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
# Ex.: Ana Maria de Souza
# primeiro = Ana
# último = Souza
nome = str(input('Qual seu nome completo? ')).strip()
print(f'Seu primeiro nome é: {nome.split()[0]}')
print(f'Seu último nome é: {nome.split()[-1]}')
# Fiz diferente do Guanabara (ele complicou sem precisar)