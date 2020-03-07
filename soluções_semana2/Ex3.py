ano = int(input("Digite o ano a ser verificado: "))
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
	print('Este ano é Bissexto')
else:
	print('Este ano não é Bissexto')