nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'A sua média foi: {media}')
if media >= 6.0:
    print(f'Sua média foi boa, parabéns!')
else:
    print(f'Sua média foi ruim, estude mais!')