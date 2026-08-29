# Desafio 035:
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# Obs.: tem um princípio matemático que trata disso!
# Princípio da desigualdade triangular: Para que três segmentos de reta formem um triângulo, a medida de qualquer um dos 
# lados deve ser sempre menor do que a soma dos outros dois lados.
print(f'Analisador de triângulos. Informe a medida do:')
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os seguimentos acima podem formar um triângulo')
else:
    print(f'Os seguimentos acima não podem formar um triângulo')