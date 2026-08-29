# Desafio 013:
# Faça um algoritimo que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento.
salario = float(input('Qual o salário do funcionário? R$ '))
salario_reajustado = salario + (salario * 15 / 100)
print(f'O salário reajustando é: R$ {salario_reajustado:.2f}')