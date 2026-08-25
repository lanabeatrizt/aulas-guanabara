# Desafio 010:
# Crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira e mostre quantos Dólares ela pode comprar.
# Considere US$ = R$ 3.27.
reais = float(input('Quantos de dinheiro você tem na carteira? R$ '))
DOLAR = 3.27
conversao = reais / DOLAR
print(f'Você pode comprar {conversao:.2f} dólares.')