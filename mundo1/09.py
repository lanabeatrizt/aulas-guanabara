# Operadores aritiméticos
# 
# soma, subtração, multiplicação e divisão: +, -, *, /
# potência: **
# divisão inteira: //
# resto da divisão: % modulo/mod
# 
# precisam de dois operandos os operadores, tem que usar dois símbolos # de igual ==
#
# Ordem de precedência:
# 1. primeiro parênteses ()
# 2. depois ** potências
# 3. depois *, /, // e %
# 4. por fim, soma + e subtração -

n1 = int(input('Digite um número: '))
raizcubica = n1**(1/3)
print(f'A raíz cúbica dele é: {raizcubica}')