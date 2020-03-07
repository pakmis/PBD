dias_da_semana = (1,2,3,4,5,6,7)
dia = int (input ("Digite o numero correspondente ao dia da semana(ex: 1- Domingo): "))
if dia in dias_da_semana:
  if dia == 1:
    print(f'{dia} - Domingo')
  elif dia == 2:
    print(f'{dia} - Segunda')
  elif dia == 2:
    print(f'{dia} - Terça')
  elif dia == 2:
    print(f'{dia} - Quarta')
  elif dia == 2:
    print(f'{dia} - Quinta')
  elif dia == 2:
    print(f'{dia} - Sexta')
  else:
    print(f'{dia} - Sábado')
else:
  print(f"Você digitou '{dia}' que é um numero invalido")