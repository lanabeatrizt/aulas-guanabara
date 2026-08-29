# Aula 08: Utilizando Módulos
# import math ou importar somente a funcionalidade sqrt, aí no raiz, não precisa usar math.sqrt, pode usar sqrt direto:
# mais módulos: https://docs.python.org/pt-br/3/tutorial/modules.html
from math import sqrt
numero = int(input('Digite um número: '))
raiz = sqrt(numero)
print(f'A raiz de {numero} é {raiz:.2f}')