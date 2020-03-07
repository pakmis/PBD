n1, n2 = float(input("Digite a primeira nota: ")), float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
print(f"Nota 1: {n1}")
print(f"Nota 2: {n2}")
print(f"Média: {media}")
print('Reprovado' if media < 7 else ('Aprovado com Distinção' if media == 10 else 'Aprovado'))
