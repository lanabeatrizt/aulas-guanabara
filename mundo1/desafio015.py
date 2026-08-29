# Desafio 015:
# Escreva um programa que pergunte a quantidade de Km
# percorridos por um carro e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que
# o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado.

dias = int(input('Informe quantos dias o veículo foi alugado: '))
km = float(input('Informe quantos Km o carro rodou: '))
VALOR_DIARIA = 60
VALOR_1KM = 0.15
valor_aluguel = dias * VALOR_DIARIA
valor_km = km * VALOR_1KM
total = valor_aluguel + valor_km
print(f'O preço a pagar de aluguel é R$ {valor_aluguel:.2f} e de km rodada é R$ {valor_km:.2f}, totalizando R$ {total:.2f}')