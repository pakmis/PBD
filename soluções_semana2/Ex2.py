n1, n2 = float(input("Digite a primeira nota: ")), float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
conceito = ''
resultado = 'APROVADO'
if media < 4:
	conceito = 'E'
	resultado = 'REPROVADO'
elif media < 6:
	conceito = 'D'
	resultado = 'REPROVADO'
elif media < 7.5:
	conceito = 'C'
elif media < 9:
	conceito = 'B'
else:
	conceito = 'A'
print(f'Nota 1: {n1}')
print(f'Nota 2: {n2}')
print(f'Média: {media}')
print(f'Conceito: {conceito}')
print(f'{resultado}')