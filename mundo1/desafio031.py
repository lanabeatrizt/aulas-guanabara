# Desafio 031:
# Desenvolva um programa que pergunte a distância de uma viagem dem Km. 
# Calcule o preço da passagem, # cobrando R$ 0,50 por Km para viagens de 
# até 200 Km e R$ 0,45 para viagens mais longas.
VALOR1 = 0.50
VALOR2 = 0.45
LIMITE = 200
distancia = float(input('Informe a distância da viagem em Km: '))
if distancia <= LIMITE:
    passagem = distancia * VALOR1
else:
    passagem = distancia * VALOR2
print(f'O valor da passagem é: R$ {passagem:.2f}')