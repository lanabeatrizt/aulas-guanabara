# Desafio 034:
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
#
# Para os inferiores ou iguais, o aumento é de 15%.
LIMITE = 1250
AUMENTO1 = 0.10
AUMENTO2 = 0.15
salario = float(input('Informe o salário do funcionário: R$ '))
if salario > LIMITE:
    valor_aumento = salario * AUMENTO1
else:
    valor_aumento = salario * AUMENTO2
print(f'O valor do aumento foi: R$ {valor_aumento:.2f} então passará a ganhar R${salario + valor_aumento:.2f}')