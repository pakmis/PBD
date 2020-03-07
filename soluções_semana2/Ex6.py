tipos_carnes = [
  (1, "F.Duplo","R$ 4,90 por Kg", "R$ 5,80 por Kg"),
  (2, "Alcatra","R$ 5,90 por Kg", "R$ 6,80 por Kg"),
  (3, "Picanha","R$ 6,90 por Kg", "R$ 7,80 por Kg"),
]
print('Opção:\tTipo:\tAté 5Kg:\tAcima 5kg:')
opcoes = []
for opcao, carne, valor1, valor2 in tipos_carnes:
  print(f'{opcao}\t{carne}\t{valor1}\t{valor2}')
  opcoes.append(opcao)
(carne, valor1, valor2) = tipos_carnes
opcao, quantidade = int(input("Digite a opção da carne desejada: ")), float(input(f"Digite a quatidade de carne desejada(em Kg): "))
if opcao in opcoes:
  if opcao == 1:
    if quantidade < 5:
      valor = 4.9
      tipo_valor = 1
    else:
      valor = 5.8
      tipo_valor = 2
  elif opcao == 2:  
    if quantidade < 5:
      valor = 5.9
      tipo_valor = 1
    else:
      valor = 6.8
      tipo_valor = 2
  else:
    if quantidade < 5:
      valor = 6.9
      tipo_valor = 1
    else:
      valor = 7.8
      tipo_valor = 2
  print(f'Opção:{opcao} - {tipos_carnes[opcao-1][1]}')
  print(f'Quantidade de carne pedida: {quantidade}Kg')
  total_base = quantidade*valor
  print(f'Valor inicial: R${total_base}')
  tipo_pgtos = [
    (1, "Dinheiro", 1),
    (2, "Cartão de Credito", 1),
    (3, "Cartão de Debito", 1),
    (4, "Cartão Tabajara", 0.95)
  ]
  opcoes_pgto = []
  for opcao1, tipo, valor in tipo_pgtos:
    print(f"{opcao1}\t{tipo}")
    opcoes_pgto.append(opcao1)
  tipo_pgto = int(input("Digite a opção do tipo de pagamento desejado: "))
  if tipo_pgto in opcoes_pgto:
    print(f"Tipo de pagamento: {tipo_pgtos[tipo_pgto-1][1]}")
    print("Valor do desconto: R${total_base*0.05}" if tipo_pgto == 4 else "Valor do desconto: R$0")
    print("Valor Total: R$total_base*0.95}" if tipo_pgto == 4 else f"Valor Total: R${total_base}")
  else: 
    print(f'Opção: {tipo_pgto} é Inválida!')
else:
  print(f'Opção: {opcao} é Inválida!')