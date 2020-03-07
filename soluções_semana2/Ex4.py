operacoes = ('+','-','*','/')
n1, n2 = float(input("Digite o primeiro numero: ")), float(input("Digite o segundo numero: "))
inop = input("Digite a operação desejada +,-,*,/: ")
if inop in operacoes: 
	if inop == '+':
		resultado = n1 + n2
	elif inop == '-':
		resultado = n1 - n2
	elif inop == '*':
		resultado = n1 * n2
	else:
		resultado = n1 / n2
	if resultado%2 == 0:
		print(f'O resultado é :{resultado}\nO numero é PAR')
	else:
		print(f'O resultado é : {resultado}\nO numero é IMPAR')
	if resultado < 0:
		print('O numero é NEGATIVO')
	else:
		print('O numero é POSITIVO')
	if resultado % 1 == 0:
		print('O numero é INTEIRO')
	else:
		print('O numero é DECIMAL')
else:
	print("Essa operação não é valida")