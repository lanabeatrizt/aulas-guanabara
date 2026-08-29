# Desafio 012:
# Faça um algoritmo que leia o preço de um produto e mostre o seu
# novo preço, com 5% de desconto.
preco = float(input('Qual o preço do produto? R$ '))
novo_preco = preco - (preco * 5 / 100)
print(f'O valor com desconto de 5% é R$ {novo_preco:.2f}')