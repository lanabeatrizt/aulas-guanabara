# Desafio 029:
# Escreva um programa que leia a velociadade de um carro.
#
# Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado.
#
# A multa vai custar R$ 7,00 por cada Km acima do limite.
LIMITE = 80
TAXA_MULTA = 7
velocidade = int(input('Informe a velocidade em Km/h: '))
if velocidade > LIMITE:
    multa = (velocidade - LIMITE) * TAXA_MULTA
    print(f'Você excedeu o limite de velocidade de {LIMITE}Km/h e sua multa é de: R$ {multa:.2f}')
print(f'Tenha um bom dia e dirija com segurança!')